import pandas as pd

df = pd.read_csv('vendas.csv')

df.loc[df['Produto'] == 'Caneta', 'Preco_Unitario'] = 3.0
print(df)