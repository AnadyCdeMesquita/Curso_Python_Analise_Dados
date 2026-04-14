nota = float(input("Digite sua nota: "))
if nota >= 8:
  print('Aprovado com louvor.')
elif nota >= 7:
  print('Aprovado.')
elif nota >= 6:
  print('Refazer a prova.')
else:
  print('Reprovado, nota menor que 6.')
  