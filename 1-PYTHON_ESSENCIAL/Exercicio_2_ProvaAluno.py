import random as r

numero_sorteado = (r.randint(1, 10))

tentativa = 0
while True:     
  try:
    sorte = int(input("Tente adivinhar o número secreto: "))
    numero_sorteado = (r.randint(1, 10))
    tentativa += 1
    if sorte == numero_sorteado:
      print(f'Parabéns, vc tentou {tentativa} vezes')
      break
    else:
      print("Vc erro, tente novamente")
  except:
    print('Só aceita números, de 1 a 10')
      

print(sorte) 
