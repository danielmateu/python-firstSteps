# Creando una funcion que nos devuelva los numeros primos  entre 0 y el argumento que pasamos

    # """
    # If the number is divisible by any number between 2 and the number itself, then it's not prime.
    # Otherwise, it is.
    
    # :param num: The number to be checked
    # :return: a boolean value.
    # """
def es_primo(num):
    # Checking if the number is prime or not.
    for i in range(2 ,num - 1):
        if num % i == 0: return False
        return True


    # """
    # It creates a list of prime numbers from 3 to the number we pass as an argument
    
    # :param num: The number we want to check if it's prime or not
    # :return: A list of prime numbers from 3 to the number we pass as an argument.
    # """
def primos_hasta(num):
    # Creating a list of prime numbers from 3 to the number we pass as an argument.
    primos = []
    for i in range(3, num + 1):
        resultado = es_primo(i)
        if resultado == True : primos.append(i)
    return primos


resultado = primos_hasta(12)
print(resultado)