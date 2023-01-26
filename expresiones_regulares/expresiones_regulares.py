# Importing the regular expression module.
import re

texto = '''
Hola maestro como estás mi capitán. Esta es la ababaab cadena 1. Hola putito yo estoy bien y tu?, esta es la cadena 2416546 ab.
    Esta es la última linea, la número 3!'''
#Haciendo una busqueda simple
resultado = re.search('hola', texto, flags=re.IGNORECASE)
resultado_all = re.findall('cadena', texto)

# print(resultado)
# print(resultado_all)

# \d -> busqueda de digitos numéricos del 0 al 9
resultado_busca_numerica = re.findall(r'\d', texto)
# print(resultado_busca_numerica)

# \D -> busqueda TODO menos digitos numéricos del 0 al 9
resultado_busca_no_numerica = re.findall(r'\D', texto)
# print(resultado_busca_no_numerica)

# \w -> busqueda de datos alfanuméricos [a-z A-Z 0-9 _]
resultado_busqueda_alfanumerica = re.findall(r'\w', texto)
# print(resultado_busqueda_alfanumerica)

# \W -> busqueda de datos alfanuméricos [a-z A-Z 0-9 _]
resultado_busqueda_no_alfanumerica = re.findall(r'\W', texto)
# print(resultado_busqueda_no_alfanumerica)

# \s -> busqueda espacios en blanco, los saltos en linea y tabs
resultado_busqueda_espacios = re.findall(r'\s', texto)
# print(resultado_busqueda_espacios)

# \S -> busqueda TODO Menos espacios en blanco, los saltos en linea y tabs
resultado_busqueda_SIN_espacios = re.findall(r'\S', texto)
# print(resultado_busqueda_SIN_espacios)

# . -> Busca TODO menos saltos de linea
resultado_busqueda_sin_saltos_de_linea = re.findall(r'.', texto)
# print(resultado)
#\n -> Busca saltos de linea
resultado_busqueda_saltos_de_linea = re.findall(r'\n', texto)
# print(resultado)

# \ -> Cancelamos caracteres especiales, buscando puntos
resultado_busqueda_cancelando_caracteres_especiales = re.findall(r'\.', texto)
# print(resultado_busqueda_cancelando_caracteres_especiales)

#Buscar una cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall(r'\d\.\s', texto)
# print(resultado)

# ^ -> Buscar el comienzo de una linea
resultado = re.findall(r'^Hola', texto, flags=re.M) #M -> activa la Multilinea
# print(resultado)


# $ -> Buscar el final de una linea
resultado = re.findall(r'3!$', texto, flags=re.M) #M -> activa la Multilinea
# print(resultado)

# {n} -> Busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r'\d{3}\s', texto)
# print(resultado)

# {n,m} -> Al menos n como máximo m
resultado = re.findall(r'\d{2,4}', texto)
# print(resultado)

resultado = re.findall(r'[ab]{2}', texto)
# print(resultado)

# | Busca una cosa o la otra, te muestra las dos
resultado = re.findall(r'\d{2,4}|Hola', texto)
print(resultado)


