import pandas as pd

df = pd.read_table('popular-names.txt', header=None, sep='\t', names=['name', 'sex', 'number', 'year'])

col1 = df['name']
col1.to_csv('./col1.txt', header = None, index = False)

col2 = df['sex']
col2.to_csv('./col2.txt', header = None, index = False)