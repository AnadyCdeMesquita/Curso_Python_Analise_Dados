#somente tuplas podem ser índice de dicionários e não listas

coordenadas = {(0, 1):"Posição A",(2,3):'Posição B'}

print(coordenadas[(0,1)])
print(coordenadas[(2,3)])

coordenadas1 = {(0, 1):"Posição A",(0,1,):'Posição B'}
#quando repetimos a mesma chave, ela sobrepõe a primeira chave e 
#aparece valor da segunda
print(coordenadas1)
print(coordenadas1[(0,1)])
