vendas = [
    ("Gabriel", 2510.95),
    ("Ana", 3200.5),
    ("Carlos", 1800.75),
    ("Gabriel", 2750.8),
    ("Fernanda", 4100.3),
    ("Lucas", 2300.45),
    ("Ana", 2950.2),
    ("Mariana", 3600.0),
    ("Pedro", 1980.7),
    ("Carlos", 2150.3),
    ("Fernanda", 3900.85),
    ("Gabriel", 3050.9),
    ("Lucas", 2600.95),
    ("Beatriz", 1700.75),
    ("Mariana", 3300.0),
    ("Ana", 3100.4),
    ("Pedro", 2200.5),
    ("João", 2800.0),
    ("Carlos", 2400.6),
    ("Beatriz", 1900.75)
]

teste = dict(vendas)
print(teste)
# totais = {}
# for nome, valor in vendas:
#   qtd, total = totais.get(nome, (0,0))
#   totais[nome] = (qtd + 1, valor + total)
# print(totais)

# for cliente, (qtde_compras, valor_total) in totais.items():
#   print(f'O {cliente} comprou em qtde {qtde_compras} produtos no valor de {valor_total:,.2f}')
