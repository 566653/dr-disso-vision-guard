"""Explainable, local-only risk scoring on authorized JSON inputs."""
import argparse
import json
from pathlib import Path
MAX_BYTES=1_000_000
def assess(data, rules):
    if not isinstance(data,dict): raise ValueError("input must be a JSON object")
    alerts=[]
    for rule in rules:
        field=rule["field"]
        if field not in data: continue
        value=data[field]
        threshold=rule["value"]
        op=rule["op"]
        if op=="eq": match=type(value) is type(threshold) and value==threshold
        elif op in ("gt","lt"):
            match=type(value) in (float,int) and type(threshold) in (float,int) and (value>threshold if op=="gt" else value<threshold)
        else: raise ValueError("invalid rule operator")
        if match: alerts.append({"field":field,"severity":rule["severity"],"reason":rule["message"]})
    return {"schema_version":1,"alerts":alerts,"count":len(alerts)}
def read(path):
    p=Path(path)
    if p.stat().st_size>MAX_BYTES: raise ValueError("file too large")
    return json.loads(p.read_text(encoding="utf-8-sig"))
def main():
    parser=argparse.ArgumentParser(description="DR Disso authorized offline risk analysis")
    parser.add_argument("input",nargs="?",default="data/sample.json")
    parser.add_argument("--rules",default="rules.json")
    parser.add_argument("--output")
    args=parser.parse_args()
    result=assess(read(args.input),read(args.rules))
    text=json.dumps(result,indent=2)+"\n"
    if args.output: Path(args.output).write_text(text,encoding="utf-8")
    else: print(text,end="")
if __name__=="__main__":main()
