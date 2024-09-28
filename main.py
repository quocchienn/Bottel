import telegram
from telegram.ext import Updater, CommandHandler

# Định nghĩa lệnh /start
def start(update, context):
    update.message.reply_text('Xin chào! Đây là bot Telegram của bạn.')

def main():
    # Thêm Token bot của bạn từ BotFather
    updater = Updater('YOUR_BOT_TOKEN', use_context=True)
    
    dp = updater.dispatcher
    
    # Xử lý lệnh /start
    dp.add_handler(CommandHandler('start', start))
    
    # Bắt đầu bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
