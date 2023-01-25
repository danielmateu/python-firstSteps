#Ha faltado el profe y hay que armar la clase

#Pedir el nombre y la edad de los compañeros que han ido hoy a clase
def obtener_alumnos(cantidad):
    
    alumnos = []
    # Asking for the name and age of the students that went to class today.
    for alumno in range(cantidad):
        nombre = input('Ingresa el nombre del alumno: ')
        edad = int(input('Ingresa la edad del alumno: '))
        alumno = (nombre, edad)
        alumnos.append(alumno)
    # Sorting the list of tuples by the second element of the tuple.
    alumnos.sort(key=lambda x: x[1])
    # Getting the first element of the first tuple in the list of tuples.
    asistente = alumnos[0][0]
    # Getting the last element of the list of tuples, and then getting the first element of that
    # tuple.
    profesor = alumnos[-1][0]
    return asistente, profesor

# Unpacking the return values of the function `obtener_alumnos` into the variables `asistente` and
# `profesor`.
asistente, profesor = obtener_alumnos(5)

print(f'El asistente es {asistente} y el profesor es {profesor}')
