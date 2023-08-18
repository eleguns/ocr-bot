import config
from pytesseract.pytesseract import tesseract_cmd
from PIL import Image
from io import BytesIO
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
    msg = await m.reply('<b>Please Wait . . .</b>', quote=True)
    try :
        file = await c.download_media(m, in_memory=True)
    except Exception as e :
        print(f'error : {e}')
        await msg.edit('<b>can\'t download file</b>')
    photo_bytes = BytesIO(bytes(file.getbuffer()))
    try :
        text = convert(Image.open(photo_bytes))
        await msg.edit(f'<b>Result :</b>\n<code>{text}</code>')
    except Exception as e :
        print(f'error : {e}')
        await msg.edit('<b>an error occurred, please try again or report to the admin</b>')

@app.on_message(filters.group & filters.command('extract'))
async def extract(c: Client, m:Message):
    if not m.reply_to_message:
        await m.reply('<b>You didn\'t reply to photo!</b>')
        return
    msg = await m.reply('<b>Please Wait . . .</b>', quote=True)
    try :
        file = await c.download_media(m.reply_to_message, in_memory=True)
    except Exception as e :
        print(f'error : {e}')
        await msg.edit('<b>can\'t download file</b>')
    photo_bytes = BytesIO(bytes(file.getbuffer()))
    try :
        text = convert(Image.open(photo_bytes))
        await msg.edit(f'<b>Result :</b>\n<code>{text}</code>')
    except Exception as e :
        print(f'error : {e}')
        await msg.edit('<b>an error occurred, please try again or report to the admin</b>')
@app.on_message(filters.group)
async def join(c: Client, m: Message):
    me = await c.get_me()
    me_id = me.id
    if m.service and m.new_chat_members[0].id == me_id:
        await c.send_message(m.chat.id, '<b>Hi I can extract texts from your photo</b>\n<b>Reply</b> <code>/extract</code> <b>to your photos to see it!</b>')



if __name__ == '__main__':
    app.run()