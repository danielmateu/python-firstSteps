import pandas as pd
import matplotlib.pyplot as plt # para visualizar datos de forma grafica
import seaborn as sns # grafica de datos estadisticos

df = pd.read_csv('archivos_problemas_graficos\\pedos.csv')
# print(df)

# Plotting a line graph with the data from the dataframe.
sns.lineplot(x='fecha',y='pedos', data=df)

# Plotting a point at the coordinates (01-15, 20)
plt.plot('01-15', 20,'o')

plt.show()