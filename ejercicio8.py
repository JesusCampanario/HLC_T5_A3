def contar_vocales_consonantes(texto):
    vocales = "aeiouAEIOU"
    conteo = {"vocales": 0, "consonantes": 0}
    
    for char in texto:
        if char():
            if char in vocales:
                conteo["vocales"] += 1
            else:
                conteo["consonantes"] += 1
                
    return conteo

texto = "Hola esto es phython"
resultado = contar_vocales_consonantes(texto)
print(resultado)