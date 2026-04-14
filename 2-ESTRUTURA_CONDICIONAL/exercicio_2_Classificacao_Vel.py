# Imagine que você está criando um sistema de monitoramento de tráfego para analisar a velocidade de veículos em uma rodovia.

# Sua tarefa é desenvolver um programa em Python que:

# Peça ao usuário que digite a velocidade de um veículo (em km/h).

# Analise o valor informado e exiba uma mensagem de acordo com as seguintes condições:

# Se a velocidade for menor que 40 km/h, mostrar: "Trânsito muito lento".

# Se a velocidade estiver entre 40 km/h e 60 km/h, mostrar: "Velocidade segura".

# Se a velocidade estiver entre 61 km/h e 80 km/h, mostrar: "Velocidade moderada".

# Se a velocidade for maior que 80 km/h, mostrar: "Acima do limite de velocidade".

# Dica: use estruturas condicionais (if, elif e else) para verificar os intervalos de velocidade.
# Observação Importante:
# Tente resolver o desafio por conta própria primeiro. Mas não se preocupe se não conseguir: na próxima aula, vamos mostrar uma possível solução completa e explicada para este desafio.

while True:
  try:
    velocidade = float(input("Qual a velocidade do veículo?  "))
    if velocidade < 40:
      print("Trânsito muito lento")
    elif 40 <= velocidade < 60:
      print("Velocidade segura")
    elif 60 <= velocidade < 80:
      print("Velocidade moderada")
    else:
      print("Acima do limite de velocidade")
  except:
    print("Digitar apenas números inteiros.")
    

