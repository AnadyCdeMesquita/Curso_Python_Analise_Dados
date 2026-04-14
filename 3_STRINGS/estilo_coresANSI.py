# Sintaxe Básica
# A sequência de escape ANSI começa com o caractere de escape, 
# seguido por um colchete abrindo [. 
# Caractere de Escape: \033 (octal), \x1B (hexadecimal), ou \e.
# Estrutura: \033[<CÓDIGO>m
# Texto em Negrito (1), Azul (34) e Fundo Amarelo (43)
print('\033[1;34;43mTexto Formatado\033[m')
print('\033[35m Fernado Antonio\033[0m')

print('\033[1;30;43m Soph Freitas Carvalho \033[0m')

print('\033[1;34;42m Fui a escola estudar\033[0m')

print('\033[1m meu nome é soph\033[0m')