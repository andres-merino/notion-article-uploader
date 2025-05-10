<!-- Encabezado -->
[![Colaboradores][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Estrellas][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- Título -->
<br />
<div align="center">

<h1 align="center">notion-article-uploader</h1>
  <p align="center">
    Automatiza la extracción desde archivos PDF de artículos científicos y su registro en una base de datos de Notion mediante GPT.
    <br />
    <a href="https://github.com/andres-merino/notion-article-uploader/issues">Reportar un Problema</a>
  </p>
</div>

<!-- Cuerpo -->
## Sobre el Proyecto

Este proyecto permite automatizar el análisis de artículos científicos en formato PDF para extraer metadatos e ideas principales mediante GPT y registrar la información estructurada directamente en una base de datos de Notion.

### Construido con

![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge) 
![Jupyter Badge](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=fff&style=for-the-badge)
![OpenAI Badge](https://img.shields.io/badge/OpenAI-412991?logo=openai&logoColor=fff&style=for-the-badge) 
![Notion Badge](https://img.shields.io/badge/Notion-000000?logo=notion&logoColor=fff&style=for-the-badge)


## Descripción

El sistema monitorea una carpeta local en busca de nuevos archivos PDF. Al detectar uno nuevo, lo procesa extrayendo texto, envía el contenido a GPT para obtener título, autor, revista, año, tema, subtema e ideas principales, y registra automáticamente los resultados en Notion.

### Contenido del Repositorio

- [`notion_uploader.ipynb`](/notion_uploader.ipynb): Notebook para desarrollo y pruebas.
- [`notion_uploader.py`](/notion_uploader.py): Script principal para monitoreo, extracción y carga en Notion.


## Créditos

**Andrés Merino** (aemerinot@gmail.com) 

- Docente-Investigador en Pontificia Universidad Católica del Ecuador  
- Fundador del [Proyecto Alephsub0](https://www.alephsub0.org/about/)

[![LinkedIn][linkedin-shield]][linkedin-url-aemt]

## Licencia

Distribuido bajo la licencia MIT.

[![MIT License][license-shield]][license-url]

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/andres-merino/notion-article-uploader.svg?style=for-the-badge
[contributors-url]: https://github.com/andres-merino/notion-article-uploader/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/andres-merino/notion-article-uploader.svg?style=for-the-badge
[forks-url]: https://github.com/andres-merino/notion-article-uploader/forks
[stars-shield]: https://img.shields.io/github/stars/andres-merino/notion-article-uploader?style=for-the-badge
[stars-url]: https://github.com/andres-merino/notion-article-uploader/stargazers
[issues-shield]: https://img.shields.io/github/issues/andres-merino/notion-article-uploader.svg?style=for-the-badge
[issues-url]: https://github.com/andres-merino/notion-article-uploader/issues
[license-shield]: https://img.shields.io/github/license/andres-merino/notion-article-uploader.svg?style=for-the-badge
[license-url]: https://es.wikipedia.org/wiki/Licencia_MIT
[linkedin-shield]: https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url-aemt]: https://www.linkedin.com/in/andrés-merino-010
