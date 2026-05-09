# bootstrap.py — First-run setup: extract bundled skills to external folder

import os
import sys
import shutil
from config import BASE_DIR

SKILLS_DIR = os.path.join(BASE_DIR, "skills")


def _bundled_skills_dir():
    """Get path to skills bundled inside .exe (PyInstaller _MEIPASS)."""
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, "skills")
    return None


def setup():
    """Sync bundled skills to external folder: add new, update existing, remove obsolete."""
    bundled = _bundled_skills_dir()

    if not bundled or not os.path.isdir(bundled):
        os.makedirs(SKILLS_DIR, exist_ok=True)
        return

    os.makedirs(SKILLS_DIR, exist_ok=True)

    bundled_files = set(f for f in os.listdir(bundled) if f.endswith(".py"))

    # Copy/update bundled skills
    for fname in bundled_files:
        src = os.path.join(bundled, fname)
        dst = os.path.join(SKILLS_DIR, fname)
        shutil.copy2(src, dst)

    # Remove skills that are no longer bundled (skip user-created ones with custom marker)
    for fname in os.listdir(SKILLS_DIR):
        if fname.endswith(".py") and fname not in bundled_files:
            filepath = os.path.join(SKILLS_DIR, fname)
            # Keep files with @author other than Scryptian (user-created)
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                header = f.read(512)
            if "@author: Scryptian" in header:
                os.remove(filepath)
