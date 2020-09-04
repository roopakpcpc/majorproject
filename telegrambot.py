x = "roopakpcpc"#io username
y = "aio_dnuT36QehOEfK6fRJBzP0Q8o2Q0t"# io key

!pip install python-telegram-bot
!pip install adafruit-io
from Adafruit_IO import Client, Feed, Data
aio = Client(x,y)

#sending a value to feed
from Adafruit_IO import Client, Feed, Data
#create feed
feed=Feed(name='bot') #feed name given
result=aio.create_feed(feed)

from telegram.ext import Updater, CommandHandler
import requests

def on(bot,update):
  value=Data(value=1)
  value_send=aio.create_data('bot',value)

def off(bot,update):
  value=Data(value=0)
  value_send=aio.create_data('bot',value)

u=Updater('1381707135:AAEyzALCkUUtx7fyKVFKQ9oD-HrVq8rCpIE')
dp=u.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
u.start_polling()
u.idle()
