import copy

lista = ['aanady', 'fernnado', 'nenem', 'socorro', 'laura', 'ana']

lista2 = lista.copy()
print('lista 2',lista2)
lista3 = lista[:]
print('lista 2',lista3)

#listas aninhadas

notas = [[10,7,.5, 8], [10,7,.5, 8], [10,7,.5, 8],[10,7,.5, 8]]

notas2 = copy.deepcopy(notas)
print(notas2)
