# Enunciado desafio prático - Verificando se o aluno pode fazer a prova final
# Você foi contratado para desenvolver uma ferramenta simples de verificação de aprovação para a prova final. O sistema deve avaliar se um aluno poderá ou não realizar a prova final com base em dois critérios:

# Média final do aluno (um número decimal).

# Entrega das atividades extras (sim ou não).

# Regras de aprovação:
# Se a média final do aluno for maior ou igual a 7, ele terá direito de realizar a prova final.

# Caso o aluno não tenha alcançado a média 7, ele ainda poderá fazer a prova final se tiver entregue todas as atividades extras.

# Caso nenhuma dessas condições seja atendida, o aluno não poderá realizar a prova final.

# Objetivo do desafio:
# Solicitar a média final do aluno.

# Perguntar se ele realizou todas as atividades extras.

# Exibir a mensagem adequada:

# "Você pode fazer a prova final."

# "Você não pode fazer a prova final."

# Observação Importante:

# Tente resolver o desafio por conta própria primeiro. Mas não se preocupe se não conseguir: na próxima aula, vamos mostrar uma possível solução completa e explicada para este desafio.


nota = float(input('Qual a sua nota?  '))

atividade = input("realizou todas as atividades extras? ")

if nota >= 7 or atividade == 's':
  print("Vc fara a prova final")
else:
  print("Não fará prova final")