#listas podem alterar, podem duplicar, são ordenados
outros_dados = 'brasileira'
dados_cliente= ['anady', 1236, 'feminino', 1.68, outros_dados]

print(dados_cliente)

dados_cliente[0] = "Soph"

print(dados_cliente)

dados_cliente[0] = None

print(dados_cliente)