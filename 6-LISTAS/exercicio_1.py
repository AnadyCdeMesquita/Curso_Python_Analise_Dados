produtos_disponiveis = (
    ("Monitor", 350),
    ("Teclado", 80),
    ("Mouse", 50),
    ("Processador", 1500),
    ("Gabinete", 250),
)
print("Digite os produtos que deseja comprar. Digite 'fim' para encerrar. \n")
compras = []
while True:
  item = input('Produto: ').strip().title()
  if item == 'Fim':
    break
  encontrado = False
  for nome, valor in enumerate(produtos_disponiveis):
    if item == nome:
      compras.append((nome, valor)) 
      print(f"O produto {nome} custa R$ {valor:.2f}")
      encontrado = True
      break
if not encontrado:
  print('Produto indisponível. Digite um outro produto')

  total = 0
  for nome, valor in compras:
    print('f-O nome do produto é {nome} e custa {valor}. ')
    total += valor
  
  print(f'O valor total a pagar é {total}')