# Asignaturas optativas del Grado en Inteligencia Artificial

Este es un repositorio que calcula distintos métodos de votación y métricas para comparar las distintas asignaturas optativas del Grado en Inteligencia Artificial de la [Universidad de Vigo](https://www.uvigo.gal/). Los datos han sido obtenidos con este [cuestionario](https://docs.google.com/forms/d/e/1FAIpQLSeHNeIP01vFKP7Y-J_DAL-7Cn0_YEE-8jA3jm2dRxvhtSVvgA/viewform?usp=dialog) que envía su información a esta [hoja de cálculo](https://docs.google.com/spreadsheets/d/1WvO5IBgJ3F6b6zHFQD5eWSxN-IUe3ONEvazHEUGb3Qo).

## Resumen estadístico

Estas son distintas métricas para todas las asignaturas, ordenadas por su media.

| <img width="1000"><br><p align="center">Asignatura | <img width="1000"><br><p align="center">Media | <img width="1000"><br><p align="center">Desviación típica | <img width="1000"><br><p align="center">Mediana | <img width="1000"><br><p align="center">Moda | <img width="1000"><br><p align="center">Máximo | <img width="1000"><br><p align="center">Mínimo | <img width="1000"><br><p align="center">Número de alumnos |
| :------------------------------------------------- | :-------------------------------------------: | :-------------------------------------------------------: | :---------------------------------------------: | :------------------------------------------: | :--------------------------------------------: | :--------------------------------------------: | --------------------------------------------------------: |
| Interfaces Inteligentes                            |                      9.5                      |                           0.71                            |                       9.5                       |                      9                       |                       10                       |                       9                        |                                                         2 |
| Visión Artificial                                  |                     8.27                      |                           0.92                            |                        8                        |                      8                       |                      9.9                       |                       7                        |                                                         7 |
| Técnicas de Procedimiento Masivo de Datos          |                     8.11                      |                           0.71                            |                        8                        |                      8                       |                       10                       |                       7                        |                                                        15 |
| Bases de Datos NoSQL                               |                     7.96                      |                           0.94                            |                        8                        |                      8                       |                       10                       |                       6                        |                                                        16 |
| Aprendizaje Automático Bio-inspirado               |                     7.91                      |                             2                             |                        9                        |                      9                       |                       10                       |                       4                        |                                                        15 |
| Dimensión Ética y Jurídica de la IA                |                      7.8                      |                           1.31                            |                        8                        |                      8                       |                       10                       |                       5                        |                                                        14 |
| Procesamiento del Lenguaje Natural                 |                     7.78                      |                            1.3                            |                        7                        |                      7                       |                       10                       |                       6                        |                                                         9 |
| Ciberseguridad Inteligente                         |                     7.73                      |                           0.97                            |                        7                        |                      7                       |                      9.1                       |                       7                        |                                                         7 |
| Sistemas Expertos                                  |                     7.59                      |                           1.19                            |                        8                        |                      8                       |                       9                        |                       5                        |                                                        16 |
| Aprendizaje Automático I                           |                     7.37                      |                           1.18                            |                       7.5                       |                      8                       |                      9.6                       |                       5                        |                                                        17 |
| Sistemas Reactivos                                 |                     6.99                      |                           2.12                            |                      7.15                       |                      6                       |                       10                       |                       3                        |                                                        16 |
| Recuperación de la Información                     |                      6.1                      |                           1.91                            |                        7                        |                      7                       |                       8                        |                       3                        |                                                        10 |
| Razonamiento con Incertidumbre                     |                     5.45                      |                           2.58                            |                        6                        |                      7                       |                       9                        |                       0                        |                                                        17 |
| Web Semántica                                      |                     5.33                      |                           2.45                            |                        6                        |                      7                       |                       8                        |                       1                        |                                                         9 |
| Plataforma de Internet de las Cosas                |                     2.46                      |                           1.84                            |                        3                        |                      3                       |                       5                        |                       0                        |                                                        14 |
| Aprendizaje Automático II                          |                     2.08                      |                           2.45                            |                       1.5                       |                      0                       |                       9                        |                       0                        |                                                        16 |
| Sistemas basados en Agentes                        |                       1                       |                           1.32                            |                        1                        |                      0                       |                       4                        |                       0                        |                                                         9 |

## Distribuciones de probabilidad

Estas son las distribuciones de probabilidad de las notas para cada asignatura, normalizadas entre 0 y 10.

![Image](./docs/distributions.png)

## [Distribuciones normales](https://en.wikipedia.org/wiki/Normal_distribution)

Estas son las distribuciones normales usando la media y desviación típica de cada asignatura.

![Image](./docs/normalDistributions.png)

## [Método Schulze](https://en.wikipedia.org/wiki/Schulze_method)

Para el método Schulze se necesita un ranking de cada votante para todas las opciones. Como en este caso tenemos una nota numérica, se pone que un votante prefiere una asignatura sobre otra si le ha dado una nota mayor. Esto se divide por el número de alumnos que han votado a las dos asignaturas para normalizar.

| <img width="1000"><br><p align="center">Asignatura |
| :------------------------------------------------: |
|              Interfaces Inteligentes               |
|        Aprendizaje Automático Bio-inspirado        |
|     Técnicas de Procedimiento Masivo de Datos      |
|                Bases de Datos NoSQL                |
|                 Visión Artificial                  |
|             Ciberseguridad Inteligente             |
|        Dimensión Ética y Jurídica de la IA         |
|                 Sistemas Expertos                  |
|         Procesamiento del Lenguaje Natural         |
|              Aprendizaje Automático I              |
|                 Sistemas Reactivos                 |
|           Recuperación de la Información           |
|           Razonamiento con Incertidumbre           |
|                   Web Semántica                    |
|        Plataforma de Internet de las Cosas         |
|             Aprendizaje Automático II              |
|            Sistemas basados en Agentes             |
