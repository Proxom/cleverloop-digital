<?php
// Anonymous demand counter. No cookies, no IP or user-agent stored: only daily totals per product and event.
header('Content-Type: application/json');
header('Cache-Control: no-store');
$PRODUCTS = ['pricing-toolkit', 'estimate-template'];
$EVENTS = ['view', 'click', 'download'];
$dir = dirname(__DIR__, 2) . '/data';
$file = $dir . '/demand.json';
if (!is_dir($dir)) { @mkdir($dir, 0755, true); }

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    echo is_file($file) ? file_get_contents($file) : '{}';
    exit;
}
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); exit; }
$in = json_decode(file_get_contents('php://input', false, null, 0, 200), true);
$p = is_array($in) ? ($in['p'] ?? '') : '';
$e = is_array($in) ? ($in['e'] ?? '') : '';
if (!in_array($p, $PRODUCTS, true) || !in_array($e, $EVENTS, true)) { http_response_code(400); echo '{"ok":false}'; exit; }

$day = gmdate('Y-m-d');
$fh = fopen($file, 'c+');
if (!$fh) { http_response_code(500); echo '{"ok":false}'; exit; }
flock($fh, LOCK_EX);
$raw = stream_get_contents($fh);
$data = json_decode($raw ?: '{}', true) ?: [];
$data[$p]['total'][$e] = ($data[$p]['total'][$e] ?? 0) + 1;
$data[$p]['daily'][$day][$e] = ($data[$p]['daily'][$day][$e] ?? 0) + 1;
$data['_updated'] = gmdate('c');
ftruncate($fh, 0); rewind($fh);
fwrite($fh, json_encode($data));
fflush($fh); flock($fh, LOCK_UN); fclose($fh);
echo '{"ok":true}';
