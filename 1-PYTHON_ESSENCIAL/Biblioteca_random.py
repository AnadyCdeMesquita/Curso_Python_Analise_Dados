import random
#1
# A função random.randint() retorna um número inteiro aleatório entre um determinado intervalo. A sintaxe do comando é:
# random.randint(start, stop)
# Em que:
# start: indica o valor inicial, que faz parte dos resultados possíveis;
# stop: representa o ponto de parada, no qual o valor indicado também pode ser selecionado como retorno.
print(random.randint(1, 10))

#2
# Gerando um número decimal aleatório entre um intervalo: randrange()
# O método random.randrange() retorna um número aleatório existente entre um determinado intervalo. A sintaxe do comando é:
# random.randrange(start, stop, step)
# Em que:
# start: indica o valor inicial, que pode ser incluído no resultado aleatório;
# stop: indica o ponto de parada e o valor não faz parte do resultado;
# step: representa um valor inteiro que será somado ao valor inicial para determinar o resultado. Se nenhum número for indicado, o valor correspondente será 1.
# Veja um exemplo:

# Perceba que os valores gerados correspondem a um múltiplo de 5, que é 
# o número definido no parâmetro step. Além disso, os resultados são 
# diferentes a cada vez que o comando é executado.
print(random.randrange(10, 100, 5))
#resultado: 60

#3-Gerando um elemento aleatório a partir de uma sequência: choice()
# A função Python random choice retorna um elemento aleatório que pertença a uma sequência, que pode ser uma variável do tipo string, uma lista, uma tupla ou uma sequência numérica. Veja alguns exemplos com diferentes tipos de variáveis:

# lista_nomes=['Maria', 'João', 'Pedro', 'Cláudia']
# print(random.choice(lista_nomes))
# #resultado: Maria

# nome = 'Ivani'
# print(random.choice(nome))
# #resultado: v

# tupla_nomes=('Maria', 'João', 'Pedro', 'Cláudia')
# print(random.choice(tupla_nomes))
# #resultado: Cláudia

# lista_dicionario_nomes= [{"nome": "Maria", "idade": 20}, {"nome": "Cláudia", "idade": 20}]
# print(random.choice(lista_dicionario_nomes))
# #resultado: {'nome': 'Maria', 'idade': 20}

# print(random.choice(range(2,20)))
# #resultado: 16
lista = ['anady', 'soph', 'fernando', 'socorreth']
print(random.choice(lista))

nome = 'anady'
print(random.choice(nome))

#4-Gerando uma lista aleatória a partir de uma sequência: choices()
# A função random.choices() permite o retorno de uma quantidade determinada de elementos. Também podemos definir a probabilidade para a repetição de cada elemento da sequência que servirá de base para a produção do resultado aleatório. A sintaxe do comando é:
# random.choices(sequence, weights=None, cum_weights=None, k=1)
# No qual:
# sequence: é obrigatório e representa a sequência original de elementos, que pode ser uma lista, uma tupla ou um conjunto de números;
# weights: é opcional e indica a probabilidade relativa de repetição para cada elemento;
# cum_weights: é opcional e indica a probabilidade acumulada de repetição de cada elemento;
#k: é opcional e indica o número de elementos retornado pela função, sendo o valor padrão igual a 1.

lista_nomes=['Maria', 'João', 'Pedro', 'Cláudia']
print(random.choices(lista_nomes,weights=[2, 5, 1, 8], k=10))
#resultado: ['Maria', 'Pedro', 'João', 'João', 'Cláudia', 'Cláudia', 'Cláudia', 'João', 'João', 'Cláudia']

print(random.choices(lista_nomes,cum_weights=[2, 5, 1, 8], k=10))
#resultado: ['Cláudia', 'Cláudia', 'Cláudia', 'Cláudia', 'Cláudia', 'Maria', 'João', 'Cláudia', 'João', 'Cláudia']

#5-Retorna um número decimal entre 0 e 1: random() 
# A função random() retorna um número decimal aleatório entre 0 e 1.
# Veja um exemplo:
# print(random.random())
#resultado: 0.41597137457321787

print(random.random())
#6 random.uniform()
# Gerando um número decimal aleatório entre um intervalo: uniform()
# A função random.uniform() retorna um número decimal aleatório de 
# acordo com os valores iniciais e finais definidos na função. 
# Veja a sintaxe:

random.uniform(5, 10)
print(random.uniform(5, 10))

# shuffle
lista1 = ['maca', 'soph', 'banana', 'laranja']
random.shuffle(lista1)
print(lista1)