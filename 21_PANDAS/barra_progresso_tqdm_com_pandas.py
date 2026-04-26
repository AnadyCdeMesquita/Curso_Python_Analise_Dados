import pandas as pd
from tqdm import tqdm
tqdm.pandas()

df = pd.DataFrame({'numeros': range(1, 10)})

df['dobro'] = df['numeros'].progress_apply(lambda x: x * 2)

print(df)