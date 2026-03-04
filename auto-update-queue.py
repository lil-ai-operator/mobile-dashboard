#!/usr/bin/env python3
"""Auto-update mission-control-data.json readQueue from docs folder."""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/Users/aioperator/.openclaw/workspace/projects/mobile-dashboard")
DATA_FILE = ROOT / "mission-control-data.json"
DOCS_DIR = ROOT / "docs"

# File categories mapping
CATEGORY_MAP = {
    "BRAND_": "🎨 Brand",
    "PORTAL": "🎨 Brand",
    "TODAY_": "🔥 Today",
    "wayne-action": "🔥 Today",
    "CURRENT_": "🔥 Today",
    "MASTER_": "🧭 Control Docs",
    "PROJECTS_": "🧭 Control Docs",
    "PLAIN_": "🧭 Control Docs",
    "MEMORY": "🧠 Memory",
    "SESSION_": "🧠 Memory",
}


def get_category(filename: str) -> str:
    """Determine category from filename."""
    for prefix, cat in CATEGORY_MAP.items():
        if prefix in filename.upper():
            return cat
    return "📚 Docs"


def scan_docs():
    """Scan docs folder and build file list."""
    files = []
    if not DOCS_DIR.exists():
        return files
    
    for f in DOCS_DIR.iterdir():
        if f.is_file() and not f.name.startswith('.'):
            stat = f.stat()
            files.append({
                "id": f.stem.lower().replace("_", "-"),
                "title": f.name,
                "group": get_category(f.name),
                "project": "AutoBookr" if "PORTAL" in f.name or "BRAND" in f.name else "Mission Control",
                "note": f"Auto-tracked from docs folder",
                "priority": "normal",
                "path": f"docs/{f.name}",
                "url": f"https://raw.githack.com/lil-ai-operator/mobile-dashboard/main/docs/{f.name}",
                "updatedAt": datetime.fromtimestamp(stat.st_mtime, timezone.utc)
                    .replace(microsecond=0).isoformat().replace('+00:00', 'Z')
            })
    
    return files


def update_data():
    """Update mission-control-data.json with current docs."""
    if not DATA_FILE.exists():
        print("ERROR: mission-control-data.json not found")
        return False
    
    data = json.loads(DATA_FILE.read_text())
    
    # Get current readQueue
    current_queue = data.get("readQueue", [])
    existing_ids = {item["id"] for item in current_queue}
    
    # Scan docs
    new_files = scan_docs()
    
    # Add new files that aren't in queue
    added = 0
    for f in new_files:
        if f["id"] not in existing_ids:
            current_queue.append(f)
            print(f"Added: {f['title']} ({f['group']})")
            added += 1
    
    if added > 0:
        data["readQueue"] = current_queue
        data["updatedAt"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
        DATA_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
        print(f"Updated mission-control-data.json with {added} new files")
        return True
    
    print("No new files to add")
    return False


if __name__ == "__main__":
    update_data()
