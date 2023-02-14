import json
import gzip

with gzip.open("train.json.gz", mode="rt") as f:
    data = [json.loads(line) for line in f]
