from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os, json, string
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
from database import Database
from config import API_TOKEN, ADMIN_ID1, ADMIN_ID2

#ТОКЕН БОТА
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

database = Database("database.db")


version = "1.4" ##НАПИШИ ВЕРСИЮ Пример : "1.0"


async def on_startup(_):
	print("Бот запущен!")


urlne = InlineKeyboardMarkup(row_width=1)
urlButtom = InlineKeyboardButton(text="🐳ИГРАТЬ🐳", url='https://prizes.gamee.com/game-bot/neonblast2-8b4d803a20090f438b6ba0fbcceb630d0eb8e76b#tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3D1kjkUtETi7uFhqc1JIvWkfXC_xOVj6rt_GQC30NnhTMqCcUVP_y7c95ewlA7xven')
urlne.add(urlButtom)

@dp.message_handler(commands=['get_id'])
async def get_id(message: types.Message):
    await message.answer(message.from_user.id)

###########   ОСНОВНАЯ ЧАСТЬ   #############

#ОПОВЕЩЕНИЕ О НОВОМ УЧАСТНИКЕ 
@dp.message_handler(content_types=["new_chat_members"])
async def handler_new_member(message):
    first_name = message.new_chat_members[0].first_name
    await bot.send_message(message.chat.id,str(message.new_chat_members[0].first_name) +'\nДобро пожаловать\n'+'в "True Семью" ученик ❗\n'+
	'Просим тебя ознакомиться с правилами группы и стараться их соблюдать! 👮\n'+'❓При возникновение вопросов❓обращаться к:\n'+"@hajimopedX\n@Svytaya_ec\n"+
	'Всегда будем рады удовлетворить ваше желание если оно не будет выходить за рамки нормы🍀\n'+'Приятного вам времени провождения 💫')


#ФИЛЬТР И КОМАНДЫ
@dp.message_handler()
async def echo_send(message : types.Message):
	if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
		.intersection(set(json.load(open('cenz.json')))) != set():
		database.add_mute(user_id=message.from_user.id, mute_time=600)
		await message.reply(f"🤬 Маты запрещены 🤬 \n@{message.from_user.username} Замучен на 10 минут❗")
		await message.delete()
	elif message.text == "/tixo" or message.text == "/tixo@TrueFamily_bot":
		if message.from_user.id == ADMIN_ID1 or message.from_user.id == ADMIN_ID2 or message.from_user.id == ADMIN_ID3:
			if not message.reply_to_message:
				await message.answer("😖 Команда должна быть ответом на сообщение 😖")
				return
			database.add_mute(user_id=message.reply_to_message.from_user.id, mute_time=0)
			await message.delete()
			await message.reply_to_message.reply(f"🥴 Пользователь @{message.reply_to_message.from_user.username} Размучен❗\n🦅 Кайфуй Молодой 🦅")
	elif message.text == "/pravila":
		await bot.send_message(message.chat.id,"🗓 правила чата:\nУчастники:\n1. ЛГБТ шутки мут 15 минут\n2. Оскорбление родителей и МАТ мут 10 минут\n3. Скидывать скрины с лс ботом сюда мут 1 час + варн\n4. Оскорбление участников в меру админ сам посчитает нужным мутить или нет, мут 20 минут\n5. Порнография бан на 24 часа\n6. Спам / Флуд, мут 10 минут\n\nМодераторы/Админы:\n1-6 пункты так же касаются и вас но вам временами будут давать поблажки но при злоупотреблении возможностями понижение.\n\nДоп-е правила:\n1.Нарушать эти же правила в войс чате карается мутом на сколько захочет админ\n2. Обман участников на деньги бан навсегда\n\nВторичное:\n1.Попытка ухода от наказания т.е удаление сообщения с нарушением мут вдвое увеличивается\n2. Разглашение личной информации мут 12 часов + варн")
	elif message.text == "/pravila@TrueFamily_bot":
		await bot.send_message(message.chat.id,"🗓 правила чата:\nУчастники:\n1. ЛГБТ шутки мут 15 минут\n2. Оскорбление родителей и МАТ мут 10 минут\n3. Скидывать скрины с лс ботом сюда мут 1 час + варн\n4. Оскорбление участников в меру админ сам посчитает нужным мутить или нет, мут 20 минут\n5. Порнография бан на 24 часа\n6. Спам / Флуд, мут 10 минут\n\nМодераторы/Админы:\n1-6 пункты так же касаются и вас но вам временами будут давать поблажки но при злоупотреблении возможностями понижение.\n\nДоп-е правила:\n1.Нарушать эти же правила в войс чате карается мутом на сколько захочет админ\n2. Обман участников на деньги бан навсегда\n\nВторичное:\n1.Попытка ухода от наказания т.е удаление сообщения с нарушением мут вдвое увеличивается\n2. Разглашение личной информации мут 12 часов + варн")
	elif message.text == "/help@TrueFamily_bot":
		await bot.send_message(message.chat.id,"Версия : "+ version +'\n\n❗Этот Бот "True-Family" от EcpochmaK❗\n\nДобро пожаловать, в Chat Гимназии №17 💫\nВ этой группе ученики общаются между собой 👥, а также играют в Мафию⚔\nДля того чтобы присоединится к нам, прочитай инструкцию по Мафии📖, а также прочитай "Правила чата"❗\nВсё приведено ниже✅\n\n🔽🔽🔽ЧИТАТЬ🔽🔽🔽\n\n/pravila - Правила чата📋\n'+'t.me/chetodelaem/602897 - Правила МАФИИ🔫')
	elif message.text == "Чебурашка" or message.text == "чебурашка":
		await message.reply('Вы про меня ?')
	elif message.text == "Чебурашка запусти игру":
		await message.answer("✨✨✨✨ NEON BLASTER 2 ✨✨✨✨",reply_markup=urlne)#??????????

	if not database.examination(message.from_user.id):
		database.add(message.from_user.id)
	if not database.mute(message.from_user.id):
		pass
	else:
		await message.delete()


#РАБОТА БОТА=TRUE
#executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
if __name__ == '__main__':
    executor.start_polling(dp)
