frase = input("Introduce una frase en minúsculas: ")

def contar_frecuencia(frase):
    palabras = frase.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

frecuencia_palabras = contar_frecuencia(frase)
print(frecuencia_palabras)
