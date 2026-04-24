import pandas as pd

df = pd.read_csv('vendas.csv')
print(df)

print(f'A quantidade somada é {df['Quantidade'].sum()}')
print(f'A Média de Preço Unitário é {df['Quantidade'].mean()}')
print(f'O valor máximo é {df['Quantidade'].max()}')
print(f'O valor mínimo é {df['Quantidade'].min()}')
print(f'A quantidade somada é {df['Quantidade'].sum()}')
print(f'Números de venda por Vendedor {df['Vendedor'].value_counts()}')