"""Strict policy validation and risk summaries for offline detection."""
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

SEVERITIES = {"low", "medium", "high", "critical"}
OPS = {"eq", "gt", "lt"}
MAX_RULES = 100

def validate_rules(rules):
    if not isinstance(rules, list) or len(rules) > MAX_RULES:
        raise ValueError("rules must be a list of at most 100 items")
    for rule in rules:
        if not isinstance(rule, dict) or not isinstance(rule.get("field"), str):
            raise ValueError("invalid rule field")
        if rule.get("op") not in OPS or rule.get("severity") not in SEVERITIES:
            raise ValueError("invalid operator or severity")
        if not isinstance(rule.get("message"), str) or "value" not in rule:
            raise ValueError("missing rule message or value")
        if rule["op"] in ("gt", "lt") and type(rule["value"]) not in (int, float):
            raise ValueError("numeric rule requires numeric threshold")
    return rules

def summarize(result):
    if not isinstance(result, dict) or not isinstance(result.get("alerts"), list):
        raise ValueError("invalid result")
    counts = Counter(item.get("severity", "unknown") for item in result["alerts"])
    return {"total": len(result["alerts"]), "by_severity": dict(sorted(counts.items())),
            "requires_review": bool(counts.get("high", 0) or counts.get("critical", 0))}

def export_report(result, destination):
    report = {"schema_version": 2, "generated_at_utc": datetime.now(timezone.utc).isoformat(),
              "result": result, "summary": summarize(result)}
    path = Path(destination)
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    return report
