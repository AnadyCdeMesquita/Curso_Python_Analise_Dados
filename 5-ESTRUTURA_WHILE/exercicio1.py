while True:
    nome = input("Digite o seu nome: ").strip()
    
    if  not nome.isalpha():
       print('Deve conter somente letras')
       continue
    while True:
        senha = input('Digite a sua senha: ').strip()
        if senha == nome:
            print('A senha não pode ser igual ao nome')
            continue
        if  len(senha) <= 4:
            print('A senha deve conter quatro dígitos ou mais')
            continue
        maiuscula = any(c.isupper() for c in senha)
        minuscula = any(c.islower() for c in senha)
        numero = any(c.isdigit() for c in senha)
        if  not (maiuscula and minuscula and numero):
            print('Deve conter pelo menos uma maiuscula, uma minuscula e um digito')
            continue
        break
