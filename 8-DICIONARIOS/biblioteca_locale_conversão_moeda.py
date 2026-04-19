import locale

# Exemplo de uso para configurar para o português brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

valor = input('digite um valor: ')
valor = float(valor)
print(f'O valor é {locale.currency(valor, grouping=True)}')