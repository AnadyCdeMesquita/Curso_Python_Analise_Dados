import pandas as pd

df = pd.read_csv('vendas.csv')

df['Categoria'] = 'Material Escolar'
print(df)