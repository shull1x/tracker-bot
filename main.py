import telebot
from config import TOKEN
from database import init_db, add_expense, get_expenses
from logic import convert_currency

bot = telebot.TeleBot(TOKEN)
init_db()

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(
        message.chat.id, 
        "Команды:\n/add <сумма> <категория>\n/stats\n/convert <сумма> <из> <в>"
    )

@bot.message_handler(commands=['add'])
def add(message):
    try:
        parts = message.text.split()
        amount = float(parts[1])
        category = parts[2]
        add_expense(message.chat.id, amount, category)
        bot.send_message(message.chat.id, "Расход успешно добавлен!")
    except Exception:
        bot.send_message(message.chat.id, "Ошибка. Пример: /add 500 Еда")

@bot.message_handler(commands=['stats'])
def stats(message):
    total = get_expenses(message.chat.id)
    bot.send_message(message.chat.id, f"Всего потрачено: {total}")

@bot.message_handler(commands=['convert'])
def convert(message):
    try:
        parts = message.text.split()
        amount = float(parts[1])
        from_c = parts[2].upper()
        to_c = parts[3].upper()
        result = convert_currency(amount, from_c, to_c)
        if result:
            bot.send_message(message.chat.id, f"{amount} {from_c} = {result:.2f} {to_c}")
        else:
            bot.send_message(message.chat.id, "Ошибка конвертации валют.")
    except Exception:
        bot.send_message(message.chat.id, "Ошибка. Пример: /convert 100 USD RUB")

if __name__ == "__main__":
    bot.polling(none_stop=True)
