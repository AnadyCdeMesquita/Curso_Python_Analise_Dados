# Enunciado desafio prático - Analisando níveis de CO₂ nos estados
# Você recebeu um dicionário contendo medições de níveis de CO₂ 
# (em ppm) registradas em diferentes estados do Brasil.
# A tarefa é analisar os dados e apresentar um relatório no terminal,
# indicando se cada estado está com níveis dentro do limite aceitável 
# ou se apresenta níveis preocupantes.

# O que você deve fazer:
# Calcular a média dos valores de CO₂ para cada estado.

# Arredondar o valor da média para facilitar a leitura.

# Comparar a média com o limite seguro de 450 ppm.

# Se a média for maior que o limite, exiba uma mensagem
#   de alerta indicando que os níveis estão altíssimos e 
# que é necessário acionar uma equipe especializada.

# Caso contrário, exiba uma mensagem informando 
# que o estado está com níveis dentro do aceitável.

# Utilize cores para diferenciar as mensagens no terminal:

# Vermelho para níveis acima do limite.

# Verde para níveis dentro do limite.

# Recursos
# O código base com os dados iniciais
#  (dicionário com os estados e medições)
# já está disponível nos recursos desta aula.
#  Baixe-o e utilize como ponto
# de partida para a sua solução.

# IMPORTANTE
# Tente resolver este desafio sozinho, aplicando
#  os conhecimentos adquiridos até aqui no curso.
# Não se preocupe caso não consiga finalizar: 
# na próxima aula, será apresentada uma possível solução comentada e explicada.


niveis_co2 = {
    'AC': [385, 493, 349, 389, 449],
    'AL': [509, 453, 326],
    'AP': [361, 470, 331, 401, 513, 439],
    'AM': [344, 353, 431, 478, 313],
    'BA': [378, 300, 451, 471, 533, 441],
    'CE': [337, 435, 336, 415],
    'ES': [464, 332, 392, 507],
    'GO': [307, 536, 472, 421, 505, 434],
    'MA': [468, 307, 395],
    'MT': [452, 514, 374],
    'MS': [434, 402, 364, 459],
    'MG': [395, 473, 453, 470, 303, 322],
    'PA': [531, 509, 375, 402],
    'PB': [348, 518, 376, 522, 537, 385],
    'PR': [544, 390, 409, 414],
    'PE': [407, 368, 420],
    'PI': [306, 413, 417, 341, 462],
    'RJ': [484, 521, 514, 339],
    'RN': [509, 335, 536, 348],
    'RS': [430, 547, 328, 343, 389],
    'RO': [530, 535, 372, 543, 443],
    'RR': [388, 311, 447, 538],
    'SC': [428, 373, 492, 370, 340],
    'SP': [319, 314, 309, 312, 517, 529],
    'SE': [420, 345, 411],
    'TO': [544, 381, 429, 441],
    'DF': [409, 352, 419, 464, 488],
}

limite = 450

for i, v in niveis_co2.items():
  media = sum(v)/ len(v)
  if media > limite:
    print(f'\033[1;31m Os níveis estão altíssimos e que é necessário acionar uma equipe especializada, {round(media)}.\033[0m')
  else:
    print(f'\033[1;32m{round(media)} - ok.\033[0m')  
