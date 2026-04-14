class Carro:
  def __init__(self, nome, marca, ano):
    self.nome = nome
    self.marca = marca
    self.ano = ano
    
  def dados(self):
    print(f'O carro é do {self.ano}, {self.marca} e o {self.nome}.')
      
carro1 = Carro('OBICE', 'GWM', 2025)
carro1.dados()
carro1.ano = 2015
carro1.dados()
print(carro1.ano)