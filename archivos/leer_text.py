

# archivo_sin_leer = open('archivos\\texto_de_dani.txt', encoding='utf-8')
# Opening the file and assigning it to the variable `archivo`.
archivo = open('archivos\\texto_de_dani.txt', encoding='utf-8')

# Leer archivo completo
# archivo = archivo.read()
# print(archivo)

# Leer linea por linea
# lineas = archivo.readlines()
# print(lineas)

linea = archivo.readline()
linea2 = archivo.readline()
# print(linea)

#Cerrar el archivo
archivo.close()
print(linea)
print(linea2)