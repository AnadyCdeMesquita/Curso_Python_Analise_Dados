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

lista = list(dados.items())
print(lista)