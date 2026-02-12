import fitz
from openai import OpenAI
from notion_client import Client
from keys import OPENAI_API_KEY, NOTION_TOKEN, NOTION_DATABASE_ID
import sys
from pydantic import BaseModel

client = OpenAI(api_key=OPENAI_API_KEY)
notion = Client(auth=NOTION_TOKEN)

def extraer_texto_desde_pdf(ruta_pdf):
    texto = ""
    with fitz.open(ruta_pdf) as doc:
        for pagina in doc:
            texto += pagina.get_text()
    return texto

class Articulo(BaseModel):
    titulo: str
    autor_principal: str
    revista: str
    año: int
    DOI: str
    tema: list[str]
    subtema: list[str]
    ideas_principales: list[str]
    citas_textuales: list[str]

def analizar_con_gpt(texto):
    prompt = """
Extrae la siguiente información del texto de un artículo académico:

- Título
- Autor principal
- Revista
- Año
- DOI
- Tema (un tema como: Educación, Matemática, Ciencia de Datos, etc.)
- Subtema (un subtema, máximo 2 palabras)
- Dos ideas principales
- Tres citas textuales

Texto:
""" + texto
    
    response = client.responses.parse(
        model="gpt-4o-mini",
        input=[{"role": "user", "content": prompt}],
        text_format = Articulo,
        temperature=0,
    )
    return response.output_parsed

def crear_post_linkedin(articulo):
    prompt = f"""Crea un post de LinkedIn para compartir un artículo académico. El post debe ser atractivo, profesional y tener un formato similar a este (no uses muchos adjetivos redundantes o innecesarios, sé directo y claro):
    ---
    📚 ¿Cómo integrar ChatGPT en una clase de programación? 🤖💻

    Te recomiendo el artículo «Título», de autor principal. Presenta...

    Tres aspectos clave del estudio:
    1️⃣ 
    2️⃣ 
    3️⃣ 

    👉 Accede al artículo completo aquí: DOI
    ---
    
    La información del artículo es la siguiente:
    - Título: {articulo.titulo}
    - Autor principal: {articulo.autor_principal}
    - Revista: {articulo.revista}
    - DOI: {articulo.DOI}
    - Ideas principales: {', '.join(articulo.ideas_principales)}
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.output_text

def enviar_a_notion(datos):
    propiedades = {
        "Título": {"title": [{"text": {"content": datos.titulo}}]},
        "Autor principal": {"rich_text": [{"text": {"content": datos.autor_principal}}]},
        "Revista": {"rich_text": [{"text": {"content": datos.revista}}]},
        "Año": {"number": int(datos.año)},
        "Lectura": {"select": {"name": "Completa"}},
        "Tema": {"multi_select": [{"name": t.strip()} for t in datos.tema]},
        "Subtema": {"multi_select": [{"name": s.strip()} for s in datos.subtema]}
    }

    children = []

    if datos.ideas_principales:
        children.append({
            "object": "block",
            "type": "heading_2",
            "heading_2": {"rich_text": [{"text": {"content": "Ideas principales"}}]}
        })
        for idea in datos.ideas_principales:
            children.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {"rich_text": [{"text": {"content": idea}}]}
            })

    if datos.citas_textuales:
        children.append({
            "object": "block",
            "type": "heading_2",
            "heading_2": {"rich_text": [{"text": {"content": "Citas"}}]}
        })
        for cita in datos.citas_textuales:
            children.append({
                "object": "block",
                "type": "quote",
                "quote": {"rich_text": [{"text": {"content": cita}}]}
            })

    notion.pages.create(
        parent={"database_id": NOTION_DATABASE_ID},
        properties=propiedades,
        children=children
    )
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python notion_uploader.py ruta/al/archivo.pdf")
        sys.exit(1)

    ruta_pdf = sys.argv[1]
    texto = extraer_texto_desde_pdf(ruta_pdf)
    datos = analizar_con_gpt(texto)
    enviar_a_notion(datos)
    print("Artículo procesado y enviado a Notion con éxito.")
