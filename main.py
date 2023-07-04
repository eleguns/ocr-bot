import config
from pyrogram import Client, filters
from pyrogram.types import Message

app = Client(
    name='bot',
    api_id=config.api_id,
    api_hash=config.api_hash,
    bot_token=config.token
)


@app.on_message(filters.private & filters.command('start'))
async def start(c: Client, m:Message):
    await m.reply('Welcome to ocr bot!\nYou can send me photos and I extract texts from it!')

@app.on_message(filters.private & filters.photo)
async def extraction(c: Client, m: Message):
    pass

@app.on_message(filters.group)
async def join(c: Client, m: Message):
    me = await c.get_me()
    me_id = me.id
    if m.service == 'new_chat_members' and m.new_chat_members[0].id == me_id:
        await c.send_message(m.chat.id, 'Hi I can extract texts from your photo\nReply <code>/extract</code> to your photos to see it!')
