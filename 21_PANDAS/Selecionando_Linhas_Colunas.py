import pandas as pd

df = pd.read_csv('vendas.csv')
print(df)
print('*' * 30)
print(df.loc[2]) # selecionar linha
print('*' * 30)
print(df[1:3])# mesmo metodo utilizado pelas listas, tuplas, strings