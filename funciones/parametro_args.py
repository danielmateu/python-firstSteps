# Forma no optima de sumar valores
# def suma(numeros):
#     numeros_sumados = 0
#     for numero in numeros:
#         numeros_sumados += numero
#     return numeros_sumados

# resultado = suma([1, 2, 10, 25])
# print(resultado)


# Utilizando el operador * como parametro *args
def suma(nombre, *numeros):
    return f'{nombre}, la suma de tus números es: {sum(numeros)}'

resultado = suma('Dani',1, 2, 10, 25)
print(resultado)

# Lo mísmo que arriba, pero usando el operador en el return, da más libertad 
def suma_total(numeros,nombre):
    return f'{nombre}, la suma de tus números es: {sum(*numeros)}'

resultado_total = suma('Silvia',10, 25, 20, 25)
print(resultado_total)
