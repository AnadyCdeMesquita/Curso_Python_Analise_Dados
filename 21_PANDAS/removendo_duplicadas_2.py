import pandas as pd

data = {
    'Nome': ['Alice', 'Bob', 'Alice', 'David'],
    'Idade': [25, 30, 25, 40],
    'Cidade': ['NY', 'LA', 'NY', 'Chicago']
}
df = pd.DataFrame(data)

# 1. Remover duplicatas exatas em todas as colunas
df_limpo = df.drop_duplicates()

# 2. Remover duplicatas baseadas em colunas específicas
df_nomes_unicos = df.drop_duplicates(subset=['Nome'])
#rint(df_nomes_unicos)

# 3. Manter a última ocorrência em vez da primeira
df_ultimo = df.drop_duplicates(subset=['Nome'], keep='last')
print(df_ultimo)

# 4. Modificar o DataFrame original (inplace)
df.drop_duplicates(inplace=True)
print(df)