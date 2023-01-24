definicion = 'Varios datos juntos, datos que dentro tiene datos simples que podemos agruparlos'

matriz = 'Matriz es un conjunto de datos'

#Creando una lista, se puede modificar
lista = ['Daniel Mateu', 'web developer', 36, True]
print(lista[0])

#Creando una tupla, no se puede modificar
definicion_tupla = 'Es lo mismo que una matriz pero en la que se usan los parentesis. Las tuplas, no se pueden modificar'
tupla = ('Daniel Mateu', 'web developer', 36, True)
# tupla[0] = 'Jose Fernandez'
print(tupla)

# Creando un conjuto (set)
definicion_conjunto = 'Se puede redifinir y reconstruir, pero no se puede modificar el valor de los elementos. Son datos no ordenados. No podemos acceder por el indice al elemento ni repetir valores. Para acceder a los datos debemos usar un bucle'
conjunto = {'Daniel Mateu', 'web developer', 36, True}
# print(conjunto[0]) -> No puede acceder al elemento

#Creando un diccionario (dict) podemos acceder por la clave del elemento
diccionario = {
    # 'key' : 'value',
    'nombre': 'Daniel Mateu',
    'canal' : 'dani_dev',
    'edad'  : 36,
    'altura': 1.80,
    'es_humano': True
}

print(diccionario['es_humano'])
