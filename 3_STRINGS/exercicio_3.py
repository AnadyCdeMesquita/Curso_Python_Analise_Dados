
nome = input('Digite o nome do aluno: ').strip()
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))
atividades = input(" fez todas as atividades extras? sim ou não: ").strip().lower()
participacao = input("Teve boa participação na aulas? sim ou não: ").strip().lower()
media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7:
    media += 0.5
    if participacao == 'sim':
      print(f'O aluno foi APROVADO, média final = {media :.2f}')
    else:
      print(f'O aluno foi APROVADO, média: {media:.2f}')
elif media >= 5 and atividades == 'sim':
    print(f'Você terá direito a prova de recuperação, média final = {media + decimal:.2f}')
else:
    print(f"REPROVADO,  média final = {media:.2f} ")

