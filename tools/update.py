"""One step after a /reload: import what the API add-ons saved, rebuild the docs, commit, and publish the website.

    python tools/update.py           # does nothing if the game hasn't saved anything new since the last run
    python tools/update.py --force   # import and publish anyway

update-docs.bat runs this. Publishing is a git push: GitHub Pages rebuilds https://zmarotrix.github.io/ForeverAPI/
from site/ (.github/workflows/pages.yml). Without a remote, the docs are still rebuilt and committed here.
"""

import glob
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from apidoc import GAME  # noqa: E402

STATE = os.path.join(ROOT, ".last-import")
LIVE = "https://zmarotrix.github.io/ForeverAPI/"


def saved_files():
    return sorted(f for f in glob.glob(os.path.join(GAME, "WTF", "Account", "*", "SavedVariables", "Api*.lua")) + glob.glob(os.path.join(GAME, "WTF", "Account", "*", "SavedVariables", "ForeverAPIProbe.lua")))


def fingerprint(files):
    return {os.path.basename(f): [int(os.path.getmtime(f)), os.path.getsize(f)] for f in files}


def run(*cmd, cwd=ROOT, quiet=False):
    r = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
    if not quiet or r.returncode:
        out = (r.stdout + r.stderr).strip()
        if out:
            print(out)
    if r.returncode:
        sys.exit("failed: " + " ".join(cmd))
    return r.stdout


def main():
    force = "--force" in sys.argv
    files = saved_files()
    if not files:
        sys.exit("No API add-on saves found. Play with the API add-ons on, then /reload or log out.")
    fp = fingerprint(files)
    last = {}
    if os.path.isfile(STATE):
        with open(STATE, encoding="utf-8") as f:
            last = json.load(f)
    newest = time.strftime("%Y-%m-%d %H:%M", time.localtime(max(v[0] for v in fp.values())))
    if fp == last and not force:
        print(f"Nothing new: the game last saved at {newest}, and that's already imported and published.")
        print("Play a while, /reload or log out, then run this again.")
        return

    print(f"Importing what the game saved at {newest}...")
    run(sys.executable, os.path.join(HERE, "apidoc.py"), "import")
    print("\nRebuilding the docs...")
    run(sys.executable, os.path.join(HERE, "apidoc.py"), "build", quiet=True)

    # git: quiet about line endings, and commit only what this produced
    run("git", "add", "-A", "docs", "luals", "site", "dumps", quiet=True)
    if run("git", "diff", "--cached", "--name-only", quiet=True).strip():
        run("git", "commit", "-q", "-m", f"Import in-game API data saved {newest}", quiet=True)
        print("Committed: " + run("git", "log", "-1", "--format=%h %s", quiet=True).strip())

    has_remote = subprocess.run(["git", "remote", "get-url", "origin"], cwd=ROOT, capture_output=True).returncode == 0
    if has_remote:
        print(chr(10) + "Publishing the website...")
        run("git", "push", "-q", "origin", "HEAD", quiet=True)
        print(f"Pushed. Live in a minute or two at {LIVE} (Ctrl+F5 if your browser shows the old one).")
    else:
        print(chr(10) + "This folder has no GitHub remote yet, so nothing was published.")

    with open(STATE, "w", encoding="utf-8") as f:
        json.dump(fp, f)


if __name__ == "__main__":
    main()
