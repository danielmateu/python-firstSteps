# import modulo_saludar as saludo
# Importing the functions `saludar` and `saludo_raro` from the module `modulo_saludar`.
from modulo_saludar import Saludar as Saludo_normal, Saludo_raro
# from modulo_saludar import * Lo importa todo, pero es una mala práctica


# saludo = modulo_saludar.saludar('Dani', 'hombre')
# saludo = saludo.saludar('Dani', 'hombre')

# Calling the function `saludar` from the module `modulo_saludar` and passing the arguments `'Dani'`
# and `'hombre'` to it.
saludo = Saludo_normal('Silvia', 'mujer')
# Calling the function `saludo_raro` from the module `modulo_saludar` and passing the arguments
# `'Nuk'` and `''` to it.
saludo_alt = Saludo_raro('Nuk','')

print(saludo)
print(saludo_alt)

#Para ver las propiedades y métodos de el namespace
# print(dir(namespace))

