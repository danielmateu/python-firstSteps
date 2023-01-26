import re

text = 'The quick brown fox jumps over the lazy dog'

x = re.search('^The.*dog$', text)

if x: print('Si')
else: print('No')

# Reemplazar digitos x texto

text_02 = 'La fecha es 23/06/2023 y el telefono es +34-617-03-99-99'
#Patron a buscar
patron = r'\d{2}/\d{2}/\d{4}'

#Texto con el que se reemplazará el patron
replacement = 'Fecha oculta'

# Reemplazar todas las apariciones del patron en la cadena de texto
new_text = re.sub(patron, replacement, text_02)

# print(f' Texto modificado: {new_text}')

# Reemplazar todas las vocales por asteríscos

text_03 = 'Hoy me voy a comer todas la svocales del mundo'

new_text_03 = re.sub('[aeiou]', '*', text_03)
# print(new_text_03)

# Validacion de mails
email = 'nukpeluk@gmail.com'
pattern = '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

result = re.match(pattern, email)

if result: print('Dirección de correo válida')
else:  print('Dirección de correo no válida')

