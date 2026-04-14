# maior =  0
# menor = 0
# for p in range(1,6):
#   peso = int(input(f"Qual é o peso da {p} pessoa: "))
#   if p == 1:
#     maior = p
#     menor = p 
#   else:
#     if peso > maior:
#       peso = maior
#     if peso < menor:
#        peso = menor
      
# print(f'O maior peso: {maior}, o menor peso {menor}')

idades = [12, 45, 78, 23, 56, 89, 34]

maior_idade = idades[0]
menor_idade = idades[0]

for idade in idades:
    if idade > maior_idade:
      maior_idade = idade 
    if idade < menor_idade:
      menor_idade = idade

print(f"Mais velha: {maior_idade} anos")
print(f"Mais nova: {menor_idade} anos")

