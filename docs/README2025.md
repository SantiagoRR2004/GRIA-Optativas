# Asignaturas optativas del Grado en Inteligencia Artificial 2025

Este es un repositorio que calcula distintos métodos de votación y métricas para comparar las distintas asignaturas optativas del Grado en Inteligencia Artificial de la [Universidad de Vigo](https://www.uvigo.gal/). Los datos han sido obtenidos con este [cuestionario](https://docs.google.com/forms/d/e/1FAIpQLSeHNeIP01vFKP7Y-J_DAL-7Cn0_YEE-8jA3jm2dRxvhtSVvgA/viewform?usp=dialog) que envía su información a esta [hoja de cálculo](https://docs.google.com/spreadsheets/d/1WvO5IBgJ3F6b6zHFQD5eWSxN-IUe3ONEvazHEUGb3Qo).

## Resumen estadístico

Estas son distintas métricas para todas las asignaturas, ordenadas por su media.

| <img width="1000"><br><p align="center">Asignatura  | <img width="1000"><br><p align="center">Media  | <img width="1000"><br><p align="center">Desviación típica  | <img width="1000"><br><p align="center">Mediana  | <img width="1000"><br><p align="center">Moda  | <img width="1000"><br><p align="center">Máximo  | <img width="1000"><br><p align="center">Mínimo  | <img width="1000"><br><p align="center">Número de alumnos |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|--:|
| Interfaces Inteligentes  | 9.67  | 0.58  | 10  | 10  | 10  | 9  | 3 |
| Minería de Textos  | 9.1  | 0.85  | 9  | 8.3  | 10  | 8.3  | 3 |
| Robótica basada en el Comportamiento  | 8.5  | nan  | 8.5  | 8.5  | 8.5  | 8.5  | 1 |
| Visión Artificial  | 8.24  | 0.86  | 8  | 8  | 9.9  | 7  | 8 |
| Técnicas de Procedimiento Masivo de Datos  | 8.16  | 0.72  | 8  | 8  | 10  | 7  | 16 |
| Bases de Datos NoSQL  | 7.99  | 0.92  | 8  | 8  | 10  | 6  | 17 |
| Aprendizaje Automático Bio-inspirado  | 7.91  | 2  | 9  | 9  | 10  | 4  | 15 |
| Ciberseguridad Inteligente  | 7.73  | 0.97  | 7  | 7  | 9.1  | 7  | 7 |
| Dimensión Ética y Jurídica de la IA  | 7.7  | 1.3  | 8  | 8  | 10  | 5  | 16 |
| Sistemas Expertos  | 7.61  | 1.16  | 8  | 8  | 9  | 5  | 17 |
| Procesamiento del Lenguaje Natural  | 7.55  | 1.29  | 7  | 7  | 10  | 6  | 11 |
| Aprendizaje Automático I  | 7.3  | 1.19  | 7.25  | 8  | 9.6  | 5  | 18 |
| Sistemas Reactivos  | 6.99  | 2.12  | 7.15  | 6  | 10  | 3  | 16 |
| Recuperación de la Información  | 6.12  | 1.81  | 7  | 7  | 8  | 3  | 12 |
| Razonamiento con Incertidumbre  | 5.54  | 2.53  | 6.1  | 7  | 9  | 0  | 18 |
| Web Semántica  | 5.3  | 2.31  | 6  | 7  | 8  | 1  | 10 |
| IA en el ámbito Sanitario  | 5  | nan  | 5  | 5  | 5  | 5  | 1 |
| Plataforma de Internet de las Cosas  | 2.73  | 2.06  | 3  | 3  | 6.5  | 0  | 15 |
| Aprendizaje Automático II  | 2.19  | 2.42  | 2  | 0  | 9  | 0  | 17 |
| Sistemas basados en Agentes  | 1.09  | 1.38  | 1  | 0  | 4  | 0  | 11 |
| IA en el ámbito Empresarial y Administrativo  | nan  | nan  | nan  | nan  | nan  | nan  | 0 |

## Distribuciones de probabilidad

Estas son las distribuciones de probabilidad de las notas para cada asignatura, normalizadas entre 0 y 10.

![Image](./distributions2025.png)

## [Distribuciones normales](https://en.wikipedia.org/wiki/Normal_distribution)

Estas son las distribuciones normales usando la media y desviación típica de cada asignatura.

![Image](./normalDistributions2025.png)

## [Método Schulze](https://en.wikipedia.org/wiki/Schulze_method)

Para el método Schulze se necesita un ranking de cada votante para todas las opciones. Como en este caso tenemos una nota numérica, se pone que un votante prefiere una asignatura sobre otra si le ha dado una nota mayor. Esto se divide por el número de alumnos que han votado a las dos asignaturas para normalizar.

| <img width="1000"><br><p align="center">Asignatura |
|:--:|
| Interfaces Inteligentes |
| Aprendizaje Automático Bio-inspirado |
| Robótica basada en el Comportamiento |
| Técnicas de Procedimiento Masivo de Datos |
| Visión Artificial |
| Ciberseguridad Inteligente |
| Minería de Textos |
| Bases de Datos NoSQL |
| Dimensión Ética y Jurídica de la IA |
| Sistemas Expertos |
| Aprendizaje Automático I |
| Procesamiento del Lenguaje Natural |
| Sistemas Reactivos |
| IA en el ámbito Sanitario |
| Recuperación de la Información |
| Razonamiento con Incertidumbre |
| Web Semántica |
| Plataforma de Internet de las Cosas |
| Aprendizaje Automático II |
| Sistemas basados en Agentes |
| IA en el ámbito Empresarial y Administrativo |
