

cpf = input("Digite o número do seu CPF: ").strip().replace('.', '').replace('-','')
if len(cpf) == 11 and cpf.isdigit():
    print(f'CPF DIGITADO COM SUCESSO: {cpf}')
else:
    print('Digite somente número')
