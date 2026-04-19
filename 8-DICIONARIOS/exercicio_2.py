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

relatorio = {}

for nome, valor in vendas:
    if nome not in relatorio:
        # Inicializa o cliente: [quantidade_vendas, valor_total]
        relatorio[nome] = [1, valor]
    else:
        # Incrementa a contagem e soma o valor
        relatorio[nome][0] += 1
        relatorio[nome][1] += valor

# Exibição dos resultados
print(f"{'Cliente':<12} | {'Vendas':<8} | {'Total Gasto':<12}")
print("-" * 35)

for cliente, dados in relatorio.items():
    quantidade = dados[0]
    total = dados[1]
    print(f"{cliente:<12} | {quantidade:<8} | R$ {total:>10.2f}")