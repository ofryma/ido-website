## Find the chat (group) id

In order to find the group id of a telegram group you can run the following script:

```py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    print(update.effective_chat.id)

    await update.message.reply_text(f'Chat ID: {update.effective_chat.id}')

# Change the api key to the one recived from botfather
app = ApplicationBuilder().token("YOUR BOT TOKEN HERE").build()

app.add_handler(CommandHandler("hello", hello))

print("Start polling")
app.run_polling()
```

After running this script, simply send a message with `/hello` commad and the chat id will be printed and send back in the chat.