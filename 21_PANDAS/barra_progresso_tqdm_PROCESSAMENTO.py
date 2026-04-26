#import panda as pd
from tqdm import tqdm
import time

# for i in tqdm(range(10), desc ='Processando'):
#   time.sleep(0.5)

# print("Concluído")

nomes = ['anady', 'fernando', 'soph', 'daniel', 'silvestre']
for i in tqdm(nomes, desc ='Processando'):
  time.sleep(0.5)

print('Nomes concluídos')