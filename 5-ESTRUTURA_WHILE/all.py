# A função embutida all() em Python verifica se todos os
# elementos de um iterável (lista, tupla, conjunto) são verdadeiros. 
# Ela retorna True se todos os itens forem verdadeiros ou se o 
# iterável estiver vazio, e False caso contrário. Implementa
# avaliação de curto-circuito, 
# parando ao encontrar o primeiro False. 

valores = [50, 20, 30, 50, 60, 70, -10, 15, -15]

if all(item >= 0 for item in valores):
  print('Todos são postivios')
else:
  print('Há valores negativos tmb.')