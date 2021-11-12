import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import time
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

tk="1285685661:AAEE7UJdhVLkKANuxj3M0D8bpszyiQrQ8ec"
updater = Updater(token=tk, use_context=True)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
updater.idle()
