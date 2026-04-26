# Importação das bibliotecas utilizadas para análise e visualização de dados

# Pandas: Biblioteca para manipulação e análise de dados estruturados (DataFrames e Series)
import pandas as pd

# NumPy: Biblioteca para operações numéricas eficientes, como arrays e funções matemáticas
import numpy as np

# Seaborn: Biblioteca para visualização de dados baseada no Matplotlib, com suporte para gráficos estatísticos
import seaborn as sns

# Matplotlib: Biblioteca para criação de gráficos estáticos e interativos
import matplotlib.pyplot as plt

# Plotly Express: Biblioteca para visualizações interativas de dados de forma simplificada
import plotly.express as px

bacteria = pd.read_excel('bacterias.xlsx')
# print(bacteria)

bacteria['Huggies']= (bacteria['Hugger_Antes_Escovacao']- bacteria['Hugger_Depois_Escovacao'])/bacteria['Hugger_Antes_Escovacao']

print(bacteria)

bacteria['Convencional_Ind']=(bacteria['Convencional_Antes_Escovacao']-bacteria['Convencional_Depois_Escovacao'])/bacteria['Convencional_Antes_Escovacao']


import matplotlib.pyplot as plt

plt.figure()

# Boxplot comparando os dois algoritmos
plt.boxplot([bacteria["Algoritmo_A"], bacteria["Algoritmo_B"]], labels=["Algoritmo A", "Algoritmo B"])

plt.title("Comparação dos Algoritmos (Boxplot)")
plt.ylabel("Tempo de Execução (ms)")

plt.show()
