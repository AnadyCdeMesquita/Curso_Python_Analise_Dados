import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
tqdm.pandas()

df = pd.read_csv('vendas_loja.csv')
df['Total'] = df['Quantidade'] * df['Valor Unitário']
#print(df)

#TOTAL GERAL VENDAS
df['Total'].sum()
#print(f'A soma total é {soma:.2f}')
#VENDEDOR
vendedores = df.groupby('Vendedor')['Total'].sum()
print(vendedores)

#PRODUTO
produto =df.groupby('Produto')['Total'].sum()
print(produto)
#FORMA DE PAGAMENTO

pagamento = df.groupby('Forma de Pagamento')['Total'].sum()
print(pagamento)

with pd.ExcelWriter("Analise_Vendas.xlsx") as writer:
    df.to_excel(writer, sheet_name="Total", index=False)
    df.to_excel(writer, sheet_name="vendedores", index=False)
    df.to_excel(writer, sheet_name="produto", index=False)
    df.to_excel(writer, sheet_name="pagamento", index=False)

df.plot(
   x= 'Produto',
   y = 'Total',
   kind='bar',
   color = 'skyblue',
   title= False
  )

plt.xlabel('Produto')
plt.ylabel('Total')
plt.tight_layout()
plt.show()
