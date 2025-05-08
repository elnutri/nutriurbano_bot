
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "AQUÍ PONES TU TOKEN REAL"

def start(update, context):
    update.message.reply_text("¡Klk! Soy el Nutricionista Urbano Bot. Pregúntame lo que quieras.")

def help_command(update, context):
    update.message.reply_text("Puedo ayudarte con tus dudas de nutrición. Solo escribe tu pregunta.")

def handle_message(update, context):
    text = update.message.text
    response = f"No cojas esa... pero te escucho: {text}"
    update.message.reply_text(response)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
