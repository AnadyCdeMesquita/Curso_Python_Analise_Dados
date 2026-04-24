import pandas as pd

df = pd.read_csv('vendas.csv')
print(df)

print(df.groupby('Produto')['Quantidade'].sum())
print(df.groupby('Produto')['Preco_Unitario'].mean())
print(df.groupby('Data')['Quantidade'].describe())