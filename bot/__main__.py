import json

from pyrogram import Client, enums, filters

from bot.db import db
from bot.lib import get_image, get_response

from .constant import Env, Message

app = Client(
    name="mybot",
    bot_token=Env.BOT_TOKEN,
    api_id=Env.APP_ID,
    api_hash=Env.APP_HASH,
)


def add_to_db(user_id, text):
    db.setex(user_id, 60 * 5, text)


@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text(Message.start)


@app.on_message(filters.command("reset"))
async def reset(_, message):
    db.set(message.chat.id, Message.default_prompt)
    await message.reply_text(Message.reset)


@app.on_message(filters.command("help"))
async def help(_, message):

    await message.reply_text(Message.help)


@app.on_message(filters.command("terms"))
async def terms(_, message):

    await message.reply_text(Message.terms)


# /image - Generates an image based on your query using openai.Image.create
@app.on_message(filters.command("image"))
async def image(client, message):
    await client.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_PHOTO)
    img_url = get_image(message.text[7:])
    await message.reply_photo(img_url, quote=True)
    await message.reply_document(img_url, file_name="image.png", caption=Message.caption)


@app.on_message(filters.text)
async def chatgpt(client, message):
    async def handle_progress():
        await client.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_PHOTO)

    await client.send_chat_action(message.chat.id, enums.ChatAction.TYPING)

    query = db.get(message.chat.id)
    query = Message.default_prompt if query is None else query.decode("utf-8")

    query += f"""{message.text} \nAI:"""
    query = query[-2048:] if len(query) > 2048 else query

    response = get_response(query)

    obj = {}
    try:
        obj = json.loads(response)
    except:
        pass

    if "action" in obj and obj["action"] == "image":
        img_url = get_image(obj["prompt"])
        await message.reply_document(
            img_url,
            quote=True,
            file_name="image.png",
            caption=Message.caption_image,
            progress=handle_progress,
        )

    else:
        query += f"""{response} \nYou:"""
        add_to_db(message.chat.id, query)

        await message.reply_text(response, quote=True)


if __name__ == "__main__":
    app.run()
