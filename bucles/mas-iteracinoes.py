frutas = ['banana', 'pera', 'sandia', 'naranja', 'fresa', 'guacamole']
numeros = [2, 4, 8, 25]

# Evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if (fruta == 'pera'): continue
    print(f'{fruta}')
print('-------')

# Evitar que el bucle se siga ejecutando (El else no se ejecuta tampoco)
for fruta in frutas:
    print(f'{fruta}')
    if (fruta == 'pera'): break
else: print('Bucle terminado')

print('-----------')

# Recorrer / Iterar cadena de texto
cadena = 'Hola me llamo Dani'

for letra in cadena:
    print(letra)


# for en una sola linea de codigo para duplicar los numeros
numeros_duplicados = [x * 2 for x in numeros]
print(numeros_duplicados)

