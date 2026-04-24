import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('vendas.csv')
print(df)

df.plot(
   y = 'Quantidade',
   labels = df['Produto'],
   kind = 'pie',
   autopct = '%1.1f%%',
   title= 'Participação Vendas por Produto',
   legend= False
  )

plt.ylabel('')
plt.tight_layout()
plt.show()