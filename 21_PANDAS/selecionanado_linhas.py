import pandas as pd

df = pd.read_csv('vendas.csv')
df.index = ['a', 'b', 'c', 'd']

print(df.loc['a']) #vc pode criar index para as linhas, indexando como acima
#ou pode apenas digitar o numero da linha
print(df.iloc[1])# o iloc aceita somente o index em numero