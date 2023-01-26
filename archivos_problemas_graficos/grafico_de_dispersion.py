import pandas as pd
import matplotlib.pyplot as plt # para visualizar datos de forma grafica
import seaborn as sns # grafica de datos estadisticos

df = pd.read_csv('archivos_problemas_graficos\\dispersion.csv')

#Creando el grafico
sns.scatterplot(x='tiempo',y='dinero', data=df)



# Showing the plot.
plt.show()