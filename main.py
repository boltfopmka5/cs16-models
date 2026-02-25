import telebot

admin_id = 123123123 #ТВОЙ id
bot_token = '893587_AJIDijiij' #твой токен бота
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands = ['start'])
def strt(message):
    if message.from_user.id == int(admin_id):
        bot.send_message(message.from_user.id, "Бот работает и принимает сообщения!")
    else:
        bot.send_message(message.from_user.id, 'Здесь вы можете написать сообщение @твой_юз, если у вас спам-блок')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    try:
        if message.from_user.id != admin_id:
            msg = message.text
            bot.send_message(message.from_user.id, "Ваше сообщение отправлено!")
            bot.send_message(admin_id, f"Сообщение от @{message.from_user.username}\n{msg}")
        else:
            bot.send_message(admin_id, "Неизвестная команда!")