import telebot
from datetime import datetime
import time
import pytz

TOKEN = '6363495896:AAFYqi8fMpLzSX68Dfm5KIPTrB8__7_DUPg'
CHANNEL_ID = '-1001904846857'
START_DATE = datetime(2023, 4, 25)

bot = telebot.TeleBot(TOKEN)


def change_message():
  timezone = pytz.timezone('Europe/Moscow')
  current_date = datetime.now(timezone).date()
  days_passed = (current_date - START_DATE.date()).days + 1

  new_message = 'Сегодня ' + str(days_passed) + '-й день'

  try:
    bot.edit_message_text(chat_id=CHANNEL_ID, message_id=134, text=new_message)
  except telebot.apihelper.ApiTelegramException:
    pass

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Тест')
    change_message()


bot.polling(none_stop=True, interval=0)
