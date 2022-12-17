
import telebot
from telebot import types # для указание типов
import config

bot = telebot.TeleBot('5846722883:AAGq9GIjXuWa-wx8gXeq9giNyZ8AHpEXc8M')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот ориентированный на работу с закачиками от команды HakaTeam".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Рады приветствовать вас в боте от HakaTeam)")
    elif(message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Что мне сделать чтобы перейти к заказу")
        btn2 = types.KeyboardButton("Интересно узнать")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Что вас интересует?", reply_markup=markup)
    
    elif(message.text == "Что мне сделать чтобы перейти к заказу"):
        bot.send_message(message.chat.id, "Ваш запрос отправлен к менеджеру, ожидайте ответа")
    
    elif message.text == "Интересно узнать":
        bot.send_message(message.chat.id, text="вы очень внимательно смотрите презентацию, подробнее ее вам информации не найти")
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Ая яй, а для кого кнопочки я тут показываю")

bot.polling(none_stop=True)