cadena1 = '36'
nombre = 'Dani'
# cadena2 = f'Bienvenido {nombre}'
cadena2 = 'Bienvenido'
cadena3 = f'Bienvenido, mi nombre es {nombre}'

resultado = dir(cadena1)

print(resultado)

string_methods = [
    'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
    'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
    'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
    'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join',
    'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix',
    'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
    'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
    'swapcase', 'title', 'translate', 'upper', 'zfill'
]

#Convierte a Mayusculas
resultado_upper = cadena1.upper()
#Convierte a Minúscula
resultado_lower = cadena1.lower()
#Convierte el string en minúscula y primera letra en Mayúscula
resultado_capitalize = cadena1.capitalize()

#FIND -> Nos retorna un valor, busca una cadena en otra cadena, devuelve la posicion en la cadena, Si no aparece el valor, devuelve -1
busqueda_find = cadena1.find('Dani')

#Index -> Buscamos una cadena dentro de otra cadena, si no encuentra nada, nos tira un error
busqueda_index = cadena1.index('')

print(resultado_upper)
print(resultado_capitalize)
print(busqueda_find)
print(busqueda_index)

#isnumeric -> Funcion que nos devuelve true si el dato es numerico, si no nos devuelve false
es_numerico = cadena1.isnumeric()
print(es_numerico)

#isalpha -> Funcion que nos devuelve true si el dato no es numerico, si no nos devuelve false
es_alfanumerico = cadena2.isalpha(
)  #Solo devuelve true si es Literalmente alphanumerico, de la a la z
print(es_alfanumerico)

#count -> nos dice cuantas veces coincide
contar_coincidencias = cadena2.count('i')
print(contar_coincidencias)

#len -> Devuelve la longitud de la cadena, no es un método. Es una función
contar_caracteres = len(nombre)
print(f'{nombre} tiene {contar_caracteres} caracteres')

#startswith -> Tambien es un metodo. Verifica si una cadena empieza con otra cadena dada, si es así, devuelve true
empieza_con = nombre.startswith('Dan')
print(empieza_con)

#endsswith -> Tambien es un metodo. Verifica si una cadena termina con otra cadena dada, si es así, devuelve true
acaba_con = nombre.endswith('ni')
print(acaba_con)

#replace -> Remplaza un pedazo de la cadena dada por otra dada, si encuentra coincidencias en el primer parametro, los cambia por la cadena dada, si no, mantiene la cadena original
cadena_reemplazada = nombre.replace( 'ni', 'Silvia' )
print(cadena_reemplazada)

#split -> Nos devuelve una lista (matriz)
sin_comas = cadena3.replace(',','')
cadena_separada = sin_comas.split(' ')
print(cadena_separada[0])