import pandas as pd

df = pd.read_table('popular-names.txt', sep='\t', names=['name', 'sex', 'number', 'year'])

def extract(N):
    return df.head(N)

num = input("数字を入力してください:")
print(extract(int(num)))
