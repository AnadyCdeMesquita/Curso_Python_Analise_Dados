frutas = ['ABACAXI', 'MAMAO', 'LARANJA']

frutas.append('uva')
print(frutas)
frutas.insert(1,'kiwi')

#<>DIFERENÇA ENTRE 
# A principal diferença entre usar extend() e o operador de soma (+) 
# em listas Python está na modificação do objeto original (in-place)
# versus a criação de uma nova lista. 

# extend(): Modifica a lista original adicionando elementos ao final dela. Não cria uma nova lista, 
# sendo mais eficiente em termos de memória.
# + (Soma): Cria uma nova lista que é a combinação das duas listas originais.
# As listas originais permanecem inalteradas. 

novas_frutas = ['pessego', 'ameixa']
frutas.extend(novas_frutas)
print(frutas)

frutas_frutas = frutas + novas_frutas
print(frutas_frutas)