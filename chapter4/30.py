import MeCab
path = 'neko.txt.mecab'
with open(path) as f:
    text = f.read().split('\n')
result = []
for line in text:
    if line == 'EOS':
        continue
    ls = line.split('\t')
    d = {}
    tmp = ls[1].split(',')
    d = {'surface':ls[0], 'base':tmp[6], 'pos':tmp[0], 'pos1':tmp[1]}
    result.append(d)