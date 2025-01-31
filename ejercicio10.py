def eliminar_pares(lista):
    return [num for num in lista if num % 2 != 0]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = eliminar_pares(numeros)
print(resultado)