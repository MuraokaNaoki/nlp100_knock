import json 
import re

filename = 'jawiki-country.json'
with open(filename,mode = 'r') as f:
    for line in f:
        line = json.loads(line)
        if line['title'] == 'イギリス':
            about_uk = line['text']
            break

pattern = r'^(.*\[\[Category:.*\]\].*)$'
result = '\n'.join(re.findall(pattern, about_uk, re.MULTILINE))

print(result)
