# Asignaturas optativas del Grado en Inteligencia Artificial 2026

Este es un repositorio que calcula distintos métodos de votación y métricas para comparar las distintas asignaturas optativas del Grado en Inteligencia Artificial de la [Universidad de Vigo](https://www.uvigo.gal/). Los datos han sido obtenidos con este [cuestionario](https://docs.google.com/forms/d/e/1FAIpQLSeHNeIP01vFKP7Y-J_DAL-7Cn0_YEE-8jA3jm2dRxvhtSVvgA/viewform?usp=dialog) que envía su información a esta [hoja de cálculo](https://docs.google.com/spreadsheets/d/1WvO5IBgJ3F6b6zHFQD5eWSxN-IUe3ONEvazHEUGb3Qo).

## Resumen estadístico

Estas son distintas métricas para todas las asignaturas, ordenadas por su media.

| <img width="1000"><br><p align="center">Asignatura | <img width="1000"><br><p align="center">Media | <img width="1000"><br><p align="center">Desviación típica | <img width="1000"><br><p align="center">Mediana | <img width="1000"><br><p align="center">Moda | <img width="1000"><br><p align="center">Máximo | <img width="1000"><br><p align="center">Mínimo | <img width="1000"><br><p align="center">Número de alumnos |
| :------------------------------------------------- | :-------------------------------------------: | :-------------------------------------------------------: | :---------------------------------------------: | :------------------------------------------: | :--------------------------------------------: | :--------------------------------------------: | --------------------------------------------------------: |
| Interfaces Inteligentes                            |                      9.5                      |                           0.71                            |                       9.5                       |                      9                       |                       10                       |                       9                        |                                                         2 |
| Aprendizaje Automático Bio-inspirado               |                       9                       |                            nan                            |                        9                        |                      9                       |                       9                        |                       9                        |                                                         1 |
| Visión Artificial                                  |                       8                       |                            nan                            |                        8                        |                      8                       |                       8                        |                       8                        |                                                         1 |
| Dimensión Ética y Jurídica de la IA                |                       8                       |                            nan                            |                        8                        |                      8                       |                       8                        |                       8                        |                                                         1 |
| Técnicas de Procedimiento Masivo de Datos          |                       8                       |                             0                             |                        8                        |                      8                       |                       8                        |                       8                        |                                                         2 |
| Sistemas Expertos                                  |                       8                       |                             0                             |                        8                        |                      8                       |                       8                        |                       8                        |                                                         2 |
| Bases de Datos NoSQL                               |                      7.5                      |                           0.71                            |                       7.5                       |                      7                       |                       8                        |                       7                        |                                                         2 |
| Procesamiento del Lenguaje Natural                 |                      7.5                      |                           0.71                            |                       7.5                       |                      7                       |                       8                        |                       7                        |                                                         2 |
| Aprendizaje Automático I                           |                       7                       |                           1.41                            |                        7                        |                      6                       |                       8                        |                       6                        |                                                         2 |
| Ciberseguridad Inteligente                         |                       7                       |                             0                             |                        7                        |                      7                       |                       7                        |                       7                        |                                                         2 |
| Sistemas Reactivos                                 |                       6                       |                           4.24                            |                        6                        |                      3                       |                       9                        |                       3                        |                                                         2 |
| Razonamiento con Incertidumbre                     |                       6                       |                           2.83                            |                        6                        |                      4                       |                       8                        |                       4                        |                                                         2 |
| Recuperación de la Información                     |                      5.5                      |                           3.54                            |                       5.5                       |                      3                       |                       8                        |                       3                        |                                                         2 |
| Web Semántica                                      |                      5.5                      |                           2.12                            |                       5.5                       |                      4                       |                       7                        |                       4                        |                                                         2 |
| Plataforma de Internet de las Cosas                |                       3                       |                            nan                            |                        3                        |                      3                       |                       3                        |                       3                        |                                                         1 |
| Aprendizaje Automático II                          |                       0                       |                            nan                            |                        0                        |                      0                       |                       0                        |                       0                        |                                                         1 |
| Sistemas basados en Agentes                        |                       0                       |                            nan                            |                        0                        |                      0                       |                       0                        |                       0                        |                                                         1 |

## Distribuciones de probabilidad

Estas son las distribuciones de probabilidad de las notas para cada asignatura, normalizadas entre 0 y 10.

![Image](./distributions2026.png)

## [Distribuciones normales](https://en.wikipedia.org/wiki/Normal_distribution)

Estas son las distribuciones normales usando la media y desviación típica de cada asignatura.

![Image](./normalDistributions2026.png)

## [Método Schulze](https://en.wikipedia.org/wiki/Schulze_method)

Para el método Schulze se necesita un ranking de cada votante para todas las opciones. Como en este caso tenemos una nota numérica, se pone que un votante prefiere una asignatura sobre otra si le ha dado una nota mayor. Esto se divide por el número de alumnos que han votado a las dos asignaturas para normalizar.

| <img width="1000"><br><p align="center">Asignatura |
| :------------------------------------------------: |
|              Interfaces Inteligentes               |
|        Aprendizaje Automático Bio-inspirado        |
|                 Visión Artificial                  |
|        Dimensión Ética y Jurídica de la IA         |
|     Técnicas de Procedimiento Masivo de Datos      |
|                 Sistemas Expertos                  |
|                Bases de Datos NoSQL                |
|         Procesamiento del Lenguaje Natural         |
|              Aprendizaje Automático I              |
|             Ciberseguridad Inteligente             |
|                 Sistemas Reactivos                 |
|           Razonamiento con Incertidumbre           |
|           Recuperación de la Información           |
|                   Web Semántica                    |
|        Plataforma de Internet de las Cosas         |
|             Aprendizaje Automático II              |
|            Sistemas basados en Agentes             |
