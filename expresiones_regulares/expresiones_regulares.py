# Importing the regular expression module.
import re

texto = '''
    Hola maestro como estás mi capitán, esta es la cadena 1
    Hola putito yo estoy bien y tu?, esta es la cadena 2
    Esta es la última linea, la número 3!
'''
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
print(resultado_busqueda_no_alfanumerica)
