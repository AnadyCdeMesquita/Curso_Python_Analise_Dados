#cuidado = é case sensitive, se não achar, retorna -1, no caso FIND.
#FIND = posição na frase, na string
texto = 'Meu nome é Soph e tenho 5 anos de idade, sou Soph.'
print(texto.find('Soph'))

teste = 'viva a vida'
print(teste.find('vida', 4, 11))

#COUNT

contagem = "MARIA SOPH"
print(contagem.count('A'))

#startswith
textando = 'ela se chama de Soph'
print(textando.startswith('ela se'))
print(textando.startswith('ela'))

#endswith 
textando2 = 'ela se chama de Soph'
print(textando2.endswith('de Soph'))
print(textando2.endswith('de Soph'))

#ISDIGIT
numero = '12345'
print(numero.isdigit())

numero = 'a12345'
print(numero.isdigit())

#ISALPHA
palavra = 'abacde'
print(palavra.isalpha())

palavra2 = '11abacde'
print(palavra2.isalpha())

#ISALNUM

alfa = 'maria123'
print(alfa.isalnum())