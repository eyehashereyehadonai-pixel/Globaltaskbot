import telebot
import requests

BOT_TOKEN = "ACA_TU_TOKEN"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, 
    "🌍 Bienvenido a *GlobalTasks*\n"
    "Ganá dinero real completando tareas de plataformas oficiales.\n"
    "👉 Escribí: tareas"
    )

@bot.message_handler(func=lambda m: m.text.lower() == "tareas")
def tasks(msg):
    bot.reply_to(msg,
    "💼 Tarea 1: Registro Toloka\n"
    "💵 paga: 2 a 10 USD\n"
    "🔗 https://toloka.ai\n\n"
    "💼 Tarea 2: Sproutgigs\n"
    "💵 paga: 0.05–1.5 USD\n"
    "🔗 https://sproutgigs.com\n\n"
    "💼 Tarea 3: Remotasks\n"
    "💵 paga: 2–5 USD / hora\n"
    "🔗 https://remotasks.com\n\n"
    "⏳ Nuevas tareas cada 30 minutos."
    )

bot.polling()
