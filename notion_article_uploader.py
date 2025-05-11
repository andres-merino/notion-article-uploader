import fitz
from openai import OpenAI
from notion_client import Client
from keys import OPENAI_API_KEY, NOTION_TOKEN, NOTION_DATABASE_ID
import sys

client = OpenAI(api_key=OPENAI_API_KEY)
notion = Client(auth=NOTION_TOKEN)

def extraer_texto_desde_pdf(ruta_pdf):
    texto = ""
    with fitz.open(ruta_pdf) as doc:
        for pagina in doc:
            texto += pagina.get_text()
    return texto

def analizar_con_gpt(texto):
    prompt = """
Extrae la siguiente información del texto de un artículo académico:

- Título
- Autor principal
- Revista
- Año
- Tema (un tema como: Educación, Matemática, Ciencia de Datos, etc.)
- Subtema (un subtema, máximo 2 palabras)
- Dos ideas principales
- Tres citas textuales

Devuelve un JSON con la estructura:
{
  "titulo": "...",
  "autor_principal": "...",
  "revista": "...",
  "año": ...,
  "tema": ["..."],
  "subtema": ["..."],
  "ideas_principales": ["..."],
  "citas_textuales": ["..."]
}

Texto:
""" + texto
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={ "type": "json_object" },
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return eval(response.choices[0].message.content)

def enviar_a_notion(datos):
    propiedades = {
        "Título": {"title": [{"text": {"content": datos["titulo"]}}]},
        "Autor principal": {"rich_text": [{"text": {"content": datos["autor_principal"]}}]},
        "Revista": {"rich_text": [{"text": {"content": datos["revista"]}}]},
        "Año": {"number": int(datos["año"])},
        "Lectura": {"select": {"name": "Completa"}},
        "Tema": {"multi_select": [{"name": t.strip()} for t in datos["tema"]]},
        "Subtema": {"multi_select": [{"name": s.strip()} for s in datos["subtema"]]}
    }

    children = []

    if datos["ideas_principales"]:
        children.append({
            "object": "block",
            "type": "heading_2",
            "heading_2": {"rich_text": [{"text": {"content": "Ideas principales"}}]}
        })
        for idea in datos["ideas_principales"]:
            children.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {"rich_text": [{"text": {"content": idea}}]}
            })

    if datos["citas_textuales"]:
        children.append({
            "object": "block",
            "type": "heading_2",
            "heading_2": {"rich_text": [{"text": {"content": "Citas"}}]}
        })
        for cita in datos["citas_textuales"]:
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
