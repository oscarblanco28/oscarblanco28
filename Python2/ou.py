import telegram, smtplib, ssl, logging, csv
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from email.message import EmailMessage
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackContext
import re
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup

listo=[2,1]
v=["a","b","c"]
void=[]
c=[]
dicto={"jaguar":6,"mar":1,"sagre":7}

def inline(dictor):
	for key,value in dictor.items():
		x = InlineKeyboardButton(text=str(key),callback_data=int(value))
		void.append(x)
	else:
		return void

def makelist(a):
	for item in a:
		c.append(void[:item])
		del void[:item]
	else:
		return c

xx=inline(dictor)
xxx=makelist(listo)
print(xx)
print(xxx)

