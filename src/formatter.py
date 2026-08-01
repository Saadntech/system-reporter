"""Transfer the data to a specific format JSON."""

import json 
from pathlib import Path


def save_report(data, output_dir="reports"):
    Path(output_dir).mkdir(exist_ok=True)
    timestamps=data["timestamp"].replace(":", "-")  # Replace colons in timestamp to avoid issues in file names
    file_path = Path(output_dir) / f"system_report_{timestamps}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return file_path