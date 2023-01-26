import pandas as pd
import matplotlib.pyplot as plt # para visualizar datos de forma grafica
import seaborn as sns # grafica de datos estadisticos

df = pd.read_csv('archivos_problemas_graficos\\bigotes.csv')
# print(df)

#Creando El Grafico
sns.boxplot(x='categoria',y='valor', data=df)


#mostrar el grafico
plt.show()