import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
import time
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def reporte(update,context):
	layout=[["A","B"],["C","D"],["E"]]
	keyb=ReplyKeyboardMarkup(layout, one_time_keyboard=True)
	context.bot.send_message(chat_id=update.effective_chat.id, text="Selectone of the five options", reply_markup=keyb)

tk="1285685661:AAEE7UJdhVLkKANuxj3M0D8bpszyiQrQ8ec"
updater = Updater(token=tk, use_context=True)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
reporte_handler= CommandHandler("reporte", reporte)
dispatcher.add_handler(reporte_handler)
updater.start_polling(timeout=5)
updater.idle()
