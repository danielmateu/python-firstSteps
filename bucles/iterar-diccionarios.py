diccionario = {
    "nombre": "Daniel",
    "apellido": "Mateu Pardo",
    "edad"  : 36,
    "sexo"  : "hombre"
}

# Recorriendo el diccionario para obtener las claves
for key in diccionario: print(f'{key}')

# Recorriendo diccionario con items() para obtener la clave y el valor
for datos in diccionario.items(): 
    key = datos[0]
    value = datos[1]
    print(f'{key}: {value}')