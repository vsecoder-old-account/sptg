import telebot
bot = telebot.TeleBot('1300559351:AAHDX-SwceDVua-M6xymezPgtOCUdwVFfTY')
i = 0
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Что не понятно? Пришешь мне сообщение и ждёшь ответа!")
    elif message.text == "/start":
        bot.send_message(message.chat.id, "Привет, я <i>бот для связи</i> с <b>Всеволодом html</b>, все <u>твои сообщения</u> написаные ниже будут отравляться ему!", parse_mode='html')
    elif message.text == "/id":
        bot.send_message(message.chat.id, message.from_user.id)
    elif message.text == "/go":
    	if message.from_user.id == 1218845111:
    		bot.send_message(message.chat.id, "123")
    	else:
    		bot.send_message(message.chat.id, "У вас нету доступа к этой команде!")
    else:
    	if i < 10:
        	bot.send_message(1218845111, message)
        	print(message)
        	global i
        else:
        	bot.send_message(message.chat.id, "Отдохни друг)))")
        i = i + 1

bot.polling(none_stop=True, interval=0)
