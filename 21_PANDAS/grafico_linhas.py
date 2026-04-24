import pandas as pd
import matplotlib.pyplot as plt

vendas_mensais = {
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'Vendas': [200, 240, 180, 300, 260, 320]
}

df_vendas = pd.DataFrame(vendas_mensais)
print(df_vendas)

df_vendas.plot (
  x= 'Mês',
  y= 'Vendas',
  kind= 'line',
  marker = 'o',
  color = 'orange',
  title = 'Evolução Mensal de Vendas'
  )
plt.xlabel = ('Mês')
plt.ylabel = ('Total Vendas') 
plt.grid(True)
plt.tight_layout()
plt.savefig('Grafico_Vendas.png')
plt.show()