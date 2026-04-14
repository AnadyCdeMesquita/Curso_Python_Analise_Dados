# nome = input('Digite o seu nome: ').strip()
# email = input("Digite seu email: ").strip()

# if nome == '' and email == '':
#   print('Dados não informados.')
# elif nome and email:
#     if '@' in email and '.' in email:
#       print(f'Dados corretos: {nome} e {email}')
#     else:
#       print("email inválido")
# else:
#   print('Dados Incompletos')
  
nome1 = input('Digite o seu nome: ').strip()
email1 = input("Digite seu email: ").strip()
if nome1 and email1:
    if '@' in email1 and '.' in email1:
      print(f'Dados corretos: {nome1} e {email1}')
    else:
      print('email inválido')
else:
  print('Dados Incompletos')