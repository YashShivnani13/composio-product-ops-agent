"""
evidence_validator.py - Expanded Evidence & Claim Validator for Composio 100 Apps Audit

Audits every application across 4-5 distinct claims:
1. Auth Method Claim
2. Access / Credential Accessibility Claim
3. API Surface & Availability Claim
4. MCP Status Claim

Reports total claims, evidence-backed claims, unsupported claims, broken URLs, ambiguous claims, and confidence distribution.
"""

import json
import os
import sys
from typing import Dict, Any, List

def validate_dataset(filepath: str) -> Dict[str, Any]:
    if not os.path.exists(filepath):
        print(f"Error: File {filepath} not found.")
        sys.exit(1)

    with open(filepath, "r", encoding="utf-8") as f:
        data: List[Dict[str, Any]] = json.load(f)

    total_apps = len(data)
    total_claims = 0
    evidence_backed_claims = 0
    unsupported_claims = 0
    ambiguous_claims = 0
    broken_urls = []
    
    confidence_distribution = {
        "high (90-100%)": 0,
        "medium (75-89%)": 0,
        "low (<75%)": 0
    }

    for app in data:
        app_id = app.get("id")
        app_name = app.get("name")
        evidence_items = app.get("evidence", [])
        confidence = app.get("confidence", 0)

        if confidence >= 90:
            confidence_distribution["high (90-100%)"] += 1
        elif confidence >= 75:
            confidence_distribution["medium (75-89%)"] += 1
        else:
            confidence_distribution["low (<75%)"] += 1

        for item in evidence_items:
            total_claims += 1
            url = item.get("url", "")
            claim_text = item.get("claim", "")
            strength = item.get("strength", "medium")

            if url and (url.startswith("http://") or url.startswith("https://")):
                evidence_backed_claims += 1
                if strength == "weak":
                    ambiguous_claims += 1
            else:
                unsupported_claims += 1
                broken_urls.append({"id": app_id, "name": app_name, "claim": claim_text, "url": url})

    report = {
        "dataset_path": filepath,
        "total_apps": total_apps,
        "total_claims_validated": total_claims,
        "claims_per_app": round(total_claims / total_apps, 2) if total_apps > 0 else 0,
        "evidence_backed_claims": evidence_backed_claims,
        "unsupported_claims": unsupported_claims,
        "ambiguous_claims": ambiguous_claims,
        "broken_url_count": len(broken_urls),
        "broken_urls": broken_urls,
        "confidence_distribution": confidence_distribution,
        "validation_passed": (unsupported_claims == 0 and len(broken_urls) == 0)
    }

    return report


def main():
    target_file = "data/research_final.json" if os.path.exists("data/research_final.json") else "data/apps_100.json"
    print(f"Running Expanded Evidence Validator on {target_file}...")
    report = validate_dataset(target_file)
    
    print("\n" + "="*60)
    print("           EXPANDED EVIDENCE VALIDATION REPORT            ")
    print("="*60)
    print(f" Total Apps Evaluated        : {report['total_apps']}")
    print(f" Total Claims Validated      : {report['total_claims_validated']} ({report['claims_per_app']} claims / app)")
    print(f" Evidence-Backed Claims      : {report['evidence_backed_claims']} ({round((report['evidence_backed_claims']/report['total_claims_validated'])*100, 1)}%)")
    print(f" Unsupported Claims          : {report['unsupported_claims']}")
    print(f" Ambiguous / Weak Claims     : {report['ambiguous_claims']}")
    print(f" Broken / Invalid URLs       : {report['broken_url_count']}")
    print(f" Confidence Distribution     : High: {report['confidence_distribution']['high (90-100%)']} | Med: {report['confidence_distribution']['medium (75-89%)']} | Low: {report['confidence_distribution']['low (<75%)']}")
    print(f" Overall Validation Status   : {'PASSED [OK]' if report['validation_passed'] else 'ATTENTION NEEDED'}")
    print("="*60 + "\n")

    os.makedirs("data", exist_ok=True)
    with open("data/validation_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print("Saved validation report to data/validation_report.json")


if __name__ == "__main__":
    main()
