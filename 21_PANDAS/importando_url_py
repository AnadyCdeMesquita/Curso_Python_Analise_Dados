import pandas as pd

url = "https://raw.githubusercontent.com/InstitutoMacielArtigas/pandas-datasets/refs/heads/main/vendas.csv"

df = pd.read_csv(url)

# print(df.head()) # mostra somente as 5 linhas

df['Total'] = df['Quantidade'] * df['Quantidade'] 
# print(df['Total'])

print(df.groupby('Produto')['Total'].sum())
df.to_csv('Vendas_Processadas1.csv', index = False)
df.to_csv('Vendas_Processadas2.csv')