texto = 'Meu nome é Soph'
print(texto.lower())
print(texto.casefold()) #mesma coisa do lower 
print(texto.upper())
print(texto.capitalize()) #só a primeira letra maiúscula
print(texto.title()) # letra maiúscula de cada palavra

texto = '   Meu nome é Soph   '
print(texto)
print(texto.strip())
print(texto.replace('Soph', 'Anady'))
texto = 'Meu nome é Soph'
print(texto.split()) # transforma em lista

texto1 = '11/05/1980'
print(texto1.split()) 

texto1 = '11/05/1980'
print(texto1.split('/')) # retira a barra

palavra = ['soph', 'é', 'minha', 'cadelinha.']
frase = ' '.join(palavra)
print(frase.title())

