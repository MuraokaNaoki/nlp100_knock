import pandas as pd

df = pd.read_table('popular-names.txt', sep='\t', names=['name', 'sex', 'number', 'year'])

print(len(df.drop_duplicates(subset = 'name')))