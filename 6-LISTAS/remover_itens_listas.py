frutas = ['morango', 'banana', 'sapoti', 'banana']

#frutas.remove('banana') #remove só a primeira
#print(frutas)

# frutas.pop() # remove o último, ou vc determina e vc pode criar uma variável para dizer o item removido
# valor= frutas.pop(0)
# print(valor)
# print(frutas)

del frutas [2] #precisa usar com índice, sem o índice apaga a variável
print(frutas)

#SE USAR DEL FRUTAS -> APAGA A VARIÁVEL DEL

frutas.clear() # imprime []
# O método clear() em Python é utilizado para remover todos os 
# elementos de um objeto (lista, dicionário ou conjunto), tornando-o 
# vazio sem deletar a variável.
print(frutas)


