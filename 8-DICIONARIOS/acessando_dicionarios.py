pessoa = {'Nome':'Ana', 'idade': 45, 'Profissão':'Analise Dados'}
print(pessoa)
pesquisa = pessoa['Nome']
pesquisa1 = pessoa.get('Nomes') # retorna None por padrão por não tem encontrado, já que Nome está no singular
pesquisa2 = pessoa.get('Nomes', 0)
print(pesquisa)
print(pesquisa1)
print(pesquisa2)
