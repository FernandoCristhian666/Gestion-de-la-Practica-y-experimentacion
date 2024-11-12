# Gestion-de-la-Practica-y-experimentacion
1. Introducción
   
El propósito de esta actividad es fomentar habilidades prácticas en la programación de algoritmos con arreglos para abordar problemas típicos de búsqueda y ordenamiento. Se han implementado algoritmos básicos en Python para encontrar elementos específicos y ordenar datos. La comparación entre estos métodos permite analizar su eficiencia en distintos contextos.

2. Problemas abordados
Búsqueda del Elemento Mayor y Menor en un Arreglo: Se creó un algoritmo para localizar los valores máximo y mínimo dentro de un arreglo, útil para identificar rápidamente los límites en un conjunto de datos.
* Ordenación de un Arreglo: Para ordenar los elementos dentro de un arreglo, se implementaron dos algoritmos fundamentales:
* Bubble Sort: Algoritmo que recorre y compara repetidamente elementos adyacentes del arreglo hasta que se logra el orden adecuado.
* Selection Sort: Algoritmo que, en cada iteración, selecciona el elemento mínimo de la parte no ordenada y lo intercambia con el primer elemento de esa sección.
  
3. Implementación de los Algoritmos
Se seleccionó Python como lenguaje de programación debido a su facilidad de uso y su estructura clara. Cada algoritmo está documentado en el código, con explicaciones paso a paso para mejorar la comprensión. Los algoritmos fueron desarrollados en funciones separadas, lo que facilita su comprensión y reutilización.

4. Código Implementado
* Búsqueda de Mayor y Menor: Utiliza las funciones max y min para encontrar los valores límite en un arreglo.
* Bubble Sort: Un algoritmo de ordenación básico que pasa repetidamente por el arreglo para ordenar elementos adyacentes.
* Ordenación de selección: Un algoritmo que selecciona el elemento mínimo y lo coloca en la posición correcta en cada iteración.
Se realizaron pruebas en diversos arreglos de datos para verificar la funcionalidad de los algoritmos. Los conjuntos de prueba incluían arreglos y ordenados, desordenados y con valores repetidos. Los resultados demostraron que ambos algoritmos ordenan correctamente, aunque presentan diferencias de eficiencia.

5. Observaciones y Reflexiones sobre la Eficiencia
* Bubble Sort: Este algoritmo es simple y fácil de implementar, pero resulta ineficiente cuando se aplica a arreglos de gran tamaño debido a su necesidad de realizar múltiples pasadas a través del conjunto de datos. El tiempo de ejecución aumenta exponencialmente a medida que crece el tamaño del arreglo. Esta característica limita considerablemente su uso en aplicaciones que involucran grandes volúmenes de datos, ya que cada incremento en el tamaño del arreglo genera un crecimiento cuadrático en el número de comparaciones y movimientos.
* Ordenación de selección: Aunque este algoritmo también presenta una complejidad temporal de, su enfoque en realizar menos intercambios lo hace ligeramente más eficiente en situaciones donde el costo de mover elementos es elevado. En lugar de realizar intercambios constantes durante cada pasada, Selection Sort selecciona el elemento mínimo de la sección no ordenada del arreglo y lo coloca en su posición definitiva en una sola operación por iteración. Esto permite una pequeña mejora en eficiencia en comparación con Bubble Sort, aunque sigue siendo limitado en su aplicación para grandes volúmenes de datos.
  
6. Análisis comparativo
La comparación entre ambos algoritmos muestra que Selection Sort puede ser más rápido en algunos casos debido a la menor cantidad de intercambios. Sin embargo, ambos son menos eficientes que algoritmos avanzados (como Quick Sort o Merge Sort) en grandes volúmenes de datos.

7. Desafíos Encontrados
Durante el desarrollo, uno de los mayores desafíos fue optimizar los algoritmos para reducir el número de intercambios y comparaciones. También fue fundamental realizar un análisis cuidadoso de los casos de prueba para asegurar la correcta funcionalidad en diferentes escenarios.

8. Conclusión
Los algoritmos de búsqueda y ordenación implementados resultan efectivos para resolver problemas simples de manipulación de arreglos. No obstante, en aplicaciones que manejan grandes volúmenes de datos, sería recomendable emplear algoritmos más avanzados. Esta actividad ha sido útil para fortalecer conocimientos fundamentales en programación y algoritmos.

