import pandas as pd
# print(type(pd))
#df -> Estructuras de datos bidimensionales que se pueden usar como una oja de calculo se divide en filas y columnas
df = pd.read_csv(
    'archivos\\datos.csv',  # names=['name', 'lastname', 'age']
)
df2 = pd.read_csv(
    'archivos\\datos.csv',  # names=['name', 'lastname', 'age']
)
# print(df)

# Obteniendo los datos de la columna nombre
nombres = df['nombre']
# print(nombres)

# Slicing [:]
cadena = '0123456789'
# print(cadena[2:8])

#ORdenando el df por la edad de forma ascendente
df_ordenado_ascendente = df.sort_values('edad')
print(df_ordenado_ascendente)

#ORdenando el df por la edad de forma descendente
df_ordenado_descendente = df.sort_values('edad', ascending=False)
print(df_ordenado_descendente)

#Concatenando los dos df
df_concatenado = pd.concat([df, df2])
print(df_concatenado)

# Accediendo a las 2 primeras fila con head()
primera_fila = df.head(2)
print(primera_fila)

# Accediendo a las 2 primeras fila con tail()
ultima_fila = df.tail(2)
print(ultima_fila)

# Accediendo a la cantidad de filas y columnas con shape
filas_y_columnas_totales = df.shape
print(filas_y_columnas_totales)
# filas_totales = filas_y_columnas_totales[0]
# columnas_totales = filas_y_columnas_totales[1]
filas_totales, columnas_totales = df.shape

# Obteniendo data estadistica del df
df_info = df.describe()
print(df_info)

# Accediendo a un elemento especifico del df con loc
elemento_especifico_loc = df.loc[3:'edad'];
elemento_especifico_iloc = df.iloc[2,2];
print(elemento_especifico_loc)
print(elemento_especifico_iloc)

# Accediento a tdas las filas de una columna
apellidos = df.loc[:'apellidos']
apellidos_iloc = df.iloc[:,1]
print(apellidos)

