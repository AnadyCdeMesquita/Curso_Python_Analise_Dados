peso = []


for i in range(5):
  kg = int(input('Qual o peso da {i}ª pessoa? '))
  peso.append(kg)
  maior_peso = peso[0]
  menor_peso = peso[0]
  if kg > maior_peso:
    maior_peso = kg
  if kg < menor_peso: 
    menor_peso = kg

print(f'O maior peso é {maior_peso}.')
print(f'O menor peso é {menor_peso}.')