# A função enumerate() recebe uma sequência, 
# como uma lista , tupla ou string , e retorna um objeto enumerate. 
# Com o parâmetro opcional start, você pode definir o valor inicial do contador.

nome = ['anady', 'fernando', 'soph', 'daniel', 'rodrigo']
for i, v in enumerate(nome):
  print(f'O índice é: {i + 1} e o nome é: {v}')
  
cidade = 'fortaleza'
for ic, c in enumerate(cidade, start=2): #parâmetro opcional start, você pode definir o valor inicial do contador.
  print(f'O índice é: {ic} e o nome é: {c}')