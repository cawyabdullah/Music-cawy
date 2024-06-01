from pyrogram import Client, idle
#'‹ ٰ💸 ⇣ سورس الفراعنة ⇣ 💸 › .'#
from pyromod import listen



bot = Client(
    "mo",
    api_id=8186557,
    api_hash="efd77b34c69c164ce158037ff5a0d117",
    bot_token="6259089665:AAHlXx6p7MBs2oWJ-W0nW4jAtchctxicH_k",#توكن المصنع
    plugins=dict(root="MHelal")
    )

DEVS = ["MohamedHelal_l", "EE_LLP","DAD_DESHA","AD3_M"] 


async def start_helalbot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    for hh in DEVS:
        try:
            await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
        except:
            pass
    await idle()
