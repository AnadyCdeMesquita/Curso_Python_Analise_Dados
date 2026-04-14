frutas = ['maca', 'mamao', 'abacaxi', 'kwui', 'pitanga']
#nas strings leva-se em consideração a ordem alfabética
print(f'A quantidade de strings nas listas: {len(frutas)}')
print(f'A MAIOR É {max(frutas)}')
print(f'A MENOR É {min(frutas)}')
#SUM NÃO EXISTE PARA STRINGS
print(f'A ordem é {sorted(frutas, reverse=True)}')
print(f'A ordem é {sorted(frutas)}')

numeros = [10,20,30,450,50,48]
print(f'O maior número é: {max(numeros)}')
print(f'O menor número é: {min(numeros)}')
print(f'Ordenação cresente número é: {sorted(numeros)}')
print(f'Ordenação decrescente: {sorted(numeros, reverse=True)}')
print(f'A soma dos números são {sum(numeros)}')
print(f'A média dos números são: {sum(numeros)/ len(numeros):.2f}')



