from userbot import tebot,client,bot
from userbot.utils import register
from telethon import events
from telethon.tl import functions, types
from telethon.tl.types import Channel, Chat, User
@tebot.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def _(event):
    me = await client.get_me()
    sendr = event.chat_id
    if me.id!=sendr:
        x=await tebot.forward_messages(me.id,event.message)
        await x.reply(f'`userid` **=** {sendr} , `profile` **=** [UserProfile](tg://user?id={sendr})\n __To reply to user__ **Use** !reply {sendr};(your message or reply to a message)')

@register(outgoing=True, pattern=r"^!reply")
async def sh1vam(event):
    try :
        lb,cn=event.text[7:].split(";")
        await tebot.send_message(entity=int(lb),message=cn)
        await event.edit(f"Message sent to [User](tg://user?id={lb})")

    except:
        lb =event.text[7:]
        reply = await event.get_reply_message()
        await tebot.send_message(entity=int(lb),message=reply)
        await event.edit(f"Your Message sent to [User](tg://user?id={lb})")

        '''else:
        lb =event.text[7:]
        reply = await event.get_reply_message()
        await tebot.forward_messages(int(lb),reply)
        await event.edit(f"Your Message sent to [User](tg://user?id={lb})")
        return'''
