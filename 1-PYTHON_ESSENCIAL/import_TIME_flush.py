import time

for i in range(10):
  print('Carregando....', i, end="\r", flush = True)
  time.sleep(2)