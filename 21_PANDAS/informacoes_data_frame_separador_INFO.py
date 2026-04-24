import pandas as pd

df = pd.read_csv('vendas.csv', sep=';') # caso o arquivo CSV esteja separado por (;)

print(df.info())