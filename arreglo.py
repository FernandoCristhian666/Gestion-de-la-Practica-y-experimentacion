def buscar_mayor_menor(arreglo):
    mayor = max(arreglo)
    menor = min(arreglo)
    return mayor, menor

# Ejemplo de uso
arreglo = [12, 45, 23, 67, 34, 89, 2]
mayor, menor = buscar_mayor_menor(arreglo)
print(f"El mayor elemento es: {mayor}")
print(f"El menor elemento es: {menor}")