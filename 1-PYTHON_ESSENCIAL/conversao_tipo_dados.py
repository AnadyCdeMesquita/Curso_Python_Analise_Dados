n1 = '10'
n2 = int(n1)
print(n2)
print(type(n2))

n3 = float('10')
print(n3)

# int, str, float, bool

t1 = 1
t2 = 1.1
t3 = False
t4 = 'Python'

#CONVERSÃO DE DADOS
#STRING
print(str(t1), str(t2), str(t3), str(t4))

#INT
print(int(t1), int(t2), int(t3)) 
#print(int(t4)) não se converte string em numero inteiro ou float

#FLOAT
print(float(t1),float(t2),float(t3)) 
#print(float(t4)) #não se converte string em numero inteiro ou float

#BOOLEAN
print(bool(t1), bool(t2), bool(t3), bool(t4)) 
string2 = ""
print(type(string2))
print(bool(string2))


#QUANDO UM STRING É PREENCHIDA EX: "ANADY", CONVERTENDO PARA BOOLEAN É CONSIDERADA TRUE,
#MAS QUANDO STRING É VAZIA "", CONVERTENDO PARA BOOLEANO É CONSIDERADA FALSA

#OS VALORES INT = 0 OU FLOAT 0.0 SÃO BOOLEANOS False SEMPRE
#OUTROS VALORES INT E FLOAT SÃO CONSIDERADOS True