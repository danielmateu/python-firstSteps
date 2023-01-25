# Si el modulo estuviera dentro de una carpeta en la misma ruta
# import funciones_buenas.Saludar as m_saludar

import sys
sys.path.append("c:\\Users\\danie\\Desktop\\python-Dalto\\funciones_buenas")
import saludar as modulo_saludo
import modulo_calculadora as calculadora
# print(sys.path)

print(modulo_saludo.Saludar('Silvia', 'Mujer'))

print(calculadora.suma(4,5))
print(calculadora.resta(4,5))
print(calculadora.multiplicacion(4,5))
print(calculadora.division(4,5))
