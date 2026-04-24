import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('vendas.csv')
print(df)

df.plot(
   x= 'Produto',
   y = 'Quantidade',
   kind='bar',
   color = 'skyblue',
   title= False
  )

plt.xlabel('Produto')
plt.ylabel('Quantidade')
plt.tight_layout()
plt.show()