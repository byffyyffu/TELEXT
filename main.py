from pyrogram import Client, filters
import os, shutil
from creds import my
from telegraph import upload_file
import logging

logging.basicConfig(level=logging.INFO)


TGraph = Client(
    "Image upload bot",
    bot_token = my.BOT_TOKEN,
    api_id = my.API_ID,
    api_hash = my.API_HASH
)


@TGraph.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(f"<b>مرحبا {message.from_user.first_name}, [📍](https://telegra.ph/file/f885709c8201a2ba098e5.jpg)انا اسمي صانع تلجراف ميديا 🥳\n\n <u>انا بوت تحويل الميديا الى تلجراف.</u>\n\n🗑️ أرسل لي أي شيء متحركة ، صورة  &فيديو MP4 وسأحمله على Telegra.ph وأرسل لك رابطًا مرة أخرى اشترك🛎️ @EITHON @VFF35 \n\n🔰احب هذا البوت♥️.</b>", True)
    
@TGraph.on_message(filters.photo)
async def getimage(client, message):
    tmp = os.path.join("تحميل",str(message.chat.id))
    if not os.path.isdir(tmp):
        os.makedirs(tmp)
    imgdir = tmp + "/" + str(message.message_id) +".jpg"
    dwn = await message.reply_text("جاري التحميل...", True)          
    await client.download_media(
            message=message,
            file_name=imgdir
        )
    await dwn.edit_text("جاري الرفع...")
    try:
        response = upload_file(imgdir)
    except Exception as error:
        await dwn.edit_text(f"اووبس هناك خطا\n{error}")
        return
    await dwn.edit_text(f"📍الرابط: https://telegra.ph{response[0]} \n\n\n 🔗تم الصنع والتعريب بواسطه : @EITHON @VFF35")
    shutil.rmtree(tmp,ignore_errors=True)


TGraph.run()
