

animales = {'perro', 'gato', 'loro', 'cocodrilo'}
numeros = {2, 4, 10, 54}
print('--------------')

# Recorriendo la conjunto animales
for animal in animales: print(f'Ahora la variable animal es: {animal}')
print('--------------')

for numero in numeros: print(numero * 2)
print('--------------')

# Para iterar dos conjuntos del mismo tamaño anidamos un for dentro de otro con la funcion zip
for numero, animal in zip(animales,numeros): 
    print(f'recorriendo conjunto 1: {numero}')
    print(f'recorriendo conjunto 2: {animal}')

print('--------------')
# Para iterar una conjunto en función del rango
for num in range(5,10): print(num)
print('--------------')

#Forma correcta de recorrer una conjunto con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    # print(type(num))
    # print(num[0])
    print(f'{indice}: {valor}')
print('--------------')

# Usando el for-else
for numero in numeros: 
    indice = num[0]
    valor = num[1]
    print(f'{indice}: {numero}')
else: print('El bucle terminó')

# Todo lo anterior funciona para tuplas y listas