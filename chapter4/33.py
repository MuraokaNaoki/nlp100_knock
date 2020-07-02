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
noun_phrase = []
for i in range(len(result)-2):
    if (result[i]['pos'] == '名詞' and result[i+1]['surface'] == 'の' and result[i+2]['pos'] == '名詞'):
        noun_phrase.append(result[i]['surface']+result[i+1]['surface']+result[i+2]['surface'])
print (noun_phrase)