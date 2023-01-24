# Creamos una lista con list()
lista = list(["Hola", "Dani", 36])

# resultado = dir({'soy', 'una', 'conjunto', True})
# print(resultado)

metodos_de_listas = [
    'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',
    'remove', 'reverse', 'sort'
]

metodos_de_tuplas = ['count', 'index']

metodos_de_conjuntos = [
    'add', 'clear', 'copy', 'difference', 'difference_update', 'discard',
    'intersection', 'intersection_update', 'isdisjoint', 'issubset',
    'issuperset', 'pop', 'remove', 'symmetric_difference',
    'symmetric_difference_update', 'union', 'update'
]

# len -> Devuelve la cantidad de elementos de una lista
long_lista = len(lista)
print(long_lista)

# append -> Agregamos un elemento a la lista, modificando la lista original
lista.append('Hombre')
print(lista)

# insert -> Agrega un elemento a la lista en un indice especifico
lista.insert(3, 'Viejo')
print(lista)

# extend -> Agregamos varios elementos a la lista
lista.extend([False, 2030, 'PUTO'])
print(lista)

#POP -> Eliminamos elemento de la lista por su indice
#Si queremos eliminar el ultimo el emento de la lista: lista.pop(-1), el penúltimo: lista.pop(-2)
lista.pop(0)
print(lista)

# remove -> Eliminamos un elemento de la lista por su valor, si no lo encuentra, nos lanza una excepcion
lista.remove('PUTO')
print(lista)

# clear -> Elimina todos los elementos de la lista
# lista.clear()

# sort -> ordena la lista de forma numerica, si usamos el parametro reverse = True lo ordena de mayor a menor
lista_numerica = [True, False, False, 23, 1, 4, 86, 125, False]
lista_numerica.sort()
# lista_numerica.sort(reverse = True)
print(lista_numerica)

# reverse -> Invirtiendo los elementos de una lista
lista_numerica.reverse()
print(lista_numerica)
