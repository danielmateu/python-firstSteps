

# Funciones buildin / integradas -> Funciones creadas por python

numeros = [4, 7, 10, 2, 50]

# encontrando el numero mayor de una lista, tupla (tiene que ser un elemento iterable)
numero_mas_alto = max(numeros)
print(f'Este es el número más alto: {numero_mas_alto}')

# encontrando el numero menor de una lista, tupla (tiene que ser un elemento iterable)
numero_mas_bajo = min(numeros)
print(f'Este es el número más bajo: {numero_mas_bajo}')

# Redondeando a 2 decimales
numero = round(12.4561123654, 2)
print(numero)

# retorna False -> 0, vacio, False, None | True -> distinto a 0, True, cadena, datos no vacios
resultado = bool('') 
print(f'Es {resultado}')

# retorna True si todos los valores son verdaderos
resultado_all = all([234, 'all', True])
print({resultado_all})

# Suma todos los valores de un iterable
suma_total = sum(numeros)
print(f'Suma total: {suma_total}')





