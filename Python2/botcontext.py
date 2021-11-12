import telegram, smtplib, ssl, internet, logging
from email.message import EmailMessage
from internet import nombres
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import ConversationHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
import time

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Email Part Beggining

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "11bbcontacto@gmail.com"
receiver_email = ["oblanco2805@gmail.com","osba_28@hotmail.com"] 
password = "messi10*"

tk="1285685661:AAEE7UJdhVLkKANuxj3M0D8bpszyiQrQ8ec"
updater = Updater(token=tk, use_context=True)
dispatcher = updater.dispatcher

TECNICO=1
LABOR=2
NODO=3
UBICACION=4

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def reporte(update,context):
	global nombres

	layout=[["R4","R5","R6"],["R7","R8","R9"],["R16","R18","R19"]]
	keyb=ReplyKeyboardMarkup(layout, one_time_keyboard=True)
	update.message.reply_text("Ingrese el técnico que reporta", reply_markup=keyb)
	return TECNICO
	
def paso1(update, context):
	context.user_data['tecnico']= update.message.text
	layout=[["Retensar C500","Reemplazar C500"],["Reemplazar Fuente de poder","Reemplazar amplificador"],["Inspeccionar"]]
	keyb=ReplyKeyboardMarkup(layout, one_time_keyboard=True)
	update.message.reply_text("Ingrese que trabajo se debe realizar.",reply_markup=keyb)
	return LABOR

def paso2(update, context):
	context.user_data['labor']= update.message.text
	update.message.reply_text("Especifique el nodo afectado")
	
	return NODO

def paso3(update, context):
	context.user_data['nodo']= update.message.text
	update.message.reply_text("""Describa el trabajo a realizar y dé la ubicación exacta. 
	Recuerde especificar tipo de troncal, metros de cable y numero de postes""")
	
	return UBICACION

def paso4(update, context):
	context.user_data['ubicacion']= update.message.text
	
	msg = """Esta es la información que tengo.

	tecnico:{}
	labor:{}
	nodo:{}
	descripción:{}""".format(
		context.user_data['tecnico'], 
		context.user_data['labor'],
		context.user_data['nodo'], 
		context.user_data['ubicacion']
		)

	update.message.reply_text(msg)

	
	text="Según técnico {}, se amerita {}".format(nombres[context.user_data["tecnico"]],context.user_data['ubicacion'])
	k = EmailMessage()
	k.set_content(text)

	k['Subject'] = "{} en {}".format(context.user_data['labor'], context.user_data['nodo'])
	k['From'] = sender_email
	k['To'] = receiver_email

	contexto = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=contexto) as server:
		server.login(sender_email, password)
		server.send_message(k)

	update.message.reply_text("Correo enviado")

	#mensaje= """Subject: {} en {}

	#Según técnico {},{}""".format(data['labor'], data['nodo'], nombres[data["tecnico"]], data['ubicacion'])

	#m=mensaje.encode("ascii","ignore")

	#contexto = ssl.create_default_context()
	#with smtplib.SMTP_SSL(smtp_server, port, context=contexto) as server:
	#	server.login(sender_email, password)
	#	server.sendmail(sender_email, receiver_email, m)

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
		NODO: [
			CommandHandler('cancel', cancel),
			MessageHandler(Filters.text, paso3)
		],
		UBICACION: [
			CommandHandler('cancel', cancel),
			MessageHandler(Filters.text, paso4)
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
