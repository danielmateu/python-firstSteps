diccionario = {
    # 'key' : 'value',
    'nombre': 'Daniel Mateu',
    'canal': 'dani_dev',
    'edad': 36,
    'altura': 1.80,
    'es_humano': True
}

metodos_dict = dir(diccionario)
print(metodos_dict)

resultado = [
    'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',
    'setdefault', 'update', 'values'
]

# keys -> Nos devuelve las keys y nos sirve para iterar

llaves = diccionario.keys()
print(llaves)

# get -> devuelve el valor de una clave, si no se encuentra, devuelve un error, si no tiene valor, devuelve none -> undefined en JS
llaves = diccionario.get('nombre')
print(llaves)

# clear -> elimina todos los elementos del diccionario
# diccionario.clear()

# pop -> elimina un elemento
diccionario.pop('altura')
print(diccionario)

# items -> para iterar el dict
diccionario_iterable = diccionario.items();
print(diccionario_iterable)