import re

# Detectando un núero y ocultandolo

texto = 'mi número es: +34 617-039-999 +34 617-039-999 +34 617-039-999'

pattern = r'\+\d{1,3}\s\d{3}-\d{3}-\d{3}'

reemplazo = re.sub(pattern, '(Numero Oculto)', texto)
print(reemplazo)