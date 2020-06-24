import json
import re

filename = 'jawiki-country.json'
with open(filename,mode = 'r') as f:
    for line in f:
        line = json.loads(line)
        if line['title'] == 'イギリス':
            about_uk = line['text']
            break

pattern = r'^(\={2,})\s*(.+?)\s*(\={2,}).*$'
result = '\n'.join(i[1] + ':' + str(len(i[0]) - 1) for i in re.findall(pattern, about_uk, re.MULTILINE))
print(result)