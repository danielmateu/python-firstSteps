with open('archivos\\texto_de_dani.txt', 'w',encoding='utf-8') as archivo:
    
    # Writing the text in the file.
    # archivo.write('Haahahahahaha eres un puto')
    # Writing the text in two lines in the file.
    archivo.writelines(['-Hola maestro, cómo andás?\n', ' -puto... 🐍\n'])
    archivo.writelines(['-Hola maestro, todo bien\n', ' -puto tú... 🦄\n'])