# GPTCHATBOT

This is a simple Telegram chatbot that uses GPT-3 to generate responses to user input. It is based on openai's [GPT-3 API](https://openai.com/api)

## Commands
```
/start - Starts a conversation with the bot 
/help - Provides an overview of all the features and commands available 
/image - Generates an image based on your query
/reset - Deletes your previous queries
/terms - Provides information about the terms and conditions of the bot
/about - Provides information about the bot 
```

### Note: 
Any message sent to the bot will be interpreted as a query except above commands. The bot will generate a response based on your query.

## Environment Variables
```
BOT_TOKEN - Telegram bot token
API_ID - Telegram API ID
API_HASH - Telegram API Hash
OPENAI_API_KEY - OpenAI API Key
REDIS_HOST - Redis db host
REDIS_PASSWORD - Redis db password
REDIS_PORT - Redis db port
```

## Installation
```bash
pip install -r requirements.txt
python -m bot
```
