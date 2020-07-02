import pandas as pd

df = pd.read_table('popular-names.txt', sep='\t', names=['name', 'sex', 'number', 'year'])

df.sort_values(by = 'number', ascending = False, inplace = True)

print(df.head())
