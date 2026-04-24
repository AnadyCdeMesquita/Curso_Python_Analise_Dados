import pandas as pd

df = pd.read_csv('vendas.csv')

# selecao = df[df['Produto'] =='Caneta']
# print(selecao)

# qtde = df[df['Quantidade']> 10]
# print(qtde)

# testando = df[(df['Produto'] == 'Borracha') & (df['Quantidade'] == 20)]
# print(testando)

testando2 = df[(df['Produto'] == 'Borracha') | (df['Quantidade'] == 50)]
print(testando2)