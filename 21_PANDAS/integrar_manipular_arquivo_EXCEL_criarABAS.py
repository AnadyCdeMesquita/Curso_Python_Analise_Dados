import pandas as pd

df = pd.read_excel('Vendas.xlsx')
df['Total'] = df['Quantidade'] * df['PrecoUnitario']
#print(df)

with pd.ExcelWriter('Vendas_Atualizadas.xlsx', engine='openpyxl') as writer: #criação da planilha
  df.to_excel(writer, sheet_name='Resumo Vendas', index=False) #criação da primeira aba da planilha
  df.groupby('Produto')['Vendas'].sum().to_excel(writer, sheet_name= 'Totais por Produto') #criação da segunda aba da planilha

print('Foi criado a aba resumo vendas dentro do arquivo Vendas_Atualizadas.')

#print(df.head()) #5 primeiros registros
#print(df.tail()) # 5 últimos registros