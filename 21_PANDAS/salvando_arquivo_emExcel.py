import pandas as pd

import pandas as pd

url = "https://raw.githubusercontent.com/InstitutoMacielArtigas/pandas-datasets/refs/heads/main/vendas.csv"

df = pd.read_csv(url)

df.to_excel('Vendas.xlsx', index= False) #use-se false para não salvar o index
print(df)
