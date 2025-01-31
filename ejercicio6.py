lista = ["gato", "perro", "elefante"]

def contar_letras(lista):
    longitud_palabras = {}
    for palabra in lista:
        longitud_palabras[palabra] = len(palabra)
    return longitud_palabras

resultado = contar_letras(lista)
print(resultado)