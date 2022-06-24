import asyncio
import configparser
from telethon.sync import TelegramClient, events

# Присваиваем значения внутренним переменным
api_id = 13939535
api_hash = 'dde2128f70fce92e9f0e7afbbcefdad8'
username = 'ghotbustard'

# Массив для хранения ID пользователей, отправивших сообщение
user_id_list = []

# Создание объекта клиента Telegram
client = TelegramClient(username, api_id, api_hash)

# Запуск клиента
client.start()


# Событие на новое входящее сообщение
@client.on(events.NewMessage(incoming=True, forwards=None))
async def handler(event):
    user_info = event.message.to_dict()['from_id']
    user_id = user_info['user_id']
    count = 0
    for i in user_id_list:
        if i == user_id:
            count += 0
        else:
            continue
    if count == 0:
        user_id_list.append(user_id)
        await asyncio.sleep(5)
        await client.send_message(user_id,
                                  '👋Привет, прочитай условия работы @r_freelance\n'
                                  '\n'
                                  '👨‍💻Если готов работать напиши свой город, а так же есть ли у тебя долги сюда @danzaze\n'
                                  '\n'
                                  '🧧Пример анкеты:\n'
                                  '\n'
                                  'Город Москва\n'
                                  'Долгов нет\n'
                                  ' \n'
                                  '💡Расскажу подробнее что нужно делать и начнем работать')
    print(user_id_list)


client.run_until_disconnected()
