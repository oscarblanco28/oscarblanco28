import telegram, smtplib, ssl
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import ConversationHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
import time

# Email Part Beggining

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "11bbcontacto@gmail.com"
receiver_email = "oblanco2805@gmail.com" 
password = "messi10*"

tk="1285685661:AAEE7UJdhVLkKANuxj3M0D8bpszyiQrQ8ec"
updater = Updater(token=tk, use_context=True)
dispatcher = updater.dispatcher

data= {'tecnico':"",'labor':"",'ubicacion':""}

TECNICO=1
LABOR=2
UBICACION=3

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def reporte(update,context):
	global data

	data= {'tecnico':"",'labor':"",'ubicacion':""}
	layout=[["R4","R5","R6"],["R7","R8","R9"],["R16","R18","R19"]]
	keyb=ReplyKeyboardMarkup(layout, one_time_keyboard=True)
	update.message.reply_text("Ingrese el técnico que reporta", reply_markup=keyb)
	return TECNICO
	
def paso1(update, context):
	data['tecnico']= update.message.text
	layout=[["Retensar C500","Reemplazar C500"],["Poner Fuente de poder","Poner amplificador"],["Inspeccionar"]]
	keyb=ReplyKeyboardMarkup(layout, one_time_keyboard=True)
	update.message.reply_text("Ingrese que trabajo se debe realizar",reply_markup=keyb)
	return LABOR

def paso2(update, context):
	data['labor']= update.message.text
	update.message.reply_text("Describa el trabajo a realizar y de una ubicación")
	
	return UBICACION

def paso3(update, context):
	data['ubicacion']= update.message.text
	
	msg = """I got all data

	tecnico:{}
	labor:{}
	ubicación:{}""".format(data['tecnico'], data['labor'], data['ubicacion'])

	update.message.reply_text(msg)

	mensaje= """Subject: Prueba de Python

	tecnico:{}
	labor:{}
	ubicación:{}""".format(data['tecnico'], data['labor'], data['ubicacion'])

	m=mensaje.encode("ascii","ignore")

	contexto = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=contexto) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, m)

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
print("Running... Presiona Ctrl+C para parar")
updater.idle()
print("Stoping...")
updater.stop()
