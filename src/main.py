import config
from pytesseract.pytesseract import tesseract_cmd
from PIL import Image
from pytesseract import image_to_string as convert
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
    try :
        file = await c.download_media(m, in_memory=True)
    except Exception as e :
        print(f'error : {e}')
        await m.reply('can\'t download file')
    buffer = file.getbuffer()
    try :
        text = convert(Image.open(buffer))
    except Exception as e :
        print(f'error : {e}')
        await m.reply('an error occurred, please try again or report to the admin')

@app.on_message(filters.group)
async def join(c: Client, m: Message):
    me = await c.get_me()
    me_id = me.id
    if m.service:
        await m.reply(str(m))
    if m.service == 'new_chat_members' and m.new_chat_members[0].id == me_id:
        await c.send_message(m.chat.id, 'Hi I can extract texts from your photo\nReply <code>/extract</code> to your photos to see it!')

@app.on_message(filters.group & filters.command('extract'))
async def extract(c: Client, m:Message):
    try :
        file = await c.download_media(m, in_memory=True)
    except Exception as e :
        print(f'error : {e}')
        await m.reply('can\'t download file')
    buffer = file.getbuffer()
    try :
        text = convert(Image.open(buffer))
    except Exception as e :
        print(f'error : {e}')
        await m.reply('an error occurred, please try again or report to the admin')


if __name__ == '__main__':
    app.run()