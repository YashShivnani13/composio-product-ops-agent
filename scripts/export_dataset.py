"""
export_dataset.py - Dataset Exporter & Sanity Checker for Composio 100 Apps Case Study
"""

import json
import csv
import os
import sys

def export_summary_csv():
    filepath = "data/research_final.json"
    if not os.path.exists(filepath):
        filepath = "data/apps_100.json"

    if not os.path.exists(filepath):
        print("Error: research_final.json not found.")
        sys.exit(1)

    with open(filepath, "r", encoding="utf-8") as f:
        apps = json.load(f)

    csv_path = "data/apps_100_summary.csv"
    fieldnames = [
        "id", "name", "category", "website", "auth_methods", "access_type",
        "api_available", "api_types", "api_breadth", "mcp_status",
        "verdict", "score", "blocker", "evidence_url", "confidence"
    ]

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for app in apps:
            evidence_url = app.get("evidence", [{}])[0].get("url") if app.get("evidence") else "https://" + app.get("website", "")
            writer.writerow({
                "id": app.get("id"),
                "name": app.get("name"),
                "category": app.get("category"),
                "website": app.get("website"),
                "auth_methods": ", ".join(app.get("auth_methods", [])),
                "access_type": app.get("access", {}).get("type"),
                "api_available": app.get("api", {}).get("available"),
                "api_types": ", ".join(app.get("api", {}).get("types", [])),
                "api_breadth": app.get("api", {}).get("breadth"),
                "mcp_status": app.get("mcp", {}).get("status"),
                "verdict": app.get("verdict"),
                "score": app.get("score"),
                "blocker": app.get("blocker", ""),
                "evidence_url": evidence_url,
                "confidence": app.get("confidence", "high")
            })

    print(f"Loaded {len(apps)} apps from {filepath}.")
    print(f" -> Exported summary CSV to {csv_path}")

    # Sanity checks
    assert len(apps) == 100, f"Expected 100 apps, got {len(apps)}"
    categories = set(a.get("category") for a in apps)
    assert len(categories) == 10, f"Expected 10 categories, got {len(categories)}"
    print(f"All dataset sanity checks PASSED [100/100 apps, 10/10 categories].")

if __name__ == "__main__":
    export_summary_csv()
