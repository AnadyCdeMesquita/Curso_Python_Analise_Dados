import pandas as pd

dados = {
    'Produto': ['Caneta', 'Caderno', 'Borracha', None, 'Lápis', 'Caneta'],
    'Quantidade': [10, 5, 20, 15, None, 10],
    'Preço_Unitário': [2.5, 12.0, 1.5, 1.0, 1.2, 2.5],
    'Vendedor': ['João', 'Maria', 'Pedro', 'Ana', 'Ana', 'João']
}

df = pd.DataFrame(dados)
print(df)
df = df.rename(columns={'Quantidade': 'Qtde'})
print(df)