# meu_dict = {'a': 1, 'b': 2, 'c': 3}
# # 1. Percorrer chave e valor (recomendado)
# for chave, valor in meu_dict.items():
#     print(f"Chave: {chave}, Valor: {valor}")

# # 2. Percorrer apenas chaves
# for chave in meu_dict.keys():
#     print(chave)

# # 3. Percorrer apenas valores
# for valor in meu_dict.values():
#     print(valor)




dados = {
  'nome': 'Ana Soph',
  'idade': 50,
  'profissão': 'desempregada',
  'filiação':'Anady Carvalho'
  }

# for v in dados:
#   print(f'os índices são: {v}')
#   print(f'os valores são: {dados[v]}')

for i, v in dados.items():
  print(i, v)

# lista = list(dados.items())
# print(lista)