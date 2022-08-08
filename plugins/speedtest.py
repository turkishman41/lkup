import os

import speedtest
import wget
from pyrogram import filters
from pyrogram.types import Message

from bot import Bot
from config import ADMINS


@Bot.on_message(filters.command("speedtest") & filters.user(ADMINS))
async def run_speedtest(client: Bot, message: Message):
    hiztesti = await message.reply_text("`⚡️ Hız Testi Yapılıyor`")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        hiztesti = await hiztesti.edit("`⚡️ İndirme hızı ölçülüyor... `")
        test.download()
        hiztesti = await hiztesti.edit("`⚡️ Yükleme hızı ölçülüyor...`")
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        await hiztesti.edit(e)
        return
    hiztesti = await hiztesti.edit("`🔄 Sonuçlar Getiriliyor...`")
    path = wget.download(result["share"])

    sonuccaption = f"""💡 <b>Hız Testi Sonucu</b>
    
<u><b>Client:<b></u>
<b>ISP:</b> {result['client']['isp']}
<b>Ülke:</b> {result['client']['country']}
  
<u><b>Sunucu:</b></u>
<b>İsim:</b> {result['server']['name']}
<b>Ülke:</b> {result['server']['country']}, {result['server']['cc']}
<b>Sponsor:</b> {result['server']['sponsor']}
⚡️ <b>Ping:</b> {result['ping']}"""
    msg = await client.send_photo(
        chat_id=chat_id, photo=path, caption=sonuccaption
    )
    os.remove(path)
    await hiztesti.delete()
