pessoa = {
  'nome': 'Soph',
  'idade': 45,
  'cor': 'negra',
  'mae': 'anady',
  'profissao': 'estudante'
  }

# print(pessoa.items())
# print(pessoa.values())
# print(pessoa.keys())

#pode se passar esses valores para tuplas ou listas
print(tuple(pessoa.items()))
print(tuple(pessoa.values()))
print(tuple(pessoa.keys()))
print('#'* 15)
print(list(pessoa.items()))
print(list(pessoa.values()))
print(list(pessoa.keys()))

#UPDATE 
#DICIONÁRIOS COM DICIONÁRIOS
#DICIONÁRIOS COM LISTAS-TUPLAS - [(12,10), (15,12)] - DESDE QUE SEJAM EM PARES
#DICIONÁRIOS COM LISTAS-TUPLAS - ((15,12), (20,30)) SEMPRE EM PARES 

# novo_dict = {'idade': 50 , 'religião': 'protestante'}
#novo_dict ={idade = 50, religiao =  protestante}
# pessoa.update(novo_dict)
# print(pessoa)

# nova_lista = [('cidade', 'fortaleza'), ('país', 'brasil')]
# pessoa.update(nova_lista)
# print(pessoa)

# nova_tupla = (('raca', 'yorkshire'), ('racao', 'prime'))
# pessoa.update(nova_tupla)
# print(pessoa)

# # clear
# pessoa.clear()
# print(pessoa)