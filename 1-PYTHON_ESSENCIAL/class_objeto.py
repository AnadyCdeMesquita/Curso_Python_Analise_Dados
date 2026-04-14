class Cachorro:
  def __init__(self, nome, raca):
    self.nome = nome
    self.raca = raca
    
  def latir(self):
    print(f'O nome da cadelinha é {self.nome} e sua raça é {self.raca} e ela faz AU AU...')
    
cao_1 = Cachorro('Soph', "Yorkshire")

cao_1.latir()

cao_2 = Cachorro("Bob", "Pittbul")
cao_2.latir()