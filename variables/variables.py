definicion = 'Las variables son espacios de memoria que usamos dentro del programa donde almacenamos datos'

# Definendo la variable
a = 5
b = 8
c = a + b

print(c)

#Definiendo variable con camelCase
nombreCompleto = 'Daniel Mateu'
print(nombreCompleto)

#Definiendo variable con snake_case, como se recomienda en Python 🐍
nombre_completo = 'Daniel Mateu'
print(nombre_completo)

# Concatenacion
bienvenida = "Hola " + nombreCompleto + " cómo estás?"
print(bienvenida)

# Tomamos un dato y se transforma en texto concatenando con f-strings
bienvenidaF = f"Hola {nombreCompleto} cómo estás?" 
print(bienvenidaF)

# Para eliminar la declaración de la variable, borrar datos
del nombreCompleto;
print(bienvenidaF)

# Operaciones de pertenencia / identidad -> Devuelve true o false en función de si está o no
print('Hola' in bienvenidaF) #true
print('Hola' not in bienvenidaF) #false


