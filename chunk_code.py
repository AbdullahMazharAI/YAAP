import json
import os

with open('d:/yaap1/YAAP/project_dump.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

py_lines = []
for d in data:
    if d['path'].endswith('.py') and 'site-packages' not in d['path'] and 'migrations' not in d['path'] and '__pycache__' not in d['path']:
        py_lines.append(f'# ===== {d["path"]} =====')
        py_lines.extend(d['content'].splitlines())

kt_lines = []
for d in data:
    if d['path'].endswith('.kt'):
        kt_lines.append(f'// ===== {d["path"]} =====')
        kt_lines.extend(d['content'].splitlines())

sql_lines = []
for d in data:
    if d['path'].endswith('.sql') or d['path'].endswith('.yaml') or d['path'].endswith('.yml'):
        sql_lines.append(f'-- ===== {d["path"]} =====')
        sql_lines.extend(d['content'].splitlines())

def write_chunks(lines, prefix):
    chunk_size = 800
    for i in range(0, len(lines), chunk_size):
        chunk = lines[i:i+chunk_size]
        with open(f'd:/yaap1/YAAP/{prefix}_chunk_{i//chunk_size}.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(chunk))
    print(f"Wrote {len(lines) // chunk_size + 1} chunks for {prefix}")

write_chunks(py_lines, 'py')
write_chunks(kt_lines, 'kt')
write_chunks(sql_lines, 'sql')
