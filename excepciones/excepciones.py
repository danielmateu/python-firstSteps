



    # It asks for two numbers, and if they are not numbers, it asks again
def sumar_dos():
    while True:
        # Asking for a number.
        num1 = input('Introduce un número: ')
        num2 = input('Introduce otro número: ')
        try:
            # Adding the two numbers.
            resultado = int(num1) + int(num2)
        except Exception as e:
            # Printing a message to the user.
            print('Introduce un numeroDebes introducir dos números, ambécil')
            print(f'Error: {e}')
        # Breaking the loop.
        else:  break
        # Printing a message to the user.
        finally: print('Manejo de excepción finalizado')
            
    # Returning the result of the sum of the two numbers.
    return resultado

# Calling the function `sumar_dos()` and printing the result.
print(sumar_dos())