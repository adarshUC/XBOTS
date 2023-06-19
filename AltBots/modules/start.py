from telethon import version, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("️️⚝ нєℓρ ⚝", data="help_back")
    ],
    [
        Button.url("️️⚝ σωηєя ️️⚝", "https://t.me/aadarsh_legend"),
        Button.url("️️⚝ ¢нαт ️️️️⚝", "https://t.me/t34m_xd_chat")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"ʜᴇʏ​ {event.sender.first_name},\n\nɪ ᴀᴍ {bot_name}​\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ : 𝝙𝗗𝗔𝗥𝗦𝗛\n\n"
        TEXT += f"» xᴅʙᴏᴛs ᴠᴇʀsɪᴏɴ : M3.3\n"
        TEXT += f"» ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 3.11.3\n"
        TEXT += f"» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : {version}\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                    event.chat_id,
                    "https://telegra.ph/file/3fbb4043cfc0d3d90e888.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
        )
