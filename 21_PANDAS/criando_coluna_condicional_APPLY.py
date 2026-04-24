import pandas as pd

df = pd.read_csv('vendas.csv')
print(df)
df['Total'] = df['Quantidade'] * df['Preco_Unitario']

def valor_total(valor):
  if valor > 30:
    return 'Alto'
  else:
    return 'Baixo'
  
df['Vendas'] = df['Total'].apply(valor_total)

#df['Vendas'] = df['Total].apply(lambda valor:'Alta' if valor > 20 else 'Baixa')
print(df)