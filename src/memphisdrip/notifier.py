# src/memphisdrip/notifier.py
from __future__ import annotations
import sys
def safe_notify(msg: str | list[str]):
    """
    Print to stderr so it doesn't break shell piping. 
    Safer than print. 
    Handles strings and lists of strings.
    """
    if isinstance(msg, list):
        msg = "\n".join(msg)
    sys.stderr.write(f"\n{msg}\n")
    sys.stderr.flush()
