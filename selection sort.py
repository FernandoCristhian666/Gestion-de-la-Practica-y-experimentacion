def selection_sort(arreglo):
    n = len(arreglo)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arreglo[j] < arreglo[min_index]:
                min_index = j
        arreglo[i], arreglo[min_index] = arreglo[min_index], arreglo[i]
    return arreglo

# Ejemplo de uso
arreglo = [64, 25, 12, 22, 11]
arreglo_ordenado = selection_sort(arreglo)
print("Arreglo ordenado por Selection Sort:", arreglo_ordenado)