
# Creando una funcion con un parámetro
def saludar(nombre, sexo): 
    sexo = sexo.lower()
    if(sexo == 'mujer'): 
        adjetivo = 'reina'
    elif(sexo == 'hombre'):
        adjetivo = 'rey'
    else:
        adjetivo = 'amor'
    print (f"Hello {nombre}, mi {adjetivo} como va?")
# Ejecutando la funcion
saludar('Dani', 'Hombre')
saludar('Silvia', 'Mujer')
saludar('Nuk', 'Perro')

# Crear una funcion que nos devuelva valores, retornamos el valor requerido para usarlo fuera de la funcion
def crear_pasword_random(num):
    chars = 'abcdefghij'
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    password = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    # print(password)
    return password, num
# Desempaquetando la funcion   
password, num = crear_pasword_random(25)

# Mostrando los resultados obtenidos y los datos utilizados para obtenerlos
frase = f'Tu contraseña es {password} y el número usado fue {num}'
print(frase)