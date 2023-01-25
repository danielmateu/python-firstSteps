numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Son como las arroy functions en JS, crea funciones anonimas que despues podemos almacenar en variables
multiplicar_por_dos = lambda x: x * 2

print(multiplicar_por_dos(10))

# Beneficios ->
# Lo podemos usar cuando queremos hacer algo rápido y sencillo
# Hacen el retorno de forma automática

# No son aptas cuando tenemos que dar más de una instruccion

# Creando una funcion comun que diga si es par o no
def es_par(num):
    if(num % 2 == 0): return True
    
# Usando filter con una funcion comun
numeros_pares = filter(es_par, numeros)

print(f'Función común -> {list(numeros_pares)}')

# Lambda version
numeros_impares_lambda = filter(lambda numero: numero % 2 != 0, numeros)
print(f'Lambda version -> {list(numeros_impares_lambda)}')