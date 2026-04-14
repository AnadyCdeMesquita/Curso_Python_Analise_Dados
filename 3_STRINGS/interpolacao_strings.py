nome = 'Anady'
idade = 15

msg = f'Meu nome é {nome} e minha idade é {idade}.'
print(msg)

msg1 = 'Meu nome é %s e minha idade é %d'%(nome, idade) 
print(msg1) 

msg2 = 'Meu nome é {} e minha idade é {}'. format(nome, idade)
print(msg2) 