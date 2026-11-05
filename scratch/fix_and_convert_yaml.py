import yaml
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

yaml_path = r"c:\Users\Lenovo\Downloads\mocha-topia-main\mocha-topia\openapi.yaml"
json_path = r"c:\Users\Lenovo\Downloads\mocha-topia-main\mocha-topia\openapi.json"
downloads_yaml_path = r"c:\Users\Lenovo\Downloads\openapi.yaml"
downloads_json_path = r"c:\Users\Lenovo\Downloads\openapi.json"

with open(yaml_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if "example: Total: Rp 40.000" in line:
        line = line.replace("example: Total: Rp 40.000", 'example: "Total: Rp 40.000"')
    elif "example: 10/22/2026, 9:30:15 AM" in line:
        line = line.replace("example: 10/22/2026, 9:30:15 AM", 'example: "10/22/2026, 9:30:15 AM"')
    new_lines.append(line)

fixed_content = "".join(new_lines)
with open(yaml_path, "w", encoding="utf-8") as f:
    f.write(fixed_content)

with open(downloads_yaml_path, "w", encoding="utf-8") as f:
    f.write(fixed_content)

# Test YAML parsing
data = yaml.safe_load(fixed_content)
print(f"YAML successfully parsed! API Title: {data['info']['title']}, Endpoints count: {len(data['paths'])}")

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

with open(downloads_json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Successfully exported {json_path} and {downloads_json_path}")
