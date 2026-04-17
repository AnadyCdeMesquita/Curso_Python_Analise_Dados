# #list compheension

# teste_quadrado = {x: x**2 for x in range(5)}
# print(teste_quadrado)
custos = {'teclado': 100,
          'mouse':50,
          'monitor': 1000,
          'processador': 1500
          }

vendas = {}
# for produto in custos:
#   vendas[produto] = custos[produto] * 1.5
# print(vendas)
  

vendas1 = {produto: custos[produto] * 1.5 for produto in custos}
print(vendas1)

for produtos in custos:
  print(custos[produtos])
