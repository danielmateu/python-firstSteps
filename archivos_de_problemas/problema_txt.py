# 2 listas, una con nombres otra con apellidos
nombres = ['Daniel','Silvia','Nuk','Jose','Teresa']
apellidos = ['Mateu','Cazorla','Peluk','Cazorla','Martinez']

#Registrar la info en un txt de forma optima
with open('problemas_de_archivos\\nombres_y_apellidos.txt','w') as arch:
    arch.writelines('Los datos son:\n------------ \n')
    [arch.writelines(f'Nombre: {n}\nApellido: {a}\n ----------- \n') for n,a in zip(nombres, apellidos)]
