frutas = ['abacaxi', 'banana', 'maçã']

for fruta in frutas:
  print(fruta)

for i in range(len(frutas)):
  print(f'índice {i}:{frutas[i]}')


for ii, v in enumerate(frutas):
  print(f'O índice {ii} e a fruta é {frutas[ii]}')