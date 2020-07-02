import pandas as pd

df = pd.read_table('popular-names.txt', sep='\t', names=['name', 'sex', 'number', 'year'])

def extract(N):
    return df.tail(N)

print(extract(4))