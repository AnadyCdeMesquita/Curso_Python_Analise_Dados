a = [1, 2, 3, 4]
b = a 
print(b is a) # objetos iguais

b[0] = 5
print(a)
print(b)

c= [5,2,3,4]
print(a==c) # tem os mesmo conteúdo