# Análisis de Intersecciones en Open Travel Areas (OTAs)

## Descripción del Problema

Este proyecto ofrece una solución para clasificar intersecciones (puntos) con respecto a su ubicación relativa a un conjunto de Open Travel Areas (OTAs) en un plano cartesiano bidimensional.

### Definiciones

- **OTA (Open Travel Area)**: Un rectángulo en un plano cartesiano, representado por una 4-tupla `(x_izquierda, x_derecha, y_inferior, y_superior)`.
- **Intersección**: Un punto en el plano cartesiano, representado por una coordenada `(x, y)`.

### Objetivo

Para cada intersección, determinar su relación con las OTAs existentes, clasificándola como:

- **Tipo 0**: No se encuentra dentro de ninguna OTA
- **Tipo 1**: Se encuentra en el borde de una OTA
- **Tipo 2**: Se encuentra en el borde de 2 OTAs que se intersectan entre sí
- **Tipo 3**: Está dentro de alguna OTA (no en el borde)

Además, para cada intersección, se deben identificar las OTAs relacionadas:
- Para tipos 1 y 3: La OTA correspondiente
- Para tipo 2: Las 2 OTAs correspondientes

### Enfoque Adoptado

Para mejorar la robustez del análisis, se implementó un algoritmo que:

1. Para cada intersección, determina su relación con cada OTA individualmente (dentro, borde o fuera)
2. Clasifica la intersección según los resultados acumulados
3. Reporta todas las OTAs relevantes para la intersección

Este enfoque permite manejar casos complejos como:
- Intersecciones dentro de múltiples OTAs anidadas
- Puntos en el borde de 3 o más OTAs
- Configuraciones donde la clasificación simple no captura adecuadamente la realidad geométrica

## Estructura de Datos

### Entrada

- **OTAs**: Un diccionario (o mapa hash) donde:
  - **Clave**: Nombre de la OTA
  - **Valor**: Lista/arreglo `[x_izquierda, x_derecha, y_inferior, y_superior]`

- **Intersecciones**: Un diccionario donde:
  - **Clave**: Nombre de la intersección
  - **Valor**: Lista/arreglo `[x, y]`

### Salida

Un diccionario de resultados donde:
- **Clave**: Nombre de la intersección
- **Valor**: Un diccionario que contiene:
  - **tipo**: Clasificación (0, 1, 2, o 3)
  - **otas**: Lista de OTAs relevantes

## Notas Adicionales

- El algoritmo es capaz de manejar casos donde una intersección se encuentra dentro de más de una OTA o en el borde de más de 2 OTAs, reportando todas las OTAs involucradas.
- Para situaciones complejas, la salida proporciona información detallada sobre la relación de cada intersección con cada OTA relevante.
