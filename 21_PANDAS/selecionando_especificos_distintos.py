import pandas as pd

df = pd.read_csv('vendas.csv')
print(df)

print(df['Produto'].unique())
print(df['Produto'].nunique())
