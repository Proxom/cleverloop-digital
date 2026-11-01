"""Add the cookie-free page-view counter (/js/pv.js) to every public HTML page that lacks it. Idempotent.
Usage: python3 scripts/site/pv_tag.py public   (also run automatically by seo_tags.py)"""
import glob, os, sys

TAG = '<script src="/js/pv.js" defer></script>'


def run(root="public"):
    n = 0
    for f in glob.glob(os.path.join(root, "**/*.html"), recursive=True):
        s = open(f).read()
        if "/js/pv.js" in s or "</head>" not in s:
            continue
        open(f, "w").write(s.replace("</head>", TAG + "\n</head>", 1))
        n += 1
    return n


if __name__ == "__main__":
    print("pv tagged", run(sys.argv[1] if len(sys.argv) > 1 else "public"))
