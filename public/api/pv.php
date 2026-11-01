<?php
// Cookie-free, anonymous page-view counter.
// Stored per day: page path, referring site domain, and whether the hit looked like a bot. Daily totals only.
// NOT stored: IP address, user-agent string, cookies, timestamps finer than a day, or any identifier.
// Data lives outside the web root (<repo root>/data/pv/, git-ignored, not served by .htaccess).
header('Cache-Control: no-store');
header('X-Robots-Tag: noindex, nofollow');
$dir = dirname(__DIR__, 2) . '/data/pv';
if (!is_dir($dir)) { @mkdir($dir, 0750, true); }

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // Aggregate report (anonymous daily totals only): /api/pv.php?days=30
    header('Content-Type: application/json');
    $days = max(1, min(400, (int)($_GET['days'] ?? 30)));
    $since = gmdate('Y-m-d', time() - ($days - 1) * 86400);
    $perDay = []; $perPage = []; $refs = []; $bots = 0;
    foreach (glob($dir . '/*.json') ?: [] as $f) {
        $m = json_decode(@file_get_contents($f), true) ?: [];
        foreach ($m as $day => $d) {
            if ($day < $since) continue;
            foreach (($d['p'] ?? []) as $path => $c) {
                $h = (int)($c['h'] ?? 0); $b = (int)($c['b'] ?? 0);
                $perDay[$day] = ($perDay[$day] ?? 0) + $h;
                if ($h) $perPage[$path] = ($perPage[$path] ?? 0) + $h;
                $bots += $b;
            }
            foreach (($d['r'] ?? []) as $dom => $n) { $refs[$dom] = ($refs[$dom] ?? 0) + (int)$n; }
        }
    }
    ksort($perDay); arsort($perPage); arsort($refs);
    echo json_encode([
        'since' => $since, 'days' => $days,
        'humanViews' => array_sum($perDay), 'botViews' => $bots,
        'perDay' => $perDay,
        'topPages' => array_slice($perPage, 0, 50, true),
        'topReferrers' => array_slice($refs, 0, 30, true),
        'updated' => gmdate('c'),
    ]);
    exit;
}
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); exit; }

$in = json_decode(file_get_contents('php://input', false, null, 0, 600), true);
if (!is_array($in)) { http_response_code(400); exit; }
$path = (string)($in['p'] ?? '');
if (!preg_match('#^/[A-Za-z0-9/_.-]{0,150}$#', $path) || strpos($path, '..') !== false) { http_response_code(400); exit; }
if (preg_match('#/index\.html$#', $path)) { $path = substr($path, 0, -10); }
$ref = strtolower((string)($in['r'] ?? ''));
if ($ref !== '' && !preg_match('#^[a-z0-9.-]{1,100}\.[a-z]{2,24}$#', $ref)) { $ref = 'other'; }
// Bot flag: decided from the user agent here, then the user agent is discarded (never written).
$ua = (string)($_SERVER['HTTP_USER_AGENT'] ?? '');
$bot = (!empty($in['b']) || $ua === '' || preg_match('/bot|crawl|spider|slurp|preview|headless|lighthouse|pagespeed|monitor|python|curl|wget|httpclient|scrape/i', $ua)) ? 'b' : 'h';
unset($ua);

$day = gmdate('Y-m-d');
$file = $dir . '/' . gmdate('Y-m') . '.json';
$fh = fopen($file, 'c+');
if (!$fh) { http_response_code(500); exit; }
flock($fh, LOCK_EX);
$data = json_decode(stream_get_contents($fh) ?: '{}', true) ?: [];
if (count($data[$day]['p'] ?? []) < 2000 || isset($data[$day]['p'][$path])) {
    $data[$day]['p'][$path][$bot] = ($data[$day]['p'][$path][$bot] ?? 0) + 1;
}
if ($ref !== '' && $bot === 'h' && (count($data[$day]['r'] ?? []) < 500 || isset($data[$day]['r'][$ref]))) {
    $data[$day]['r'][$ref] = ($data[$day]['r'][$ref] ?? 0) + 1;
}
ftruncate($fh, 0); rewind($fh);
fwrite($fh, json_encode($data));
fflush($fh); flock($fh, LOCK_UN); fclose($fh);
http_response_code(204);
