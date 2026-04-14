# A função any() em Python retorna True se pelo menos um elemento de 
# um iterável (lista, tupla, conjunto) for verdadeiro. Ela é eficiente,
#  pois interrompe a verificação assim que encontra o primeiro valor
# verdadeiro (curto-circuito), retornando
#  False apenas se todos forem falsos ou se o iterável estiver vazio. 

#any retorna tru se pelo menos 1 for verdadeiro
#verifique se há um valor negativo
valores = [50, 20, 30, 50, 60, 70, -10, 15, -15]

if any(item <=0 for item in valores):
  print('Há valores menor que iguais ou menor que zero')
else:
  print('Não há valores')
