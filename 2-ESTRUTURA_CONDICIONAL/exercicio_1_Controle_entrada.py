# Enunciado desafio prático - Controle de Entrada
# Imagine que você foi contratado para desenvolver um sistema simples de controle de entrada para um parque de diversões. Esse sistema deve verificar a idade da pessoa que deseja entrar e aplicar algumas regras de acordo com a situação.

# As regras de entrada são:

# Pessoas com menos de 12 anos não podem entrar no parque.

# Pessoas com 12 a 17 anos só podem entrar se estiverem acompanhadas de um responsável.

# Caso estejam com um responsável, a entrada é permitida.

# Caso não estejam, a entrada é proibida.

# Pessoas com 18 anos ou mais podem entrar livremente.

# Sua tarefa é criar um programa em Python que:

# Pergunte a idade do visitante.

# Verifique as condições acima.

# Exiba a mensagem correspondente, como por exemplo:

# "Entrada proibida. Você precisa ter pelo menos 12 anos."

# "Entrada permitida! Divirta-se!"

# "Entrada permitida apenas com um responsável."

# "Entrada liberada! Divirta-se!"
while True:
    idade = int(input("Qual a sua idade? "))
    if idade < 12:
        print("Não pode entrar no parque")
    elif idade >= 12 and idade <=17:
      acompanhada = input("Vc está com um responsável? ")
      if acompanhada == "Sim":
        print('Pode entrar, vc está acompanhado')
      else:
        print("Vc não está acompanhado")
    else:
        print("Entrada liberada! Divirta-se!")

