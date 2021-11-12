import telegram, smtplib, ssl, internet
from internet import nombres
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CallbackQueryHandler, CallbackContext, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
import time
import logging

# Email Part Beggining

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "11bbcontacto@gmail.com"
receiver_email = ["oblanco2805@gmail.com","osba_28@hotmail.com"] 
password = "messi10*"

tk="1285685661:AAEE7UJdhVLkKANuxj3M0D8bpszyiQrQ8ec"
updater = Updater(token=tk, use_context=True)
dispatcher = updater.dispatcher

ohsi= {'tecnico':"",'labor':"",'nodo':"",'ubicacion':""}

TECNICO=1
LABOR=2
NODO=3
UBICACION=4

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def reporte(update,context: CallbackContext):
	global ohsi
	global nombres

	ohsi= {'tecnico':"",'labor':"",'nodo':"",'ubicacion':""}
	layout = [
        [
            InlineKeyboardButton("R5", callback_data='R5'),
            InlineKeyboardButton("R6", callback_data='R6'),
        ],
        [
        	InlineKeyboardButton("R7", callback_data='R7'),
        	InlineKeyboardButton("R8", callback_data='R8'),
        ],
        [
        	InlineKeyboardButton("R9", callback_data='R9'),
        	InlineKeyboardButton("R13", callback_data='R13'),
        ],
        [
        	InlineKeyboardButton("R16", callback_data='R16'),
        	InlineKeyboardButton("R19", callback_data='R19'),
        ]
    ]
	keyb=InlineKeyboardMarkup(layout)
	update.message.reply_text("Ingrese el técnico que reporta", reply_markup=keyb)

def gg(update, context: CallbackContext):
	ohsi['tecnico']= update.callback_query
	ohsi['tecnico'].answer()
	update.message.reply_text("Opción elegida: {}".format(ohsi['tecnico'].data))
	return TECNICO
	
def paso1(update, context):
	layout=[["Retensar C500","Reemplazar C500"],["Reemplazar Fuente de poder","Reemplazar amplificador"],["Inspeccionar"]]
	keyb=ReplyKeyboardMarkup(layout, one_time_keyboard=True)
	update.message.reply_text("Ingrese que trabajo se debe realizar",reply_markup=keyb)
	return LABOR

def paso2(update, context):
	ohsi['labor']= update.message.text
	update.message.reply_text("Especifique el nodo afectado")
	
	return NODO

def paso3(update, context):
	ohsi['nodo']= update.message.text
	update.message.reply_text("Describa el trabajo a realizar y dé la ubicación exacta")
	
	return UBICACION

def paso4(update, context):
	ohsi['ubicacion']= update.message.text
	
	msg = """I got all data

	tecnico:{}
	labor:{}
	nodo:{}
	ubicación:{}""".format(ohsi['tecnico'], ohsi['labor'],ohsi['nodo'], ohsi['ubicacion'])

	update.message.reply_text(msg)

	mensaje= """Subject: {} en {}

	Según técnico {},{}""".format(ohsi['labor'], ohsi['nodo'], nombres[ohsi["tecnico"]], ohsi['ubicacion'])

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
	per_chat=False,
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
updater.dispatcher.add_handler(CallbackQueryHandler(gg))
updater.start_polling(timeout=5, clean=True)
print("Running... Presiona Ctrl+C para parar")
updater.idle()
print("Stoping...")
updater.stop()
