import copy

copia = {
  'x': 1,
  'x2': [9]
  }

# copia2 = copia.copy()
# #print(copia2)
# copia2['x'] = 2
# copia2['x2'][0] = [99] 
# # por ser valor de referencia, a mudança na lista altera nos dois,
# #já no valor de x não alterou
# print('copia', copia)
# print('copia2', copia2)


copia3 = copy.deepcopy(copia)
copia3['x'] = 2
copia3['x2'][0] = [99] 
print('copia', copia)
print('copia3', copia3)