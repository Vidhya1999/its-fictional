from flask import Flask,request
import telegram
from telbot.credentials import
bot_token, bot_username,URL
global bot
global TOKEN
TOKEN=bot_token
bot=telegram.Bot(token=TOKEN)
app=Flask(__name__)
@app.token('/{}'.format(TOKEN),methods=['POST'])
def respond():
	update = telegram.Update.de_json(request.get_json(force=True), bot)
	chat_id = update.message.chat.id
	msg_id = update.message.message_id
	text = update.message.text.encode('utf-8').decode()
	print("got text message :", text)
	if text == "/start":
		bot_welcome = """
       Welcome to Recs4u bot.This bot will give you recommendations based on your taste. What do you want recommendations for? Books or movies?
	Enter books for books and movies for movies"""
       bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)
	else:
	try:
           # clear the message we got from any non alphabets
           text = re.sub(r"\W", "_", text)
           # create the api link for the avatar based on http://avatars.adorable.io/
           url = "https://api.adorable.io/avatars/285/{}.png".format(text.strip())
           # reply with a photo to the name the user sent,
           # note that you can send photos by url and telegram will fetch it for you
           bot.sendPhoto(chat_id=chat_id, photo=url, reply_to_message_id=msg_id)
       except Exception:
           # if things went wrong
           bot.sendMessage(chat_id=chat_id, text="There was a problem in the name you used, please enter different name", reply_to_message_id=msg_id)

   return 'ok'
@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
   s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
   if s:
       return "webhook setup ok"
   else:
       return "webhook setup failed"

@app.route('/')
def index():
   return '.'


if __name__ == '__main__':
   app.run(threaded=True)


