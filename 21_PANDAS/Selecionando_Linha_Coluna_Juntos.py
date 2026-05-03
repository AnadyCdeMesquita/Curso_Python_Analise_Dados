
import pandas as pd

df = pd.read_csv('vendas.csv')
print(df[0:2])
print(df[['Data', 'Produto'][0:3]])
print(df.loc[[1,3],['Quantidade', 'Preco_Unitario']])#usando o loc pega os indices que quiser e determina as colunas
print(df.iloc[[1,3],[2,3]]) # iloc trabalha apenas com índices e numero das colunas
