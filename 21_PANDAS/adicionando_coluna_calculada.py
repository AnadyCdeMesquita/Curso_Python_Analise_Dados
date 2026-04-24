import pandas as pd

df = pd.read_csv('vendas.csv')
df['Total'] = df['Quantidade'] * df['Preco_Unitario']
print(df)