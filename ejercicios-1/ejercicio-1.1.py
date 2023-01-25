

#Promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_actual = 1.5

#duracion de crudos
crudo_promedio = 5
crudo_actual = 3.5

#Diferencia de duración
porcentaje_min = round(curso_actual / otros_cursos_min * 100, 2)
porcentaje_max = round(curso_actual / otros_cursos_max * 100, 2)
porcentaje_promedio = round(curso_actual / otros_cursos_promedio * 100, 2)
# diferencia_con_min = 100 - curso_actual / otros_cursos_min * 100
# diferencia_con_max = 100 - curso_actual * 1000 // otros_cursos_max / 10
# diferencia_con_promedio = 100 - curso_actual / otros_cursos_promedio * 100
diferencia_con_min = 100 - porcentaje_min
diferencia_con_max = 100 - porcentaje_max
diferencia_con_promedio = 100 - porcentaje_promedio

#Calculado el porcentaje de tiempo vacio
# tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 100 / crudo_promedio 
tiempo_vacio_curso_actual = 100 - curso_actual * 1000 // crudo_actual / 10

#mostrando las diferencias de duración (Ejercicio A)
print('-------------')
print('El curso actual dura: ')
print(f' - un {diferencia_con_min}% menos que el más rapido')
print(f' - un {diferencia_con_max}% menos que el más lento')
print(f' - un {diferencia_con_promedio}% menos que el promedio')
print('-------------')


#Mostrando el tiempo vacio que se elimina(Ejercicio B)
print(f'Un curso de promedio elimina un {tiempo_vacio_promedio}% de tiempo vacío');
print(f'Este curso ha eliminado el {tiempo_vacio_curso_actual}% de tiempo vacío')
print('-------------')

#Mostrando diferencia si los cursos durasen 10 horas
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100// curso_actual / 10} horas de otros curos')
print('-------------')
