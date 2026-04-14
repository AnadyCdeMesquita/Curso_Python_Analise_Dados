lista1 = [200, 500, 1000, 800, 700]

# for p in lista1:
#   soma = p * 2
#   novo_preco.append(soma)

# print(novo_preco)

novo_preco = [p * 3 for p in lista1 if p >= 500]
print(novo_preco)

nome = ['anady', 'fernando', 'soph', 'socorreth', 'juca', 'bianca']

alunos = [n.upper() for n in nome if n == 'anady']
print(alunos)

valores = [800, 100, 1500, 2000, 5000, 700, 1100, 8000]
novo_valores = []
for v in valores:
  if v > 1000:
   novo_valores.append( v + (v * 0.50))
print(novo_valores)

preco_novo = [valor + (valor * 0.50) for valor in valores if valor > 1000]
print(preco_novo)