# Opening the file `archivos\texto_de_dani.txt` and assigning it to the variable `archivo`.
with open('archivos\\texto_de_dani.txt', encoding='utf-8') as archivo:
    # Assigning the content of the file to the variable `contenido`.
    contenido = archivo.read()
    # Printing the content of the file.
    print(archivo.read())
    
    # No es necesario cerrarlo al usar el with open