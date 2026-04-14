frutas = ['abacaxi', 'limão', 'banana', 'morango', 'pessego']

frutas[-1] = 'mamão'

print(frutas)

teste = 'mamão' in frutas 
print(teste)

if 'mamão' in frutas:
  print('Sim, há mamão.')
else:
  print('Não há mamão.')