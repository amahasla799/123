import telebot

TOKEN = '5152696792:AAFcyi0XKhr-Ma13TC3UvkPUEwsW6JUkJtg'
bot = telebot.TeleBot(TOKEN)
def echo_messages(*messages):

    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            text = m.text
            bot.send_message(chatid, text)
            bot.set_update_listener(echo_messages)

        bot.polling()
