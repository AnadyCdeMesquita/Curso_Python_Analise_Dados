nomes = ["Ana", "João", "Maria", "Carlos", "Beatriz"]
idades = [25, 42, 19, 68, 33]

idade_velha = idades[0]
nome_velha = nomes[0]

idade_nova = idades[0]
nome_nova = nomes[0]

for i in range(len(idades)):
  if idades[i] > idade_velha:
    idade_velha = idades[i]
    nome_velha = nomes[i]
  if idades[i] < idade_nova:
    idade_nova = idades[i]
    nome_nova = nomes[i]
    
print(f'O  nome da mais velha é {nome_velha} e idade {idade_velha}')
print(f'O  nome da mais velha é {nome_nova} e idade {idade_nova}')