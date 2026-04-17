pessoa = {'Nome':'Ana', 'idade': 45, 'Profissão':'Analise Dados'}

#POP 
#teste = pessoa.pop('Nome')
#print(pessoa)
#print(teste)

#DEL 
#del pessoa['Profissão']
#print(pessoa)

#POP ITEM
#A sintaxe do método popitem() em Python é dicionario.popitem().
#Ele remove e retorna o último par (chave, valor) inserido no dicionário como uma tupla. 

pessoa = {'Nome':'Ana', 'idade': 45, 'Profissão':'Analise Dados'}

removendo = pessoa.popitem() # retorna tupla
print(pessoa)
print(removendo)

