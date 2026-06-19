# Asignaturas optativas del Grado en Inteligencia Artificial 

Este es un repositorio que calcula distintos métodos de votación y métricas para comparar las distintas asignaturas optativas del Grado en Inteligencia Artificial de la [Universidad de Vigo](https://www.uvigo.gal/). Los datos han sido obtenidos con este [cuestionario](https://docs.google.com/forms/d/e/1FAIpQLSeHNeIP01vFKP7Y-J_DAL-7Cn0_YEE-8jA3jm2dRxvhtSVvgA/viewform?usp=dialog) que envía su información a esta [hoja de cálculo](https://docs.google.com/spreadsheets/d/1WvO5IBgJ3F6b6zHFQD5eWSxN-IUe3ONEvazHEUGb3Qo).

## Resumen estadístico

Estas son distintas métricas para todas las asignaturas, ordenadas por su media.

| <img width="1000"><br><p align="center">Asignatura  | <img width="1000"><br><p align="center">Media  | <img width="1000"><br><p align="center">Desviación típica  | <img width="1000"><br><p align="center">Mediana  | <img width="1000"><br><p align="center">Moda  | <img width="1000"><br><p align="center">Máximo  | <img width="1000"><br><p align="center">Mínimo  | <img width="1000"><br><p align="center">Número de alumnos |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|--:|
| Interfaces Inteligentes  | 9.67  | 0.58  | 10  | 10  | 10  | 9  | 3 |
| Minería de Textos  | 9.29  | 0.66  | 9.5  | 8.3  | 10  | 8.3  | 5 |
| Robótica basada en el Comportamiento  | 8.5  | nan  | 8.5  | 8.5  | 8.5  | 8.5  | 1 |
| Visión Artificial  | 8.43  | 0.88  | 8  | 8  | 9.9  | 7  | 10 |
| IA en el ámbito Sanitario  | 8.33  | 2.89  | 10  | 10  | 10  | 5  | 3 |
| Técnicas de Procedimiento Masivo de Datos  | 8.27  | 0.75  | 8  | 8  | 10  | 7  | 18 |
| Aprendizaje Automático Bio-inspirado  | 8.11  | 1.95  | 9  | 10  | 10  | 4  | 17 |
| Bases de Datos NoSQL  | 8.11  | 0.94  | 8  | 8  | 10  | 6  | 19 |
| Dimensión Ética y Jurídica de la IA  | 7.86  | 1.3  | 8  | 8  | 10  | 5  | 18 |
| Ciberseguridad Inteligente  | 7.73  | 0.97  | 7  | 7  | 9.1  | 7  | 7 |
| Procesamiento del Lenguaje Natural  | 7.71  | 1.25  | 7  | 7  | 10  | 6  | 13 |
| Sistemas Expertos  | 7.55  | 1.11  | 8  | 8  | 9  | 5  | 19 |
| Aprendizaje Automático I  | 7.28  | 1.13  | 7.16  | 7  | 9.6  | 5  | 20 |
| Sistemas Reactivos  | 6.96  | 1.99  | 7  | 6  | 10  | 3  | 18 |
| Recuperación de la Información  | 6.21  | 1.68  | 6.85  | 7  | 8  | 3  | 14 |
| Razonamiento con Incertidumbre  | 5.77  | 2.5  | 6.6  | 7  | 9  | 0  | 20 |
| Web Semántica  | 5.57  | 2.18  | 6.4  | 7  | 8  | 1  | 12 |
| Plataforma de Internet de las Cosas  | 2.78  | 1.93  | 3  | 3  | 6.5  | 0  | 17 |
| Aprendizaje Automático II  | 2.19  | 2.28  | 2  | 0  | 9  | 0  | 19 |
| Sistemas basados en Agentes  | 1.12  | 1.26  | 1  | 0  | 4  | 0  | 13 |
| IA en el ámbito Empresarial y Administrativo  | nan  | nan  | nan  | nan  | nan  | nan  | 0 |

## Distribuciones de probabilidad

Estas son las distribuciones de probabilidad de las notas para cada asignatura, normalizadas entre 0 y 10.

![Image](./docs/distributions.png)

## [Distribuciones normales](https://en.wikipedia.org/wiki/Normal_distribution)

Estas son las distribuciones normales usando la media y desviación típica de cada asignatura.

![Image](./docs/normalDistributions.png)

## [Método Schulze](https://en.wikipedia.org/wiki/Schulze_method)

Para el método Schulze se necesita un ranking de cada votante para todas las opciones. Como en este caso tenemos una nota numérica, se pone que un votante prefiere una asignatura sobre otra si le ha dado una nota mayor. Esto se divide por el número de alumnos que han votado a las dos asignaturas para normalizar.

| <img width="1000"><br><p align="center">Asignatura |
|:--:|
| Interfaces Inteligentes |
| IA en el ámbito Sanitario |
| Aprendizaje Automático Bio-inspirado |
| Robótica basada en el Comportamiento |
| Minería de Textos |
| Técnicas de Procedimiento Masivo de Datos |
| Bases de Datos NoSQL |
| Visión Artificial |
| Ciberseguridad Inteligente |
| Dimensión Ética y Jurídica de la IA |
| Sistemas Expertos |
| Procesamiento del Lenguaje Natural |
| Aprendizaje Automático I |
| Sistemas Reactivos |
| Razonamiento con Incertidumbre |
| Recuperación de la Información |
| Web Semántica |
| Plataforma de Internet de las Cosas |
| Aprendizaje Automático II |
| Sistemas basados en Agentes |
| IA en el ámbito Empresarial y Administrativo |

## Informes por año

- ### [2026](./docs/README2026.md)

- ### [2025](./docs/README2025.md)
