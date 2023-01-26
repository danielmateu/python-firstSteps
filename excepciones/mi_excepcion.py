#Creando mi excepcion personalizada

# The class MiExcepcion inherits from the Exception class. 
# 
# The __init__ method is called when the class is instantiated. 
# 
# The __init__ method takes two parameters: self and err. 
# 
# The err parameter is the error message that is passed to the class. 
# 
# The __init__ method prints the error message
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f'Cometiste el siguiente error: {err}')
        
        
# Raising an exception and then catching it.
try:
    raise MiExcepcion('Deberias hacertelo mirar')
except: 
    print('Qué ha pasado?')
    
# Raising an exception.
raise MiExcepcion('Deberias hacertelo mirar')