import telebot;
from telebot import types
bot = telebot.TeleBot('5935726363:AAHEvS0SFXe5jGlPVZfZl-zpNLtWXhXBbQ8');



@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start' or message.text == 'Привет' or message.text == 'Ещё':
        bot.send_message(message.from_user.id, "Привет!");
        keyboard = types.InlineKeyboardMarkup(); 
        key_2022 = types.InlineKeyboardButton(text='2022', callback_data='2022'); 
        keyboard.add(key_2022); 
        key_2018= types.InlineKeyboardButton(text='2018', callback_data='2018');
        keyboard.add(key_2018);
        key_2014 = types.InlineKeyboardButton(text='2014', callback_data='2014'); 
        keyboard.add(key_2014); 
        key_2010= types.InlineKeyboardButton(text='2010', callback_data='2010');
        keyboard.add(key_2010);
        bot.send_message(message.from_user.id, text='Выберите год и бот покажет первые три места по фигурному катанию на Олимпийских играх выбранного года', reply_markup=keyboard)
        

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "2022":
        bot.send_message(call.message.chat.id, 'Женщины:\n1. Анна Щербакова, Россия\n2. Александра Трусова, Россия\n3. Каори Сакамото, Япония\n'
                                               'Мужчины:\n1. Нейтан Чен, США\n2. Юма Кагияма, Япония\n3. Сема Уно, Япония\n'
                                               'Пары:\n1. Вэньцзин Суй и Цун Хань, Китай\n2. Евгения Тарасова и Владимир Морозов, Россия\n3. Анастасия Мишина и Александр Галлямов, Россия\n'
                                               'Танцы на льду:\n1. Габриэла Пападакис и Гийом Сизерон, Франция\n2. Виктория Синицина и Никита Кацалапов, Россия\n3. Мэдисон Хаббелл и Закари Донохью, США');
    elif call.data == "2018":
        bot.send_message(call.message.chat.id, 'Женщины:\n1. Алина Загитова, Россия\n2. Евгения Медведева, Россия\n3. Кейтлин Осмонд, Канада\n'
                                               'Мужчины:\n1. Юдзуру Ханю, Япония\n2. Сема Уно, Япония\n3. Хавьер Фернандес, Испания\n'
                                               'Пары:\n1. Алёна Савченко и Бруно Массо, Германия\n2. Вэньцзин Суй и Цун Хань, Китай\n3. Меган Дюамель и Эрик Рэдфорд, Канада\n'
                                               'Танцы на льду:\n1. Тесса Вертью и Скотт Моир, Канада\n2. Габриэла Пападакис и Гийом Сизерон, Франция\n3. Майя и Алекс Шибутани, США');
    elif call.data == "2014":
        bot.send_message(call.message.chat.id, 'Женщины:\n1. Аделина Сотникова, Россия\n2. Ким Ён А, Южная Корея\n3. Каролина Костнер, Италия\n'
                                               'Мужчины:\n1. Юдзуру Ханю, Япония\n2. Патрик Чан, Канада\n3. Денис Тен, Казахстан\n'
                                               'Пары:\n1. Татьяна Волосожар и Максим Траньков, Россия\n2. Ксения Столбова и Фёдор Климов, Россия\n3. Алёна Савченко и Робин Шолковы, Германия\n'
                                               'Танцы на льду:\n1. Мерил Дэвис и Чарли Уайт, США\n2. Тесса Вертью и Скотт Моир, Канада\n3. Елена Ильиных и Никита Кацалапов, Россия');
    elif call.data == "2010":
        bot.send_message(call.message.chat.id, 'Женщины:\n1. Ким Ён А, Южная Корея\n2. Мао Асада, Япония\n3. Джоанни Рошетт, Канада\n'
                                                'Мужчины:\n1. Эван Лайсачек, США\n2. Евгений Плющенко, Россия\n3. Дайсукэ Такахаси, Япония\n'
                                               'Пары:\n1. Шэнь Сюэ и Чжао Хунбо, Китай\n2. Пан Цин и Тун Цзянь, Китай\n3. Алёна Савченко и Робин Шолковы, Германия\n'
                                               'Танцы на льду:\n1. Тесса Вертью и Скотт Моир, Канада\n2. Мерил Дэвис и Чарли Уайт, США\n3. Оксана Домнина и Максим Шабалин, Россия');
        
bot.polling(none_stop=True, interval=0)
