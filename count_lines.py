import json

with open('d:/yaap1/YAAP/project_dump.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for d in data:
    print(f"{d['path']} - {len(d['content'].splitlines())} lines")
