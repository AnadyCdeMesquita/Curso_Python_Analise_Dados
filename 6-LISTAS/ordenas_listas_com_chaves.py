nomes = [('Fernando', 64), ('Soph', 5), ('Anady', 45), ('Socorreth',79)]
nomes.sort(key = lambda nome: nome[1])
print(nomes)

def ordem (nome):
  return nome[1]
nomes.sort(key = ordem)
print(nomes)