#Método Count
alunos =  ('Anady', 'Ana', 'Bruno', 'Fernando', 'Soph', 'Laura', 'Anady', 'Bruno', 'Anady')

print(alunos.count('Anady'))

#metodo index
print(alunos.index('Anady')) # print = 0
print(alunos.index('Anady', 3, 7)) #print = 6
#há mais 'anady', o python pega de 1 em 1, sempre o primeiro, no intervalo definido.

try:
  print(alunos.index('Anady', 3, 7)) #print = 6
except:
  print('Nome não encontrado')
      