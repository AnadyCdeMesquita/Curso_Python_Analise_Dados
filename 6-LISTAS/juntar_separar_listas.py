# nome = ['Anady', 'Carvalho', 'de', 'Mesquita']
# nome2 = ' '.join(nome) # OU nome2 = ' '.join(nome)
# print(nome2)

texto = 'ANADY CARVALHO DE MESQUITA'
lista = texto.split()
print(lista)
print(f"{lista[-1]},{lista[0]}")

nome_completo = []
nome = input('QUAL O SEU PRIMEIRO NOME: ')
meio = input('QUAL O SEU SEGUNDO NOME: ')
sobrenome = input('QUAL O SEU TERCEIRO NOME: ')

nome_completo.append(nome)
nome_completo.append(meio)
nome_completo.append(sobrenome)
print(nome_completo)

print(f'O nome do passageiro é {nome_completo[-1]} , {nome_completo[0]}.')