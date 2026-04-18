
#quando digita no modelo brasileiro  tipo 1.500,82
# valor = input('Digite o valor').replace('.','').replace('.',',')
# print(valor)

#quando digita modelo americano, valor abaixo
valor1 = 1500.10
novo_valor = f'{valor1:_.2f}'.replace('.',',').replace('_','.')
print(novo_valor)