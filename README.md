# Taller de Resolución de Problemas - Grupo A: Probabilidad de Fallo y Domain Learning

## Contexto Académico
* **Programa:** Magíster en Simulación Computacional, Pontificia Universidad Católica de Valparaíso (PUCV).
* **Asignatura:** Taller de Resolución de Problemas.
* **Profesor:** Juan M. Cárdenas.

## Equipo de Trabajo (Grupo A)
* Gabriela Oyarzo
* Thomas Aguayo
* Victor Donoso
* Matías Cáceres

## Descripción del Proyecto
Este repositorio contiene la implementación en Python de un algoritmo iterativo de *Domain Learning* para la estimación de la probabilidad de fallo en eventos raros o extremos. 

Dado que evaluar la función de estado límite real ($g(y)$) en todo el dominio suele ser computacionalmente costoso, el algoritmo construye modelos sustitutos (*surrogate models*) que se enfocan únicamente en el dominio de interés. Para esto, se comparan dos estrategias de muestreo:
1. **Christoffel Sampling (CS):** Aproximación mediante *Weighted Least-Squares* (Mínimos Cuadrados Ponderados).
2. **Monte Carlo (MC):** Aproximación mediante *Least-Squares* estándar con una medida de probabilidad uniforme.

## Flujo del Algoritmo
El código ejecuta un proceso iterativo donde cada ciclo consta de 5 pasos fundamentales:
1. Construcción de la medida de probabilidad (CS y MC) sobre el dominio.
2. Muestreo de $m$ puntos y filtrado según la condición del dominio de interés ($Q(g(x))=1$).
3. Construcción de la aproximación $\tilde{g}_l$ usando los puntos muestreados.
4. Identificación del dominio de interés aproximado $Z_l$ en toda la malla.
5. Cálculo de la probabilidad de fallo, error relativo ($E_l$) y *volume mismatch* ($V_l$).

## Requisitos y Dependencias
El proyecto requiere las siguientes librerías estándar de computación científica en Python:
* `numpy`
* `matplotlib` (incluyendo `mpl_toolkits.mplot3d` para visualización)
