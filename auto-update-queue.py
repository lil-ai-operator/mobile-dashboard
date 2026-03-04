#!/usr/bin/env python3
"""Auto-sync: updates mission-control-data.json from docs AND tasks."""

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/Users/aioperator/.openclaw/workspace/projects/mobile-dashboard")
DATA_FILE = ROOT / "mission-control-data.json"
DOCS_DIR = ROOT / "docs"

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
    for prefix, cat in CATEGORY_MAP.items():
        if prefix in filename.upper():
            return cat
    return "📚 Docs"

def scan_docs():
    files = []
    if not DOCS_DIR.exists():
        return files
    for f in DOCS_DIR.iterdir():
        if f.is_file() and not f.name.startswith('.') and f.suffix in ['.md', '.txt']:
            stat = f.stat()
            files.append({
                "id": f.stem.lower().replace("_", "-"),
                "title": f.name,
                "group": get_category(f.name),
                "project": "AutoBookr" if "PORTAL" in f.name or "BRAND" in f.name else "Mission Control",
                "note": "Auto-tracked from docs folder",
                "priority": "normal",
                "path": f"docs/{f.name}",
                "url": f"https://raw.githack.com/lil-ai-operator/mobile-dashboard/main/docs/{f.name}",
                "updatedAt": datetime.fromtimestamp(stat.st_mtime, timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
            })
    return files

def scan_for_new_tasks():
    new_tasks = []
    if not DOCS_DIR.exists():
        return new_tasks
    task_patterns = [r'\[NEW_TASK\]\s*(.+)', r'TODO:\s*(.+)', r'TASK:\s*(.+)']
    for f in DOCS_DIR.iterdir():
        if not f.is_file() or f.suffix != '.md':
            continue
        content = f.read_text()
        project_key = None
        if 'BRAND' in f.name.upper():
            project_key = 'autobookr_suite'
        elif 'PORTAL' in f.name.upper():
            project_key = 'autobookr_suite'
        if not project_key:
            continue
        for pattern in task_patterns:
            for match in re.findall(pattern, content, re.IGNORECASE):
                task = match.strip()
                if len(task) > 10:
                    new_tasks.append({'project': project_key, 'task': task})
    return new_tasks

def update_data():
    if not DATA_FILE.exists():
        print("ERROR: mission-control-data.json not found")
        return False
    data = json.loads(DATA_FILE.read_text())
    current_queue = data.get("readQueue", [])
    existing_ids = {item["id"] for item in current_queue}
    for f in scan_docs():
        if f["id"] not in existing_ids:
            current_queue.append(f)
            print(f"Added: {f['title']}")
    for item in scan_for_new_tasks():
        for proj in data.get('projects', []):
            if proj.get('key') == item['project']:
                todo = proj.get('todo', [])
                if item['task'] not in todo and item['task'] not in proj.get('done', []):
                    todo.append(item['task'])
                    print(f"Task added to {item['project']}: {item['task']}")
                break
    data["readQueue"] = current_queue
    data["updatedAt"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    DATA_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    print("Updated!")
    return True

if __name__ == "__main__":
    update_data()
