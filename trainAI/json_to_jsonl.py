import json

JSON_file = json.load(open('youtubewp.json', encoding="utf8"))

with open('youtubewp.jsonl', 'wb') as outfile:
    for entry in JSON_file:
        outfile.write(json.dumps(entry, ensure_ascii=False).encode('utf-8'))
        outfile.write('\n'.encode('utf-8'))