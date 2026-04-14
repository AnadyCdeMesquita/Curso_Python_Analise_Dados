# Questão 1
idades = [12, 45, 78, 23, 56, 89, 34]
maior_idade = menor_idade = idades[0]
for idade in idades:
  if idade < menor_idade:
    menor_idade = idade
    
  if idade > maior_idade:
    maior_idade = idade
    
print(f'A maior idade tem {maior_idade} e a menor idade tem {menor_idade}')