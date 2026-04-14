# Um laço for aninhado é uma estrutura de repetição
# onde um laço for (interno) 
# é colocado dentro de outro for (externo). 
# O laço interno executa completamente a cada iteração 
# individual do laço externo, 
# sendo ideal para percorrer matrizes, tabelas ou criar combinações,
# com a complexidade crescendo rapidamente.

# Principais Características e Funcionamento:
# Execução: O loop externo inicia, e para cada rodada dele, 
# todo o loop interno roda do início ao fim.
# Estrutura: Utiliza variáveis de controle diferentes 
# para cada nível (geralmente i para o externo e j para o interno).
# Aplicações Comuns: Tabelas de multiplicação, 
# manipulação de matrizes (linhas e colunas), e geração de pares de dados.

# for i in range(3):
#   for j in range(3):
#     for k in range(3):
#       print(i, j, k)
      
for i in range(1,3):
  for j in range(1,3):
    for k in range(1,3):
      print(i, j, k)