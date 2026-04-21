import pandas as pd

df = pd.read_csv('vendas.csv')

print(df['Produto']) # uma coluna
print(df[['Data','Produto' ]]) # duas coluna - abrre uma lista

