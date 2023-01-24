# Los podemos crear con set
conjunto = set(['Dato 1', 'Dato 2'])

#metiendo un conjunto dentro de otro conjunto
conjunto_1 = frozenset(['dato 1', 'dato 2'])
conjunto_2 = {conjunto_1, 'dato 3'}

print(conjunto)
print(conjunto_2)

#Teoria de conjuntos

conjunto1 = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}
conjunto3 = {2, 4, 6, 8}

#Verificando si es un subconjunto
resultado_subconjunto = conjunto2.issubset(conjunto1)
# resultado = conjunto2 <= conjunto1
print(resultado_subconjunto)


#Verificando si es un superconjunto
resultado_superconjunto = conjunto2.issuperset(conjunto1)
# resultado_superconjunto = conjunto2 > conjunto1
print(resultado_superconjunto)

#Verificar si hay algun numero en común
resultado_comun = conjunto3.isdisjoint(conjunto1)
print(resultado_comun)