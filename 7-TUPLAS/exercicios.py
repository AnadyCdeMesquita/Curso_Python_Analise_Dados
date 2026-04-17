# Sua tarefa será:




#  armazenando como valor a quantidade total vendida de cada produto.

# Converter os dados de vendas para lista, adicionar uma nova venda e,
#  em seguida, voltar a ser tupla.

# Exibir o número total de vendas após a atualização.

# Código de Partida
# Para facilitar, o código com os dados de vendas já 
# estará disponível nos recursos desta aula.
# Você poderá usá-lo como ponto de partida para a solução do desafio.

# Este desafio foi pensado para que você aplique, 
# de forma prática, os conceitos aprendidos neste módulo sobre tuplas em Python:

# Criação e acesso a elementos.

# Desempacotamento.

# Uso de tuplas como chave em dicionários.

# Métodos úteis como .count() e .index().

# Conversão entre lista e tupla.


vendas = (
    (101, "Notebook", 2, 3500.00),
    (102, "Mouse", 5, 80.00),
    (103, "Teclado", 3, 120.00),
    (104, "Notebook", 1, 3500.00),
    (105, "Monitor", 2, 900.00),
    (106, "Mouse", 4, 80.00),
)
## Mostrar a primeira e a última venda registrada.
primeira_venda = vendas[0]
ultima_venda = vendas[-1]
print(f'A primeira venda: {primeira_venda} e a segunda venda venda: {ultima_venda}')

# Calcular e exibir o valor total de cada venda (quantidade × preço unitário).
for cod, produto, qtde, preco in vendas:
  total = qtde * preco
  print(f'O valor do {cod} - {produto} é : {total:,.2f}')

# Contar quantas vezes o produto "Mouse" foi vendido na semana.
qtde_mouses = 0
for v in vendas:
  if v[1] == 'Mouse':
      qtde_mouses += 1
print(f'A quantidade de mouses vendidas: {qtde_mouses}')

# Criar um dicionário usando tuplas como chave, no formato (produto, preco_unitario):

vendas = (
    (101, "Notebook", 2, 3500.00),
    (102, "Mouse", 5, 80.00),
    (103, "Teclado", 3, 120.00),
    (104, "Notebook", 1, 3500.00),
    (105, "Monitor", 2, 900.00),
    (106, "Mouse", 4, 80.00),
)

lista = list(vendas)
lista.append((107, "Monitor", 4, 70.00))
print(lista)

vendas = tuple(lista)
print(vendas)
