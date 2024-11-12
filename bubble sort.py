def bubble_sort(arreglo):
    n = len(arreglo)
    for i in range(n):
        for j in range(0, n-i-1):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
    return arreglo

# Ejemplo de uso
arreglo = [64, 34, 25, 12, 22, 11, 90]
arreglo_ordenado = bubble_sort(arreglo)
print("Arreglo ordenado por Bubble Sort:", arreglo_ordenado)