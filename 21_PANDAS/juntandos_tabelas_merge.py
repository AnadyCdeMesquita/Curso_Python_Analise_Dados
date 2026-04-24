import pandas as pd

dados = {
    'Produto': ['Caneta', 'Caderno', 'Borracha', None, 'Lápis', 'Caneta'],
    'Quantidade': [10, 5, 20, 15, None, 10],
    'Preço_Unitário': [2.5, 12.0, 1.5, 1.0, 1.2, 2.5],
    'Vendedor': ['João', 'Maria', 'Pedro', 'Ana', 'Ana', 'João']
}

dados2 = {
    'Produto': ['Caneta', 'Caderno', 'Borracha', 'Lápis'],
    'Desconto': [0.1, 0.05, 0, 0.2],  # percentual de desconto
    'Regiao': ['Sul', 'Norte', 'Leste', 'Oeste']
}

df = pd.DataFrame(dados)
df2 = pd.DataFrame(dados2)

df_completo = pd.merge(df,df2, on='Produto', how ='left')
print(df_completo)