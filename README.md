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
    <img src="logo.png" alt="Logo" height="180">
    <br />
    <a href="https://github.com/andres-merino/notion-article-uploader/issues">Reportar un Problema</a>
  </p>
</div>

<!-- Cuerpo -->
## Sobre el Proyecto

Este proyecto permite automatizar el análisis de artículos científicos en formato PDF para extraer metadatos, ideas principales y citas mediante GPT, y registrar la información estructurada directamente en una base de datos de Notion.

Ofrece tres formas de uso:
- Desde un notebook de Jupyter
- Como script ejecutable desde terminal
- A través de un bot de Telegram privado

### Construido con

![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge) 
![Jupyter Badge](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=fff&style=for-the-badge)
![OpenAI Badge](https://img.shields.io/badge/OpenAI-412991?logo=openai&logoColor=fff&style=for-the-badge) 
![Notion Badge](https://img.shields.io/badge/Notion-000000?logo=notion&logoColor=fff&style=for-the-badge)
![Telegram Badge](https://img.shields.io/badge/Telegram-2CA5E0?logo=telegram&logoColor=fff&style=for-the-badge)

## Descripción

El sistema permite leer un archivo PDF, extraer su contenido textual, enviarlo a GPT para generar un resumen estructurado en formato JSON (título, autor, revista, año, tema, subtema, ideas principales y citas) y registrar toda esa información como una nueva entrada en Notion. 

El contenido se registra como:
- Propiedades estructuradas (título, año, autor, etc.)
- Contenido de página con ideas principales y citas textuales

### Contenido del Repositorio

- [`notion_uploader.ipynb`](/notion_uploader.ipynb): Notebook interactivo para desarrollo y pruebas.
- [`notion_article_uploader.py`](notion_article_uploader.py): Script de línea de comandos para uso desde terminal.
- [`bot_uploader.py`](/bot_uploader.py): Bot de Telegram para enviar archivos PDF y registrarlos directamente en Notion.
- [`requirements.txt`](/requirements.txt): Lista de dependencias necesarias para ejecutar el proyecto.

### Configuración (`keys.py`)

Antes de ejecutar el proyecto, crea un archivo llamado `keys.py` con el siguiente contenido:

```python
OPENAI_API_KEY = "..."      # Tu clave API de OpenAI
NOTION_TOKEN = "..."        # Token de integración de Notion
NOTION_DATABASE_ID = "..."  # ID de la base de datos de Notion
TELEGRAM_TOKEN = "..."      # Token del bot de Telegram
USUARIO_AUTORIZADO = "..."  # Tu ID personal de Telegram
```

### Uso desde terminal

```bash
python notion_article_uploader.py ruta/al/archivo.pdf
```

### Uso desde Telegram

Crea un bot privado, configura tu `BOT_TOKEN` y tu `USUARIO_AUTORIZADO` en `keys.py`, y ejecuta:

```bash
python bot_uploader.py
```

Solo tú podrás interactuar con el bot gracias al control de acceso por ID.

## Créditos

**Andrés Merino** ([aemerinot@gmail.com](mailto:aemerinot@gmail.com))

* Docente-Investigador en Pontificia Universidad Católica del Ecuador
* Fundador del [Proyecto Alephsub0](https://www.alephsub0.org/about/)

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
[linkedin-url-aemt]: https://www.linkedin.com/in/andrés-merino-010a9b12b/
