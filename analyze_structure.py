import json
import os

def analyze_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            paths = [item['path'] for item in data if 'path' in item]
            print(f"\n--- {os.path.basename(filepath)} Paths ({len(paths)} files) ---")
            for p in sorted(paths):
                # only print paths to get high level architecture
                print(p)
    except Exception as e:
        print(f"Error reading JSON {filepath}: {e}")

def analyze_tree(filepath):
    encodings = ['utf-16', 'utf-8', 'cp1252']
    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                lines = f.readlines()
                print(f"\n--- {os.path.basename(filepath)} Analysis (Encoding: {enc}) ---")
                print(f"Total lines: {len(lines)}")
                for line in lines:
                    print(line.rstrip())
            return
        except Exception as e:
            pass
    print(f"Error reading Tree {filepath} with all encodings.")

if __name__ == '__main__':
    analyze_json('d:/yaap1/YAAP/project_dump.json')
    analyze_tree('d:/yaap1/YAAP/backend_tree.txt')
