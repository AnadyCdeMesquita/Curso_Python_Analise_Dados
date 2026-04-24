# A função dropna() do Pandas remove linhas ou colunas 
# com valores ausentes (NaN, None, NaT) em Python. 
# A sintaxe básica é
# df.dropna(axis=0, how='any', subset=None, inplace=False). 
# Por padrão, elimina qualquer linha com pelo menos um valor nulo, 
# retornando um novo DataFrame sem modificar o original

# Exemplo de DataFrame
data = {'A': [1, 2, np.nan], 'B': [4, np.nan, np.nan], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# 1. Remover todas as linhas que contenham nulos (padrão)
df_limpo = df.dropna()

# 2. Remover colunas que contêm valores nulos (axis=1)
df_colunas = df.dropna(axis=1)

# 3. Remover apenas se TODAS as colunas na linha forem nulas
df_all = df.dropna(how='all')

# 4. Remover linhas com nulos apenas nas colunas 'A' ou 'B'
df_subset = df.dropna(subset=['A', 'B'])

# 5. Modificar o DataFrame original (inplace=True)
df.dropna(inplace=True)

import pandas as pd

dados = {
    'Produto': ['Caneta', 'Caderno', 'Borracha', None, 'Lápis', 'Caneta'],
    'Quantidade': [10, 5, 20, 15, None, 10],
    'Preço_Unitário': [2.5, 12.0, 1.5, 1.0, 1.2, 2.5],
    'Vendedor': ['João', 'Maria', 'Pedro', 'Ana', 'Ana', 'João']
}

df = pd.DataFrame(dados)
# df['Quantidade'] = df['Quantidade'].fillna(0) #substituir um valor em branco
# df['Produto'] = df['Produto'].fillna('Papel') #substituir um valor em branco
df = df.dropna(subset = ['Produto'])

print(df)