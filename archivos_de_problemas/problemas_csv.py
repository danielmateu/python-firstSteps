#Debemos cambiar el tipo de datos de una columna

import pandas as pd
df = pd.read_csv('archivos_de_problemas\\datos.csv')
# print(df)
# print(type(df['edad']))

# Changing the type of the column 'edad' to string.
cambio_tipo_dato = df['edad'] = df['edad'].astype(str)
# Printing the type of the first element of the column 'edad'
# print(type(cambio_tipo_dato[0]))

# Reemplazar Valores
reemplazo_apellidos = df['apellidos'].replace('cazorla', 'guapo')
# print(reemplazo_apellidos)

#Eliminar filas con datos faltantes
df = df.dropna()
# print(df)

#Eliminar filas duplicadas
df = df.drop_duplicates()
# print(df)

# Creando un CSV con el dataframe limpio (resultante)
df.to_csv('archivos_de_problemas\\datos_limpios.csv')