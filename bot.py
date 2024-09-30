import telebot
import os
from telebot import types
from dotenv import load_dotenv 
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Информация о нашей юридической клинике')
    btn2 = types.KeyboardButton('Как записаться на приём')
    btn3 = types.KeyboardButton('Часто задаваемые вопросы')
    btn4 = types.KeyboardButton('Кто проводит консультации')
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    bot.send_message(message.from_user.id, "Вас приветствует бот юридической клиники Волжского филиала Волгоградского государственного университета! Чем я могу быть вам полезен?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Часто задаваемые вопросы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('1')#placeholder
        btn2 = types.KeyboardButton('2')#placeholder
        btn3 = types.KeyboardButton('3')#placeholder
        btn4 = types.KeyboardButton('Назад')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)
        markup.row(btn4)
        bot.send_message(message.from_user.id, 'Выберите интересующий вас вопрос.', reply_markup=markup)

    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Информация о нашей юридической клинике')
        btn2 = types.KeyboardButton('Как записаться на приём')
        btn3 = types.KeyboardButton('Часто задаваемые вопросы')
        btn4 = types.KeyboardButton('Кто проводит консультации')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        bot.send_message(message.from_user.id, "Вас приветствует бот юридической клиники Волжского филиала Волгоградского государственного университета! Чем я могу быть вам полезен?", reply_markup=markup)

    elif message.text == 'Информация о нашей юридической клинике':
        bot.send_message(message.from_user.id, 'В Волжском филиале ВолГУ функционирует Центр бесплатной юридической помощи Волгоградского регионального отделения Ассоциации юристов России (г. Волжский, улица 40 лет Победы, д. 11, каб. 1.16). \nОсновной целью клиники является формирование у обучающихся по юридической специальности практических навыков посредством оказания ими бесплатной юридической помощи гражданам и их общественным организациям.', parse_mode='Markdown')

    elif message.text == 'Как записаться на приём':
        bot.send_message(message.from_user.id, 'Записаться на приём можно следующими способами: \n1) Позвонив по телефону (8443) 51-55-17 или (8443) 51-53-00 с указанием контактных телефонов для оперативной обратной связи. \n2) Написав письмо по адресу электронной почты stud.cons@vgi.volsu.ru \nЮридическая клиника также проводит прием граждан в дистанционном формате в on-line режиме ежедневно.', parse_mode='Markdown')

    elif message.text == 'Кто проводит консультации':
        bot.send_message(message.from_user.id, 'Консультации проводят студенты, обучающиеся в ВФ ВолГУ по юридической специальности.', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0)
