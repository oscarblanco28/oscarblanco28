import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import ConversationHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
import time
data= {'tecnico':"",'labor':"",'ubicacion':""}

TECNICO=1
LABOR=2
UBICACION=3

tk="1285685661:AAEE7UJdhVLkKANuxj3M0D8bpszyiQrQ8ec"
updater = Updater(token=tk, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def reporte(update,context):
	global data

	data= {'tecnico':"",'labor':"",'ubicacion':""}

	update.message.reply_text("Ingrese el técnico que reporta, el tipo de labor que se debe realizar y la ubicación en tres mensajes")
	return TECNICO
	
def paso1(update, context):
	update.message.reply_text("Ingrese el Técnico que reporta")
	layout=[["R4","R5","R6"],["R7","R8","R9"],["R11","R13","R16"]]
	keyb=ReplyKeyboardMarkup(layout, one_time_keyboard=True)
	context.bot.send_message(chat_id=update.effective_chat.id,text="Que labor de construcción se debe hacer",reply_markup=keyb)
	data['tecnico']= update.message.text
	return LABOR

def paso2(update, context):
	layout=[["Retensar 500","Reemplazar 500"],["Poner Fuente de poder","Poner amplificador"],["Inspeccionar"]]
	keyb=ReplyKeyboardMarkup(layout, one_time_keyboard=True)
	context.bot.send_message(chat_id=update.effective_chat.id, text="Describa la labor de construcción y la ubicación.", reply_markup=keyb)
	data['labor']= update.message.text
	return UBICACION

def paso3(update, context):
	data['ubicacion']= update.message.text
	
	msg = """I got all data

	tecnico:{}
	labor:{}
	ubicación:{}""".format(data['tecnico'], data['labor'], data['ubicacion'])

	update.message.reply_text(msg)
	return ConversationHandler.END

def cancel(update, context):
	update.message.reply_text('cancelado')
	return ConversationHandler.END

converse_handler= ConversationHandler(
	entry_points=[CommandHandler('reporte', reporte)],
	states={
		TECNICO: [
			CommandHandler('cancel', cancel),
			MessageHandler(Filters.text, paso1)
		],
		LABOR: [
			CommandHandler('cancel', cancel),
			MessageHandler(Filters.text, paso2)
		],
		UBICACION: [
			CommandHandler('cancel', cancel),
			MessageHandler(Filters.text, paso3)
		],
	},
	fallbacks=[CommandHandler('cancel', cancel)]
)

dispatcher.add_handler(converse_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling(timeout=5, clean=True)
print("Running")
updater.idle()
