#Suponiendo que el promedio habla 2 palabras / segundo:

# a) Pedirle al usuario que diga cualquier texto real y: Calcular cuanto tardaría en decir esa frase y cuantas palabras dijo

texto_usuario = input('Introduce un texto: ')
# print(texto_usuario)
num_palabras_introducidas = len(texto_usuario.split(' '))
tiempo_promedio = float(num_palabras_introducidas)
print(f'Has introducido {num_palabras_introducidas} palabras y has tardado {tiempo_promedio / 2} segundos')

# b) Si tarda más de un minuto decirle: 'Para flaco, tampoco te pedí un testamento
if tiempo_promedio > 60 or num_palabras_introducidas > 120 : print('Para flaco, tampoco te pedí un testamento')

# c) Cuanto tardaría alguien que hable un 30% más rápido
speed_talker = num_palabras_introducidas * 100 // 2.3 / 100
print(f'Si lo dijese alguien que habla un 30% más rápido, tardaria {speed_talker} segundos')



