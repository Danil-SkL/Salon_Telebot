import telebot
from telebot import types

bot=telebot.TeleBot('6161122528:AAH_eLRXntIk2eRjHnYNTNBdIXZfDnRHRmk')

#главное меню
markup = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton('О нашем салоне', callback_data='id_us')
item2 = types.InlineKeyboardButton('Список услуг', callback_data='id_service')
item3 = types.InlineKeyboardButton('Акции', callback_data='id_sale')
item4 = types.InlineKeyboardButton('Мы находимся', callback_data='id_map')
item5 = types.InlineKeyboardButton('Наши контакты', callback_data='id_call')
markup.add(item1, item2, item3, item4, item5)

#Вернутся в меню
markup1 = types.InlineKeyboardMarkup(row_width=1)
item6 = types.InlineKeyboardButton('Вернутся в меню', callback_data='id_back')
markup1.add(item6)

#Меню услуг
markup2 = types.InlineKeyboardMarkup(row_width=1)
item7 = types.InlineKeyboardButton('Прически', callback_data='id_pri')
item8 = types.InlineKeyboardButton('Мейкап', callback_data='id_Mc')
item9 = types.InlineKeyboardButton('Укладка', callback_data='id_Ukl')
item10 = types.InlineKeyboardButton('Массаж', callback_data='id_Mass')
markup2.add(item7, item8, item9, item10, item6)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Выберите пункт меню', reply_markup=markup)



@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'id_us':
            bot.send_message(call.message.chat.id, 'Этот салон красоты - идеальное место для тех, кто хочет почувствовать себя настоящей звездой. Здесь вы можете насладиться богатым выбором услуг, которые включают в себя стрижки, укладки, макияж и многое другое. Профессиональные стилисты и косметологи всегда готовы помочь вам стать еще красивее и увереннее в своей коже.')
            bot.send_message(call.message.chat.id, 'Спа-салон')
            bot.send_message(call.message.chat.id, 'Салон красоты', reply_markup=markup1)
        elif call.data == 'id_service':
            bot.send_message(call.message.chat.id, 'наши услуги.', reply_markup=markup2)
        elif call.data == 'id_sale':
            bot.send_message(call.message.chat.id, 'Наши акции', reply_markup=markup1)
        elif call.data == 'id_map':
            bot.send_message(call.message.chat.id, 'Мы находимся', reply_markup=markup1)
        elif call.data == 'id_call':
            bot.send_message(call.message.chat.id, 'Наши контакты', reply_markup=markup1)
        elif call.data == 'id_back':
            bot.send_message(call.message.chat.id, start(call.message))
        elif call.data == 'id_pri':
            bot.send_message(call.message.chat.id, 'Номер телефона для записи-89994442233')
            bot.send_message(call.message.chat.id, "Наша почта", reply_markup=markup1)

bot.polling(non_stop = True, interval=0)