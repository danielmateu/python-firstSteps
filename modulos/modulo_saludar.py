def Saludar(nombre, sexo): 
    sexo = sexo.lower()
    if(sexo == 'mujer'): 
        adjetivo = 'reina'
    elif(sexo == 'hombre'):
        adjetivo = 'rey'
    else:
        adjetivo = 'amor'
    return (f"Hello {nombre}, mi {adjetivo} como va?")

def Saludo_raro(nombre, sexo): 
    sexo = sexo.lower()
    if(sexo == 'mujer'): 
        adjetivo = 'reina'
    elif(sexo == 'hombre'):
        adjetivo = 'rey'
    else:
        adjetivo = 'amor'
    return (f"Que pasa {nombre} , mi {adjetivo} vols fer un kiki?")

