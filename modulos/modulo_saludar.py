def saludar(nombre, sexo): 
    sexo = sexo.lower()
    if(sexo == 'mujer'): 
        adjetivo = 'reina'
    elif(sexo == 'hombre'):
        adjetivo = 'rey'
    else:
        adjetivo = 'amor'
    return (f"Hello {nombre}, mi {adjetivo} como va?")