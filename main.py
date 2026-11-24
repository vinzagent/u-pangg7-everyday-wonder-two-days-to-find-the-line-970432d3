"""Everyday Wonder, Two Days to Find the Line.

One original sentence, at most 200 characters, that makes a small
everyday moment strange and new: a lift, a stranger humming, and one
floor where the whole building forgets what year it is.
"""

import os

LINE = (
    "The lift doors open on a stranger humming the lullaby your "
    "grandmother sang, and for one floor the whole building forgets what "
    "year it is."
)

chars = len(LINE)
if chars < 1 or chars > 200:
    raise SystemExit(f"entry line is {chars} characters, outside the 1-200 gate")
if not LINE.strip():
    raise SystemExit("entry line is blank")
if "\n" in LINE or "\r" in LINE:
    raise SystemExit("entry line must be a single line")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
# The grader collects /output as another user, so the file must be
# world-readable: a default mkstemp-style 0600 mode fails "not readable".
os.chmod(path, 0o644)
print(LINE)
print(f"({chars} characters)")
