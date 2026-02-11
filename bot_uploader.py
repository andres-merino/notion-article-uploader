import os
import telebot
from keys import TELEGRAM_TOKEN, USUARIO_AUTORIZADO
from notion_article_uploader import extraer_texto_desde_pdf, analizar_con_gpt, enviar_a_notion, crear_post_linkedin

# Inicializar bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# 📍 Restricción de acceso
def es_usuario_autorizado(message):
    return message.from_user.id == int(USUARIO_AUTORIZADO)

def acceso_restringido(func):
    def wrapper(message):
        if not es_usuario_autorizado(message):
            bot.reply_to(message, "⛔ No estás autorizado para usar este bot.")
            return
        return func(message)
    return wrapper

# /start
@bot.message_handler(commands=['start'])
@acceso_restringido
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 ¡Hola! Envíame un artículo en formato PDF para procesarlo."
    )

# Archivos PDF
@bot.message_handler(content_types=['document'])
@acceso_restringido
def handle_document(message):
    if not message.document.file_name.lower().endswith(".pdf"):
        bot.reply_to(message, "Por favor, envía un archivo PDF.")
        return

    bot.send_message(message.chat.id, "📥 Descargando y procesando el archivo...")

    # Descargar el archivo
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    ruta_pdf = f"datos/{message.document.file_name}"
    os.makedirs("datos", exist_ok=True)
    with open(ruta_pdf, 'wb') as new_file:
        new_file.write(downloaded_file)

    try:
        texto = extraer_texto_desde_pdf(ruta_pdf)
        json_data = analizar_con_gpt(texto)
        enviar_a_notion(json_data)
        post_linkedin = crear_post_linkedin(json_data)
        bot.send_message(message.chat.id, "✅ Artículo procesado y enviado a Notion.")
        bot.send_message(message.chat.id, "🔗 Post de LinkedIn generado:\n\n" + post_linkedin)
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Ocurrió un error: {str(e)}")

# Fallback: otros mensajes
@bot.message_handler(func=lambda message: True)
def fallback(message):
    if not es_usuario_autorizado(message):
        return
    bot.reply_to(message, "Por favor, envía un archivo PDF.")

# Iniciar el bot
if __name__ == "__main__":
    print("🤖 Bot en ejecución...")
    bot.polling()
