# Asignaturas optativas del Grado en Inteligencia Artificial

Este es un repositorio que calcula distintos métodos de votación y métricas para comparar las distintas asignaturas optativas del Grado en Inteligencia Artificial de la [Universidad de Vigo](https://www.uvigo.gal/). Los datos han sido obtenidos con este [cuestionario](https://docs.google.com/forms/d/e/1FAIpQLSeHNeIP01vFKP7Y-J_DAL-7Cn0_YEE-8jA3jm2dRxvhtSVvgA/viewform?usp=dialog) que envía su información a esta [hoja de cálculo](https://docs.google.com/spreadsheets/d/1WvO5IBgJ3F6b6zHFQD5eWSxN-IUe3ONEvazHEUGb3Qo).

## Resumen estadístico

Estas son distintas métricas para todas las asignaturas, ordenadas por su media.

| <img width="1000"><br><p align="center">Asignatura | <img width="1000"><br><p align="center">Media | <img width="1000"><br><p align="center">Desviación típica | <img width="1000"><br><p align="center">Mediana | <img width="1000"><br><p align="center">Moda | <img width="1000"><br><p align="center">Máximo | <img width="1000"><br><p align="center">Mínimo | <img width="1000"><br><p align="center">Número de alumnos |
| :------------------------------------------------- | :-------------------------------------------: | :-------------------------------------------------------: | :---------------------------------------------: | :------------------------------------------: | :--------------------------------------------: | :--------------------------------------------: | --------------------------------------------------------: |
| Técnicas de Procedimiento Masivo de Datos          |                     7.97                      |                           0.84                            |                        8                        |                      8                       |                       10                       |                       7                        |                                                        14 |
| Bases de datos NoSQL                               |                     7.95                      |                           0.97                            |                        8                        |                      8                       |                       10                       |                       6                        |                                                        15 |
| Aprendizaje Automático Bio-inspirado               |                     7.77                      |                           1.98                            |                        8                        |                      10                      |                       10                       |                       4                        |                                                        15 |
| Dimensión Ética y Jurídica de la IA                |                     7.73                      |                           1.26                            |                        8                        |                      8                       |                       10                       |                       5                        |                                                        14 |
| Aprendizaje Automático I                           |                     7.49                      |                           1.19                            |                        8                        |                      8                       |                      9.6                       |                       5                        |                                                        15 |
| Sistemas Expertos                                  |                     7.49                      |                           1.23                            |                       7.5                       |                      7                       |                       9                        |                       5                        |                                                        15 |
| Sistemas Reactivos                                 |                     7.35                      |                           1.85                            |                        8                        |                      8                       |                       10                       |                       3                        |                                                        15 |
| Razonamiento con Incertidumbre                     |                     5.48                      |                           2.54                            |                       6.2                       |                      7                       |                       8                        |                       0                        |                                                        15 |
| Plataforma de Internet de las Cosas                |                     2.39                      |                             2                             |                        3                        |                      0                       |                       5                        |                       0                        |                                                        14 |
| Aprendizaje Automático II                          |                     1.68                      |                           1.78                            |                        1                        |                      0                       |                       5                        |                       0                        |                                                        15 |

## Distribuciones de probabilidad

Estas son las distribuciones de probabilidad de las notas para cada asignatura, normalizadas entre 0 y 10.

![Image](/images/distributions.png)

## [Distribuciones normales](https://en.wikipedia.org/wiki/Normal_distribution)

Estas son las distribuciones normales usando la media y desviación típica de cada asignatura.

![Image](/images/normalDistributions.png)

## [Método Schulze](https://en.wikipedia.org/wiki/Schulze_method)

Para el método Schulze se necesita un ranking de cada votante para todas las opciones. Como en este caso tenemos una nota numérica, se pone que un votante prefiere una asignatura sobre otra si le ha dado una nota mayor. Esto se divide por el número de alumnos que han votado a las dos asignaturas para normalizar.

| <img width="1000"><br><p align="center">Asignatura |
| :------------------------------------------------: |
|                Bases de datos NoSQL                |
|     Técnicas de Procedimiento Masivo de Datos      |
|        Aprendizaje Automático Bio-inspirado        |
|        Dimensión Ética y Jurídica de la IA         |
|              Aprendizaje Automático I              |
|                 Sistemas Expertos                  |
|                 Sistemas Reactivos                 |
|           Razonamiento con Incertidumbre           |
|        Plataforma de Internet de las Cosas         |
|             Aprendizaje Automático II              |
