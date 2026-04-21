import pandas as pd

dados_vendas = {
    "Data": ["2025-01-01", "2025-01-02", "2025-01-03"],
    "Produto": ["Caneta", "Caderno", "Borracha"],
    "Quantidade": [10, 5, 20],
    "Preco_Unitario": [2.5, 12.0, 1.5],
    "Vendedor": ["João", "Maria", "Pedro"]
}

data_frame = pd.DataFrame(dados_vendas)
print(data_frame)

print(data_frame['Data']) #imprimir uma coluna

print(data_frame[['Data','Preco_Unitario']]) #imprimir duas colunas - abre colchete-lista