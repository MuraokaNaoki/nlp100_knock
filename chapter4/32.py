path = 'neko.txt.mecab'
with open(path) as f:
    text = f.read().split('\n')
result = []
for line in text[:-1]:
    if line == 'EOS':
        continue
    ls = line.split('\t')
    d = {}
    tmp = ls[1].split(',')
    d = {'surface':ls[0], 'base':tmp[6], 'pos':tmp[0], 'pos1':tmp[1]}
    result.append(d)
[d['base'] for d in result if d['pos'] == '動詞' ]