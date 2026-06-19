# Asignaturas optativas del Grado en Inteligencia Artificial 2026

Este es un repositorio que calcula distintos métodos de votación y métricas para comparar las distintas asignaturas optativas del Grado en Inteligencia Artificial de la [Universidad de Vigo](https://www.uvigo.gal/). Los datos han sido obtenidos con este [cuestionario](https://docs.google.com/forms/d/e/1FAIpQLSeHNeIP01vFKP7Y-J_DAL-7Cn0_YEE-8jA3jm2dRxvhtSVvgA/viewform?usp=dialog) que envía su información a esta [hoja de cálculo](https://docs.google.com/spreadsheets/d/1WvO5IBgJ3F6b6zHFQD5eWSxN-IUe3ONEvazHEUGb3Qo).

## Resumen estadístico

Estas son distintas métricas para todas las asignaturas, ordenadas por su media.

| <img width="1000"><br><p align="center">Asignatura  | <img width="1000"><br><p align="center">Media  | <img width="1000"><br><p align="center">Desviación típica  | <img width="1000"><br><p align="center">Mediana  | <img width="1000"><br><p align="center">Moda  | <img width="1000"><br><p align="center">Máximo  | <img width="1000"><br><p align="center">Mínimo  | <img width="1000"><br><p align="center">Número de alumnos |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|--:|
| IA en el ámbito Sanitario  | 10  | 0  | 10  | 10  | 10  | 10  | 2 |
| Aprendizaje Automático Bio-inspirado  | 9.6  | 0.57  | 9.6  | 9.2  | 10  | 9.2  | 2 |
| Minería de Textos  | 9.59  | 0.12  | 9.59  | 9.5  | 9.67  | 9.5  | 2 |
| Visión Artificial  | 9.22  | 0.54  | 9.22  | 8.83  | 9.6  | 8.83  | 2 |
| Técnicas de Procedimiento Masivo de Datos  | 9.16  | 0.23  | 9.16  | 9  | 9.33  | 9  | 2 |
| Bases de Datos NoSQL  | 9.16  | 0.23  | 9.16  | 9  | 9.33  | 9  | 2 |
| Dimensión Ética y Jurídica de la IA  | 9.12  | 0.16  | 9.12  | 9  | 9.23  | 9  | 2 |
| Procesamiento del Lenguaje Natural  | 8.64  | 0.21  | 8.64  | 8.5  | 8.79  | 8.5  | 2 |
| Razonamiento con Incertidumbre  | 7.86  | 0.52  | 7.86  | 7.5  | 8.23  | 7.5  | 2 |
| Aprendizaje Automático I  | 7.16  | 0.23  | 7.16  | 7  | 7.32  | 7  | 2 |
| Sistemas Expertos  | 7  | 0  | 7  | 7  | 7  | 7  | 2 |
| Web Semántica  | 6.9  | 0.14  | 6.9  | 6.8  | 7  | 6.8  | 2 |
| Sistemas Reactivos  | 6.75  | 0.35  | 6.75  | 6.5  | 7  | 6.5  | 2 |
| Recuperación de la Información  | 6.7  | 0  | 6.7  | 6.7  | 6.7  | 6.7  | 2 |
| Plataforma de Internet de las Cosas  | 3.16  | 0.23  | 3.16  | 3  | 3.33  | 3  | 2 |
| Aprendizaje Automático II  | 2.13  | 0.19  | 2.13  | 2  | 2.27  | 2  | 2 |
| Sistemas basados en Agentes  | 1.26  | 0.37  | 1.26  | 1  | 1.52  | 1  | 2 |
| Ciberseguridad Inteligente  | nan  | nan  | nan  | nan  | nan  | nan  | 0 |
| Interfaces Inteligentes  | nan  | nan  | nan  | nan  | nan  | nan  | 0 |
| IA en el ámbito Empresarial y Administrativo  | nan  | nan  | nan  | nan  | nan  | nan  | 0 |
| Robótica basada en el Comportamiento  | nan  | nan  | nan  | nan  | nan  | nan  | 0 |

## Distribuciones de probabilidad

Estas son las distribuciones de probabilidad de las notas para cada asignatura, normalizadas entre 0 y 10.

![Image](./distributions2026.png)

## [Distribuciones normales](https://en.wikipedia.org/wiki/Normal_distribution)

Estas son las distribuciones normales usando la media y desviación típica de cada asignatura.

![Image](./normalDistributions2026.png)

## [Método Schulze](https://en.wikipedia.org/wiki/Schulze_method)

Para el método Schulze se necesita un ranking de cada votante para todas las opciones. Como en este caso tenemos una nota numérica, se pone que un votante prefiere una asignatura sobre otra si le ha dado una nota mayor. Esto se divide por el número de alumnos que han votado a las dos asignaturas para normalizar.

| <img width="1000"><br><p align="center">Asignatura |
|:--:|
| IA en el ámbito Sanitario |
| Aprendizaje Automático Bio-inspirado |
| Minería de Textos |
| Visión Artificial |
| Técnicas de Procedimiento Masivo de Datos |
| Bases de Datos NoSQL |
| Dimensión Ética y Jurídica de la IA |
| Procesamiento del Lenguaje Natural |
| Razonamiento con Incertidumbre |
| Aprendizaje Automático I |
| Sistemas Expertos |
| Web Semántica |
| Sistemas Reactivos |
| Recuperación de la Información |
| Plataforma de Internet de las Cosas |
| Aprendizaje Automático II |
| Sistemas basados en Agentes |
| Ciberseguridad Inteligente |
| IA en el ámbito Empresarial y Administrativo |
| Interfaces Inteligentes |
| Robótica basada en el Comportamiento |
