# Creando una funcion de 3 parametros
def frase(nombre, apellido, adjetivo, sexo ):
    if sexo == 'hombre': adjetivo = 'feo'
    elif sexo == 'mujer': adjetivo = 'fea'
    else: adjetivo = 'ugly'
    return (f'Hola {nombre} {apellido}, eres muy {adjetivo}')


#Utilizando keyword arguments
frase_resultante = frase(nombre='Dani', apellido='Mateu', adjetivo='', sexo='perros')
print(frase_resultante)