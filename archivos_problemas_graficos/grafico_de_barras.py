import pandas as pd
import matplotlib.pyplot as plt # para visualizar datos de forma grafica
import seaborn as sns # grafica de datos estadisticos

df = pd.read_csv('archivos_problemas_graficos\\cofla_ingresos.csv')
# print(df)

# Plotting a line graph with the data from the dataframe.
sns.barplot(x='fuente',y='ingresos', data=df)

# Summing all the values in the column `ingresos`
total_ingresos = df['ingresos'].sum()

# Printing the total of the column `ingresos`
print(f'El total de ingresos: {total_ingresos}')

# Plotting a point at the coordinates (01-15, 20)
# plt.plot('01-15', 20,'o')

plt.show()