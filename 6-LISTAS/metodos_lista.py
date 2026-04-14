# A principal diferença é que sort() modifica a lista original "no local" 
# (in-place) e retorna None, sendo exclusivo para listas.
# Já sorted() é uma função embutida que aceita qualquer iterável,
# cria uma nova lista ordenada e preserva a original.
# sort() é mais eficiente em memória para listas grandes. 

# Principais Diferenças
# Comportamento:
# lista.sort(): Altera a lista existente. Não cria cópia.
# sorted(iterável): Cria e retorna uma nova lista. A original não muda.
# Retorno:
# sort(): Retorna None.
# sorted(): Retorna a nova lista ordenada.
# Compatibilidade:
# sort(): Apenas para listas (list.sort()).
# sorted(): Funciona com qualquer iterável (listas, tuplas, dicionários, sets).
# Performance:
# sort(): Mais rápido e eficiente para listas, pois não gera cópia.
# sorted(): Usa um pouco mais de memória ao criar a nova lista. 

frutas = ['maca', 'mamao', 'abacaxi', 'kwui', 'pitanga']
numeros = [10, 20, 30, 450, 50, 48]

frutas.sort() # ordem alfabética
numeros.sort(reverse= True) # de trás para frente
print(frutas)
print(numeros)
frutas.reverse()
print(frutas)