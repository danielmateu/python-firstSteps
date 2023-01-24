

#Creando diccionarios con dict()
diccionario = dict(nombre = 'Dani', apellido = 'Mateu');

#Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(['dani', 'mateu']): 'El més guapo'}

#Creando diccionario con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(['nombre', 'apellido']);

#Creando diccionario con fromkeys() valor por defecto: 'lo que sea'
diccionario = dict.fromkeys(['nombre', 'apellido'], 'lo que sea');

print(diccionario)