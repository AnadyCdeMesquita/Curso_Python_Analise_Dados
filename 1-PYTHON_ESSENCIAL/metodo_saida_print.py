
#SEPARADOR DE STRINGS
print('Anady', 'Carvalho', 'de', 'Mesquita', sep = ' / ') 

#PULANDO LINHA
print("Anady\nCarvalho") # SEPARADO \N

# PUXA ALINHA DE BAIXO PARA CIMA, UTILIZANDO O END
print('Anady', end="...")
print('Carvalho')

print('Anady', end=" ")
print('Carvalho')

#TRANSFORMAR EM ARQUIVO

print('ANADY CARVALHO DE MESQUITA', file= open("teste.txt", "w") )


