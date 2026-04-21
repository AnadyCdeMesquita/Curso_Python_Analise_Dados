import pandas as pd

df = pd.read_csv('vendas.csv', index_col= 'Data')

print(df.loc['2025-01-03'])

#------------------

df = df.reset_index(drop = True)
print(df)