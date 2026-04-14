#tuplas não são alteráveis, podem se duplicar, são ordenados
frutas = ('abacate', 'melancia', 'goiaba', 'mamao', 'mamao')
print(frutas)

#gerará um erro: TypeError: 'tuple' object does not support item assignment
frutas[0] = "melão"

#print(frutas[0])


