import telegram, smtplib, ssl, logging, csv
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from email.message import EmailMessage
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackContext
import re
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup

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
fijador=r" ---> "
pizz={
	"Pizza pequeña":3.00,
	"Pizza mediana":4.00,
	"Pizza familiar":5.00
}
adic={
	"Borde de queso":0.5,
	"Peperonni":1.00,
	"Maíz":1.00,
	"Tocineta":1.00
}

o=[2,2]
void=[]
c=[]

def inline(dictor):
	for key,value in dictor.items():
		x = InlineKeyboardButton(text=str(key),callback_data=int(value))
		void.append(x)
	else:
		return void

ingr=inline(adic)

def makelist(a,b):
	for item in a:
		c.append(b[:item])
		del b[:item]
	else:
		return c

inlinek=makelist(o,ingr)

def start(update:Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Bienvenido al bot de Restaurante Fabiola. 
En este chat usted podra revisar el menú, los especiales del día y hacer sus pedidos!""")

def menu(update:Update, context: CallbackContext):
	file1=telegram.InputMediaPhoto(media="https://hot.granpulse.us/manga/Boku-No-Hero-Academia/0295-002.png", 
	caption="Esto es un tremendo album papu")
	file2=telegram.InputMediaPhoto(media="https://hot.granpulse.us/manga/Boku-No-Hero-Academia/0295-003.png")
	filelist=[file1,file2]
	context.bot.send_media_group(chat_id=update.effective_chat.id, media=filelist)

def order(update:Update, context: CallbackContext):
	context.bot.sendMessage(chat_id=update.effective_chat.id, text="""Seleccione los items que desea ordenar,
cuando finalice puede presionar el botón de /total para ver el total de la orden y confirmar su compra.""", 
reply_markup=InlineKeyboardMarkup(inlinek))

def ingrediente(update:Update, context: CallbackContext):
	query=update.callback_query
	query.answer()
	x=pizza.get(query)
	context.user_data["total"]=x
	query_data=query.data
	context.bot.sendMessage(text="Seleccione ingrediente/s para su {0}:\n\n{1}".format(query_data,mnsj,
reply_markup=inlinek))


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
menu_handler=CommandHandler('menu', menu)
dispatcher.add_handler(menu_handler)
order_handler=CommandHandler('order', order)
dispatcher.add_handler(order_handler)
updater.start_polling(timeout=5, clean=True)
print("Running... Presiona Ctrl+C para parar")
updater.idle()
print("Stoping...")
updater.stop()