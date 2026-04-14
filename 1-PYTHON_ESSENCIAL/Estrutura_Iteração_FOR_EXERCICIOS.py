#exercício 1
# soma = 0
# for n in range(15):
#    soma += n
#    print(soma)
  
# numeros = [1, 2, 3, 4, 5]
# soma1 = 0
# for n in numeros:
#     soma1 += n
#     print(soma1)
 
# #exercicio 2
# vendas = [100, 200, 150, 300, 250]

# total = 10
# for v in vendas:
#   total += v
#   print(total)
  
# # 100 +10 = 110
# # 110 + 200 = 310
# # 310 + 150 = 460

# #exercicio 3

# nome = "Soph Carvalho Figueredo"

# for letra in nome:
#   print(letra)

#EXERCICIO 4
# Imprimir apenas múltiplos de 3
# Contar quantos números pares existem entre 1 e 100

# for numeros in range(100):
#   if numeros % 3 == 0:
#     print(numeros)

# count = 0
# for numeros in range(1, 101):
#   if numeros % 2 == 0:
#     count += 1
#     print(count)

#EXERCICIO 5

# Contar quantas vogais existem em uma palavra
# Mostrar apenas consoantes

# count = 0
# nome = 'PYTHON'
# for letra in nome:
#     count += len(letra)
#     print(count)
    
# animal = "cachorro"
# vogal = 'aeiouAEIOU'

# cont = 0
# for l in animal:
#   if l in vogal:
#     cont += 1
#     print(cont)

#EXERCICIO 6

# Exercícios:
# Calcular média
# Encontrar o maior valor da lista
numeros = [10, 20, 30, 40]
#media = sum(notas) / len(notas)
# soma = 0
# maior = numeros[0]
# menor = numeros[0]
# for n in numeros:
#   soma += n
#   print(soma)
#   if n > maior:
#     maior = n
#   if n < menor:
#     menor = n 
  
# media = soma / len(numeros)
# print(media)
# print(maior)
# print(menor)

#EXERCICIO 7

frutas = ["maçã", "banana", "uva"]

for i, fruta in enumerate(frutas):
    if fruta == "uva":
      print(i)

# Mostrar posição + valor
# Encontrar o índice de um item específico

#EXERCICIO 8
# Mostrar apenas os valores
# Filtrar dados (ex: idade maior que 18)
dados = {"nome": "Ana", "idade": 25}

for c, v in dados.items():
    print(f'{c} : {v}')



  