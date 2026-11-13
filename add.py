# ---------------------------
# 𝐘ᴏᴜ𝐑ꜱ𝐒ꜱ !! 𝐕17 Ultra 
# ---------------------------
import sys

def check_branding():
    try:
        with open(__file__, 'r', encoding='utf-8') as f:
            content = f.read()
            
            if "# 𝐘ᴏᴜ𝐑ꜱ𝐒ꜱ !! 𝐕17 Ultra" not in content:
                print("Error: Unauthorized Modification Detected!")
                print("Original branding missing. Closing script...")
                sys.exit()
    except Exception:
        sys.exit()

check_branding()

print("Script started successfully!")

import base64
import random
import asyncio
from telethon import TelegramClient, events, functions, types
from telethon.errors import FloodWaitError, RPCError
# ---------------------------
#              ADD ID 
# ---------------------------
API_ID = 32051125
# ---------------------------
#      ADD API HASH
# ---------------------------
API_HASH = "ad1b7cd0a5c14bb8553c4cf5a9851b00"
# ---------------------------
#      ADD SESSION
# ---------------------------
SESSION = "MY.SESSION"
# ---------------------------
#   ADD BOTS USER
# ---------------------------
ADD_BOTS_LIST = [
    "@Amanmusic_bot", #1
    "@Roguewarrior1_bot", #2
    "@Roguewarrior3_bot", #3
    "@Roguewarrior7_bot", #4
    "@Roguewarrior2_bot", #5
    "@Roguewarrior4_bot", #6
    "@Roguewarrior5_bot", #7
    "@Roguewarrior6_bot", #8
    "@Roguewarrior8_bot", #9
    "@Roguewarrior9_bot", #10
]
# ---------------------------
#    MENU IMG URL
# ---------------------------
MENU_IMAGE_URL = "https://h.uguu.se/BTMYcCSF.jpg"
# ---------------------------
#         REACT LIST
# ---------------------------
REACT_EMOJIS = ["👍", "❤️", "😂", "😱", "🤔", "🔥", "🥰", "👏", "💯", "😈", "🤡", "🎉", "💀", "👀", "😍"]
# ---------------------------
#          REPLY LIST
# ---------------------------
RAID_LIST = [
    "AMAN !!🪽 𝐊ᴏ 𝐁ᴀᴀᴘ 𝐁ᴀɴᴀ 𝐋ᴇ 𝐑ᴀɴᴅɪ 𝐊ᴇ  𝐁ᴀᴄʜᴇ",
    "𝐌ᴜᴊʜᴇ 𝐏ᴀᴘᴀ  𝐁ᴏʟ 𝐑ᴀɴᴅɪ 🤣",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐂ʜᴜᴅᴡᴀ 𝐋ᴇ 𝐘ᴀʜᴀ 😀",
    "𝐑ʀ 𝐊ᴀʀ 𝐑ᴀɴᴅɪ 𝐊ᴇ 𝐁ᴀᴄʜᴇ 😃",
    "𝐌ᴇʀᴇ 𝐒ᴇ 𝐌ᴀᴀ 𝐂ʜ𝐮ᴅᴡᴀ 𝐋ᴇ 𝐒ʟɪᴅᴇ 𝐊ᴀʀ 𝐊ᴇ !!",
    "𝐘ᴀʜᴀ 𝐂ʜᴜᴅ 𝐑ᴀɴᴅɪ 𝐊ᴇ 𝐁ᴀᴄʜᴇ 😃",
    "𝐓ᴇʀɪ 𝐁ʜᴇɴ 𝐂ʜ𝐮ᴅ 𝐊ᴇ 𝐌ᴀʀ 𝐆ʏɪ?",
    "𝐌ᴀᴀ 𝐂ʜᴅᴡᴀ 𝐋ᴇ 𝐓ᴇʀɪ 🤣",
    "𝑯𝒂𝒘𝒂𝒃𝒂𝒂𝒛𝒊 𝒌𝒂𝒓 𝒇𝒂𝒎𝒆 𝒎𝒊𝒍𝒆 𝒈𝒂!",
    "𝐓𝐦𝐤𝐜 𝐎𝐤",
    "𝐓𝐞𝐫𝐢 𝐦𝐚𝐚 150𝐫𝐬 𝐦𝐞 𝐝𝐞𝐭𝐢 𝐡𝐚𝐢 😃",
    "𝑺𝒍𝒊𝒅𝒆 𝒌𝒂𝒓 𝒎𝒂𝒅𝒓𝒄𝒉𝒐𝒅!",
    "𝑪𝒉𝒖𝒅 𝒐𝒏𝒍𝒊𝒏𝒆 𝒇𝒚𝒕𝒓!",
    "𝑩𝒉𝒂𝒘 𝒅𝒖 𝒓𝒓 𝒘𝒉𝒚 𝑹𝒂𝒏𝒅𝒊?",
    "𝑳𝒐𝒍 𝒂𝒊𝒔𝒆 𝒓𝒐𝒚𝒆 𝒈𝒂 😀",
    "𝑹𝒐 𝑹𝒐 𝑹𝒐 𝒕𝒆𝒓𝒊 𝒎𝒂𝒂 𝒕𝒐𝒉 𝒄𝒉𝒖𝒅 𝒌𝒊 𝒉𝒂𝒔𝒉 𝒓𝒉𝒊 😃",
    "𝐂𝐡𝐮𝐝 𝐠𝐚𝐫𝐞𝐞𝐛!",
    "𝐌𝐤𝐜 𝐧𝐨 𝐛𝐡𝐚𝐰 𝐭𝐚𝐭𝐭𝐞!",
    "𝐋𝐨𝐥 𝐜𝐡𝐮𝐝 𝐤𝐢 𝐫𝐨 𝐫𝐡𝐚 𝐚𝐛𝐡 𝐡𝐚𝐰𝐚𝐛𝐚𝐚𝐳 🤣",
    "𝐀𝐰𝐰 𝐑𝐚𝐧𝐝𝐢 𝐭𝐞𝐫𝐢 𝐦𝐚𝐚 𝐭𝐨𝐡 𝐜𝐡𝐮𝐝 𝐠𝐲𝐢!",
    "𝑩𝒐𝒉𝒐𝒕 𝒄𝒉𝒖𝒅𝒊 𝒕𝒉𝒊 𝑻𝒆𝒓𝒊 𝒎𝒂𝒂 𝒓𝒂𝒂𝒕 𝒌𝒐 𝒎𝒆𝒓𝒆 𝒔𝒆 😀",
    "𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐛𝐨𝐥𝐤𝐞 𝐫𝐨𝐲𝐞 𝐠𝐚 𝐚𝐛𝐡 𝐠𝐚𝐫𝐞𝐞𝐛 𝐤𝐢𝐝 𝐮𝐬𝐞 𝐤𝐚𝐫𝐧𝐞 𝐤𝐢 𝐚𝐮𝐤𝐚𝐚𝐭 𝐧𝐡𝐢 𝐭𝐨𝐡 𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐛𝐨𝐥𝐞 𝐠𝐚!!"
]
# ---------------------------
#   RAID TRACKER LIST
# ---------------------------
RAID_MSG_IDS = []
RAID_USERS = []
RAID_DELAY = 1.0
# ---------------------------
#      CLONE MODE
# ---------------------------
MY_OLD_PFP = None
MY_OLD_NAME = ""
MY_OLD_BIO = ""
SPAM_ACTIVE = False

X_TEXT = base64.b64decode(
    "8J2QjuG0ocm04bSHyoAg4p6gIPCdkJjhtI/htJzwnZCR6pyx8J2QkuqcsSAhISDwn6q9"
).decode()
# ---------------------------
#      SPAM MODE
# ---------------------------
SPAM_ACTIVE = False
SPAM_SPEED = 0.5
SPAM_MSG_IDS = []    
# ---------------------------
#      REACT MODE
# ---------------------------
REACT_ACTIVE = False
REACT_USERS = []
REACT_MSG_IDS = []
# ---------------------------
#  SEND/DELETE MODE
# ---------------------------
SEND_ACTIVE = False
SEND_USERS = []  
SEND_MSG_IDS = []
# ---------------------------
#      Client Initialization
# ---------------------------
YoUrSsS = TelegramClient(SESSION, API_ID, API_HASH)


async def safe_edit(event, text):
    try:
        return await event.edit(text)
    except:
        return await event.reply(text)     
# ========================
#        REACT COMMAND (.react)
# ========================
@YoUrSsS.on(events.NewMessage(pattern=r"^\.react$", outgoing=True))
async def cmd_react(event):
    global REACT_ACTIVE, REACT_USERS
    
    if not event.is_reply:
        return await safe_edit(event, "❌ .𝐑ᴇᴀᴄᴛ 𝐑ᴇᴘʟʏ 𝐎ɴ 𝐒ᴏᴍᴇᴏɴᴇ 𝐌sɢ ~")
    
    try:
        reply_msg = await event.get_reply_message()
        target_id = reply_msg.sender_id
        chat_id = event.chat_id
        gc_target = (chat_id, target_id)
        
        if gc_target not in REACT_USERS:
            REACT_USERS.append(gc_target)
            REACT_ACTIVE = True
            await event.edit(f"✅ 𝐑ᴇᴀᴄᴛ 𝐀ᴄᴛɪᴠᴀᴛᴇᴅ 𝐅ᴏʀ 𝐓ʜɪs 𝐔sᴇʀ!")
        else:
            await event.edit("ℹ️ 𝐓ʜɪs 𝐔sᴇʀ 𝐀ʟʀᴇᴀᴅʏ 𝐈ɴ 𝐑ᴇᴀᴄᴛ 𝐋ɪsᴛ")
        
        await asyncio.sleep(2)
        await event.delete()
        
    except Exception as e:
        await safe_edit(event, f"❌ 𝐑ᴇᴀᴄᴛ 𝐄ʀʀᴏʀ: `{str(e)[:40]}`")
# ======================
#     UNREACT COMMAND 
# ======================
@YoUrSsS.on(events.NewMessage(pattern=r"^\.unreact$", outgoing=True))
async def cmd_unreact(event):
    global REACT_ACTIVE, REACT_USERS, REACT_MSG_IDS
    
    try:
        chat_id = event.chat_id
        
        if event.is_reply:
            reply_msg = await event.get_reply_message()
            target_id = reply_msg.sender_id
            gc_target = (chat_id, target_id)
            
            if gc_target in REACT_USERS:
                REACT_USERS.remove(gc_target)
                await event.edit("✅ 𝐑ᴇᴀᴄᴛ 𝐒ᴛᴏᴘᴘᴇᴅ 𝐅ᴏʀ 𝐓ʜɪs 𝐔sᴇʀ")
            else:
                await event.edit("ℹ️ 𝐓ʜɪs 𝐔sᴇʀ 𝐍ᴏᴛ 𝐈ɴ 𝐑ᴇᴀᴄᴛ 𝐋ɪsᴛ")
        else:
            REACT_USERS = [pair for pair in REACT_USERS if pair[0] != chat_id]
            await event.edit("🛑 𝐀ʟʟ 𝐑ᴇᴀᴄᴛ𝐒 𝐒ᴛᴏᴘᴘᴇᴅ 𝐅ᴏʀ 𝐓ʜɪs 𝐂ʜᴀᴛ")
        
        if not REACT_USERS:
            REACT_ACTIVE = False
        
       
        REACT_MSG_IDS.clear()
        
        await asyncio.sleep(2)
        await event.delete()
        
    except Exception as e:
        await safe_edit(event, f"❌ 𝐔ɴʀᴇᴀᴄᴛ 𝐄ʀʀᴏʀ: `{str(e)[:40]}`")
# =======================
#        REACT LISTENER (AUTO)
# =======================
@YoUrSsS.on(events.NewMessage(incoming=True))
async def auto_react_listener(event):
    global REACT_ACTIVE, REACT_USERS, REACT_MSG_IDS
    
    if not REACT_ACTIVE:
        return
    
    gc_target = (event.chat_id, event.sender_id)
    
  
    if gc_target in REACT_USERS:
        try:
         
            me = await YoUrSsS.get_me()
            if event.sender_id == me.id:
                return
            
            
            await asyncio.sleep(0.5)
            
           
            emoji = random.choice(REACT_EMOJIS)
            
          
            await YoUrSsS(functions.messages.SendReactionRequest(
                peer=event.chat_id,
                msg_id=event.id,
                reaction=[types.ReactionEmoji(emoticon=emoji)]
            ))
            
            
            REACT_MSG_IDS.append(event.id)
            
        except Exception as e:
            print("Auto React Error:", e)
# ======================
#   SEND/DELETE COMMAND 
# ======================
@YoUrSsS.on(events.NewMessage(pattern=r"^\.send$", outgoing=True))
async def cmd_send(event):
    global SEND_ACTIVE, SEND_USERS
    
    if not event.is_reply:
        return await safe_edit(event, "❌ .𝐒ᴇɴᴅ 𝐑ᴇᴘʟʏ 𝐎ɴ 𝐒ᴏᴍᴇᴏɴᴇ 𝐌sɢ ~")
    
    try:
        reply_msg = await event.get_reply_message()
        target_id = reply_msg.sender_id
        chat_id = event.chat_id
        gc_target = (chat_id, target_id)
        
        if gc_target not in SEND_USERS:
            SEND_USERS.append(gc_target)
            SEND_ACTIVE = True
            await event.edit(f"✅ 𝐒ᴇɴᴅ/𝐃ᴇʟᴇᴛᴇ 𝐀ᴄᴛɪᴠᴀᴛᴇᴅ 𝐅ᴏʀ 𝐓ʜɪs 𝐔sᴇʀ!")
        else:
            await event.edit("ℹ️ 𝐓ʜɪs 𝐔sᴇʀ 𝐀ʟʀᴇᴀᴅʏ 𝐈ɴ 𝐒ᴇɴᴅ 𝐋ɪsᴛ")
        
        await asyncio.sleep(2)
        await event.delete()
        
    except Exception as e:
        await safe_edit(event, f"❌ 𝐒ᴇɴᴅ 𝐄ʀʀᴏʀ: `{str(e)[:40]}`")
# ======================
#    UNSEND COMMAND 
# ======================
@YoUrSsS.on(events.NewMessage(pattern=r"^\.unsend$", outgoing=True))
async def cmd_unsend(event):
    global SEND_ACTIVE, SEND_USERS, SEND_MSG_IDS
    
    try:
        chat_id = event.chat_id
        
        if event.is_reply:
            reply_msg = await event.get_reply_message()
            target_id = reply_msg.sender_id
            gc_target = (chat_id, target_id)
            
            if gc_target in SEND_USERS:
                SEND_USERS.remove(gc_target)
                await event.edit("✅ 𝐒ᴇɴᴅ/𝐃ᴇʟᴇᴛᴇ 𝐒ᴛᴏᴘᴘᴇᴅ 𝐅ᴏʀ 𝐓ʜɪs 𝐔sᴇʀ")
            else:
                await event.edit("ℹ️ 𝐓ʜɪs 𝐔sᴇʀ 𝐍ᴏᴛ 𝐈ɴ 𝐒ᴇɴᴅ 𝐋ɪsᴛ")
        else:
            SEND_USERS = [pair for pair in SEND_USERS if pair[0] != chat_id]
            await event.edit("🛑 𝐀ʟʟ 𝐒ᴇɴᴅ/𝐃ᴇʟᴇᴛᴇ 𝐒ᴛᴏᴘᴘᴇᴅ 𝐅ᴏʀ 𝐓ʜɪs 𝐂ʜᴀᴛ")
        
        if not SEND_USERS:
            SEND_ACTIVE = False
        
        
        SEND_MSG_IDS.clear()
        
        await asyncio.sleep(2)
        await event.delete()
        
    except Exception as e:
        await safe_edit(event, f"❌ 𝐔ɴsᴇɴᴅ 𝐄ʀʀᴏʀ: `{str(e)[:40]}`")
# ========================
#        SEND/DELETE 
# =======================
@YoUrSsS.on(events.NewMessage(incoming=True))
async def auto_send_delete_listener(event):
    global SEND_ACTIVE, SEND_USERS, SEND_MSG_IDS
    
    if not SEND_ACTIVE:
        return
    
    gc_target = (event.chat_id, event.sender_id)
    
   
    if gc_target in SEND_USERS:
        try:
            
            me = await YoUrSsS.get_me()
            if event.sender_id == me.id:
                return
            
          
            await asyncio.sleep(0.5)
            
            
            await YoUrSsS.delete_messages(event.chat_id, [event.id])
            
            
            SEND_MSG_IDS.append(event.id)
            
        except Exception as e:
            print("Auto Send/Delete Error:", e)
# =====================
#         ADMIN COMMAND 
# =====================
@YoUrSsS.on(events.NewMessage(pattern=r"^\.admin(?:\s+(\d+))?$", outgoing=True))
async def cmd_admin(event):
    
    if not event.is_reply:
        return await safe_edit(event, "❌ .𝐀ᴅᴍɪɴ [𝐂ᴏᴜɴᴛ] 𝐑ᴇᴘʟʏ 𝐎ɴ 𝐁ᴏᴛ 𝐌sɢ ~")
    
    try:
       
        count_str = event.pattern_match.group(1)
        if count_str:
            count = int(count_str)
            if count < 1:
                count = 1
            if count > 30:  
                count = 30
        else:
            count = 1  
        
        reply_msg = await event.get_reply_message()
        
        
        reply_user = await YoUrSsS.get_entity(reply_msg.sender_id)
        if not reply_user.bot:
            return await safe_edit(event, "❌ 𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀 𝐁ᴏᴛ 𝐓ᴏ 𝐌ᴀᴋᴇ 𝐀ᴅᴍɪɴ!")
        
      
        first_bot_id = reply_msg.sender_id
        
        
        chat = await event.get_chat()
        chat_id = event.chat_id
        
       
        try:
            perms = await YoUrSsS.get_permissions(chat_id, 'me')
            if not perms or not perms.is_admin:
                return await safe_edit(event, "❌ 𝐈 𝐌ᴜsᴛ 𝐁ᴇ 𝐀ᴅᴍɪɴ 𝐓ᴏ 𝐀ᴅᴅ 𝐀ᴅᴍɪɴs!")
        except Exception:
            return await safe_edit(event, "❌ 𝐏ᴇʀᴍɪssɪᴏɴ 𝐄ʀʀᴏʀ")
        
      
        bot_ids = [first_bot_id]
        
        
        if count > 1:
            
            first_bot_username = reply_user.username
            if first_bot_username:
                try:
                    start_index = next(i for i, bot in enumerate(ADD_BOTS_LIST) if bot.lower() == first_bot_username.lower())
                except StopIteration:
                    start_index = 0
            else:
                start_index = 0
            
            
            for i in range(start_index + 1, min(start_index + count, len(ADD_BOTS_LIST))):
                try:
                    bot_entity = await YoUrSsS.get_entity(ADD_BOTS_LIST[i])
                    if bot_entity.bot: 
                        bot_ids.append(bot_entity.id)
                except Exception:
                    continue
        
        await event.edit(f"⚙️ 𝐀ᴅᴅɪɴɢ `{len(bot_ids)}` 𝐁ᴏᴛs 𝐀s 𝐀ᴅᴍɪɴ...")
        
        
        admin_rights = types.ChatAdminRights(
            change_info=True,
            post_messages=True,
            edit_messages=True,
            delete_messages=True,
            ban_users=True,
            invite_users=True,
            pin_messages=True,
            manage_call=True,
            anonymous=False,
            manage_topics=True
        )
        
        
        added_count = 0
        failed_count = 0
        
        for bot_id in bot_ids:
            try:
                if isinstance(chat, types.Channel):
                    await YoUrSsS(functions.channels.EditAdminRequest(
                        channel=chat_id,
                        user_id=bot_id,
                        admin_rights=admin_rights,
                        rank="Admin"
                    ))
                elif isinstance(chat, types.Chat):
                    await YoUrSsS(functions.messages.EditChatAdminRequest(
                        chat_id=chat_id,
                        user_id=bot_id,
                        is_admin=True
                    ))
                added_count += 1
                await asyncio.sleep(1.5)
                
            except FloodWaitError as fw:
                await event.edit(f"⏳ 𝐅ʟᴏᴏᴅ ~ {fw.seconds}s")
                await asyncio.sleep(fw.seconds)
                failed_count += 1
                
            except Exception as e:
                print(f"Admin add error for bot {bot_id}: {e}")
                failed_count += 1
        
        result_text = (
            f"✅ `{added_count}` 𝐁ᴏᴛs 𝐀ᴅᴅᴇᴅ 𝐀s 𝐀ᴅᴍɪɴ!\n"
            f"❌ `{failed_count}` 𝐅ᴀɪʟᴇᴅ"
        )
        await event.edit(result_text)
        
        await asyncio.sleep(3)
        await event.delete()
        
    except FloodWaitError as fw:
        await safe_edit(event, f"⏳ 𝐅ʟᴏᴏᴅ ~ {fw.seconds}s")
        await asyncio.sleep(fw.seconds)
    except ValueError:
        await safe_edit(event, "❌ .𝐀ᴅᴍɪɴ [𝐂ᴏᴜɴᴛ] - 𝐔sᴇ 𝐍ᴜᴍʙᴇʀ 𝐎ɴʟʏ")
    except Exception as e:
        await safe_edit(event, f"❌ 𝐀ᴅᴍɪɴ 𝐄ʀʀᴏʀ: `{str(e)[:40]}`")
# ---------------------------
#COMMAND HANDLER
# ---------------------------
@YoUrSsS.on(events.NewMessage(pattern=r"^\.addbots(?: |$)(.*)", outgoing=True))
async def cmd_addbots(event):
    try:
        arg = event.pattern_match.group(1).strip()

        if not arg:
            return await safe_edit(event, "addbots <count>`")

        try:
            limit = int(arg)
        except ValueError:
            return await safe_edit(event, "𝐈ɴᴠᴀʟɪᴅ 𝐍ᴜᴍʙᴇʀ")

        if limit < 1:
            limit = 1
        if limit > len(ADD_BOTS_LIST):
            limit = len(ADD_BOTS_LIST)

        chat = await event.get_chat()
       
        try:
            perms = await YoUrSsS.get_permissions(event.chat_id, 'me')
            if not perms or not perms.is_admin:
                return await safe_edit(event, "𝐈 𝐌ᴜsᴛ 𝐁ᴇ 𝐀ᴅᴍɪɴ")
        except Exception:
            return await safe_edit(event, "𝐏ᴇʀᴍ 𝐄ʀʀ")

        status = await event.edit(f"𝐀ᴅᴅɪɴɢ `{limit}` 𝐁ᴏᴛs...")

        added = 0
        failed = 0
        already = 0

        for idx, bot_username in enumerate(ADD_BOTS_LIST[:limit], start=1):
            try:
                await status.edit(f"{idx}/{limit} → @{bot_username}")

                entity = await YoUrSsS.get_entity(bot_username)

                if isinstance(chat, types.Chat):
                    await YoUrSsS(functions.messages.AddChatUserRequest(
                        chat_id=chat.id,
                        user_id=entity,
                        fwd_limit=0
                    ))
                else:
                    await YoUrSsS(functions.channels.InviteToChannelRequest(
                        channel=event.chat_id,
                        users=[entity]
                    ))

                added += 1
                await asyncio.sleep(2.5)

            except FloodWaitError as fw:
                await status.edit(f"𝐅ʟᴏᴏᴅ ~ {fw.seconds}s")
                await asyncio.sleep(fw.seconds)

            except RPCError as e:
                err = str(e).lower()
                if "already" in err or "participant" in err or "member" in err:
                    already += 1
                else:
                    failed += 1
                    print("RPC ERROR:", e)
                await asyncio.sleep(1)

            except Exception as e:
                failed += 1
                print("GENERAL ERROR:", e)
                await asyncio.sleep(1)

        text = (
            " 𝐘ᴏᴜ𝐑ꜱ𝐒ꜱ !! 𝐕17 𝐔𝐬𝐞𝐫\n"
            "━━━━━━━━━━━━━━━\n"
            f"`{added}` 𝐀ᴅᴅᴇᴅ ~\n"
            f"`{already}` 𝐀ʟʀᴇᴀᴅʏ ~\n"
            f"`{failed}` 𝐅ᴀɪʟᴇᴅ ~"
        )
        await status.edit(text)

    except Exception as e:
        await safe_edit(event, f"𝐀ᴅᴅ𝐁ᴏᴛs ~ {str(e)[:40]}")
# ---------------------------
#   MUTE COMMAND
# ---------------------------
@YoUrSsS.on(events.NewMessage(pattern=r"^\.mute$", outgoing=True))
async def cmd_mute(event):
    if not event.is_reply:
        return await safe_edit(event, ".𝐌ᴜᴛᴇ 𝐑ᴇᴘʟʏ 𝐎ɴ 𝐒ᴏᴍᴇᴏɴᴇ 𝐌sɢ ~")
    
    try:
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.sender_id
        
       
        mute_rights = types.ChatBannedRights(
            until_date=None,
            view_messages=False,
            send_messages=True,
            send_media=True,
            send_stickers=True,
            send_gifs=True,
            send_games=True,
            send_inline=True,
            embed_links=True
        )
        
        await YoUrSsS(functions.channels.EditBannedRequest(
            channel=event.chat_id,
            participant=user_id,
            banned_rights=mute_rights
        ))
        await event.edit("🤐 𝐒ᴜᴄᴄᴇ𝘴𝘴ғᴜʟʟʏ 𝐌ᴜᴛᴇᴅ ~")
    except Exception as e:
        await safe_edit(event, f"𝐌ᴜᴛᴇ 𝐄ʀʀᴏʀ ~`{str(e)[:40]}`")

@YoUrSsS.on(events.NewMessage(pattern=r"^\.owr$", outgoing=True))
@YoUrSsS.on(events.NewMessage(pattern=r"^\.owr$", incoming=True))
async def cmd_owr_decode(event):
    try:
        
        await event.reply(X_TEXT)
    except Exception as e:
        print("OWR Command Error:", e)  
# ---------------------------
# UNMUTE COMMAND
# ---------------------------
@YoUrSsS.on(events.NewMessage(pattern=r"^\.unmute$", outgoing=True))
async def cmd_unmute(event):
    if not event.is_reply:
        return await safe_edit(event, ".𝐔ɴᴍᴜᴛᴇᴅ 𝐑ᴇᴘʟʏ 𝐎ɴ 𝐒ᴏᴍᴇᴏɴᴇ 𝐌sɢ ~")
    
    try:
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.sender_id
             
        unmute_rights = types.ChatBannedRights(
            until_date=None,
            view_messages=False,
            send_messages=False, 
            send_media=False,
            send_stickers=False,
            send_gifs=False,
            send_games=False,
            send_inline=False,
            embed_links=False
        )
        
        await YoUrSsS(functions.channels.EditBannedRequest(
            channel=event.chat_id,
            participant=user_id,
            banned_rights=unmute_rights
        ))
        await event.edit("𝐒ᴜᴄᴄᴇ𝘴𝘴ғᴜʟʟʏ 𝐔ɴᴍᴜᴛᴇᴅ ~")
    except Exception as e:
        await safe_edit(event, f"❌ 𝐔ɴᴍᴜᴛᴇ 𝐄ʀʀᴏʀ ~ `{str(e)[:40]}`")
# ---------------------------
# SET RAID DELAY (.delay)
# ---------------------------
@YoUrSsS.on(events.NewMessage(pattern=r"^\.delay (2\.0|1\.[0-9]|0\.[8-9])$", outgoing=True))
async def cmd_set_raid_delay(event):
    global RAID_DELAY
    try:
        
        RAID_DELAY = float(event.pattern_match.group(1))
        await event.edit(f"𝐑ᴀɪᴅ 𝐃ᴇʟᴀʏ 𝐒ᴇᴛ 𝐭ᴏ: `{RAID_DELAY}` 𝐬ᴇᴄᴏɴᴅs!")
        await asyncio.sleep(1.5)
        await event.delete()
    except Exception as e:
        print("Delay Error:", e)
# ---------------------------
# RAID COMMAND (.raid)
# ---------------------------
@YoUrSsS.on(events.NewMessage(pattern=r"^\.raid$", outgoing=True))
async def cmd_read_raid(event):
    global RAID_USERS, RAID_MSG_IDS
    if not event.is_reply:
        return await safe_edit(event, ".𝐑ᴀɪᴅ 𝐑ᴇᴘʟʏ 𝐎ɴ 𝐒ᴏᴍᴇᴏɴᴇ 𝐌sɢ ~")
    
    try:
        reply_msg = await event.get_reply_message()
        target_id = reply_msg.sender_id
        chat_id = event.chat_id
        
        gc_target = (chat_id, target_id)
               
        if gc_target not in RAID_USERS:
            RAID_USERS.append(gc_target)
            
        random_raid = random.choice(RAID_LIST)
        sent_msg = await reply_msg.reply(random_raid)
        RAID_MSG_IDS.append(sent_msg.id)
              
        await event.delete()
        
    except Exception as e:
        print("𝐑ᴀɪᴅ 𝐄ʀʀᴏʀ ~", e)
# ---------------------------
# AUTOMATIC LISTENER
# ---------------------------
@YoUrSsS.on(events.NewMessage(incoming=True))
async def auto_raid_listener(event):
    global RAID_MSG_IDS, RAID_USERS, RAID_DELAY
    
    gc_target = (event.chat_id, event.sender_id)
    
    if gc_target in RAID_USERS:
        try:
            
            await asyncio.sleep(RAID_DELAY)
            
            random_raid = random.choice(RAID_LIST)
            sent_msg = await event.reply(random_raid)
            RAID_MSG_IDS.append(sent_msg.id)
        except Exception as e:
            print("Auto Raid Listener Error:", e)
# ---------------------------
# STOP RAID COMMAND (.unraid)
# ---------------------------
@YoUrSsS.on(events.NewMessage(pattern=r"^\.unraid$", outgoing=True))
async def cmd_unraid(event):
    global RAID_USERS
    try:
        chat_id = event.chat_id
        if event.is_reply:
            reply_msg = await event.get_reply_message()
            target_id = reply_msg.sender_id
            gc_target = (chat_id, target_id)
            
            if gc_target in RAID_USERS:
                RAID_USERS.remove(gc_target)
                await event.edit("𝐑ᴀɪᴅ 𝐒ᴛᴏᴘᴘᴇᴅ 𝐅ᴏʀ 𝐓ʜɪs 𝐔sᴇʀ ~")
            else:
                await event.edit("𝐓ʜɪs 𝐍ɪɢɢᴀ 𝐃ᴏᴇsɴ'ᴛ 𝐈ɴ 𝐋ɪsᴛ ~")
        else:
            RAID_USERS = [pair for pair in RAID_USERS if pair[0] != chat_id]
            await event.edit("𝐀ʟʟ 𝐀ᴄᴛɪᴠᴇ 𝐑ᴀɪᴅ 𝐒ᴛᴏᴘᴘᴇᴅ ~")
            
        await asyncio.sleep(2)
        await event.delete()
        
    except Exception as e:
        print("Unraid Error:", e)
# ---------------------------
# DELETE RAID ONLY (.delete)
# ---------------------------
@YoUrSsS.on(events.NewMessage(pattern=r"^\.delete$", outgoing=True))
async def cmd_delete_raid_only(event):
    global RAID_MSG_IDS, RAID_USERS
    try:
        chat_id = event.chat_id
        await event.delete()
                
        RAID_USERS = [pair for pair in RAID_USERS if pair[0] != chat_id]
        
        if not RAID_MSG_IDS:
            return
            
        await YoUrSsS.delete_messages(chat_id, RAID_MSG_IDS)
        RAID_MSG_IDS.clear()
                    
    except Exception as e:
        print("Raid Delete Error:", e)
# ---------------------------
# LOCK CHAT COMMAND
# ---------------------------
@YoUrSsS.on(events.NewMessage(pattern=r"^\.lock$", outgoing=True))
async def cmd_lock_chat(event):
    try:
        
        lock_rights = types.ChatBannedRights(
            until_date=None,
            send_messages=True,
            send_media=True,
            send_stickers=True,
            send_gifs=True,
            send_games=True,
            send_inline=True,
            embed_links=True
        )
        await YoUrSsS(functions.messages.EditChatDefaultBannedRightsRequest(
            peer=event.chat_id,
            banned_rights=lock_rights
        ))
        await event.edit("𝐆ʀᴏᴜᴘ 𝐂ʜᴀᴛ 𝐋ᴏᴄᴋᴇᴅ 𝐁ʏ 𝐘ᴏᴜ𝐑ꜱ𝐒ꜱ 𝐕16 𝐔𝐬𝐞𝐫 !!")
    except Exception as e:
        await safe_edit(event, f"𝐋ᴏᴄᴋ 𝐄ʀʀᴏʀ ~ `{str(e)[:40]}`")
# ---------------------------
#UNLOCK CHAT COMMAND
# ---------------------------
@YoUrSsS.on(events.NewMessage(pattern=r"^\.unlock$", outgoing=True))
async def cmd_unlock_chat(event):
    try:
        
        unlock_rights = types.ChatBannedRights(
            until_date=None,
            send_messages=False,
            send_media=False,
            send_stickers=False,
            send_gifs=False,
            send_games=False,
            send_inline=False,
            embed_links=False
        )
        await YoUrSsS(functions.messages.EditChatDefaultBannedRightsRequest(
            peer=event.chat_id,
            banned_rights=unlock_rights
        ))
        await event.edit("𝐆ʀᴏᴜᴘ 𝐂ʜᴀᴛ 𝐔ɴʟᴏᴄᴋᴇᴅ 𝐁ʏ 𝐘ᴏᴜ𝐑ꜱ𝐒ꜱ 𝐕16 𝐔𝐬𝐞𝐫 !!")
    except Exception as e:
        await safe_edit(event, f"𝐔ɴʟᴏᴄᴋ 𝐄ʀʀᴏʀ ~ `{str(e)[:40]}`")
# ---------------------------
# CLONE COMMAND
# ---------------------------
@YoUrSsS.on(events.NewMessage(pattern=r"^\.clone$", outgoing=True))
async def cmd_clone(event):
    global MY_OLD_PFP, MY_OLD_NAME, MY_OLD_BIO
    if not event.is_reply:
        return await safe_edit(event, ".𝐂ʟᴏɴᴇ 𝐑ᴇᴘʟʏ 𝐎ɴ 𝐒ᴏᴍᴇᴏɴᴇ 𝐌sɢ ~")
        
    try:
        await event.edit("𝐂ʟᴏɴɪɴɢ...")
        reply_msg = await event.get_reply_message()
        target = await YoUrSsS.get_entity(reply_msg.sender_id)
                
        me = await YoUrSsS.get_me()
        if not MY_OLD_NAME:
            MY_OLD_NAME = f"{me.first_name or ''} {me.last_name or ''}".strip()
            
            full_me = await YoUrSsS(functions.users.GetFullUserRequest(id=me.id))
            MY_OLD_BIO = full_me.full_user.about or ""
                   
            async for photo in YoUrSsS.iter_profile_photos('me', limit=1):
                MY_OLD_PFP = photo
                break
  
        target_full = await YoUrSsS(functions.users.GetFullUserRequest(id=target.id))
        target_bio = target_full.full_user.about or ""
        target_name = target.first_name or ""
        target_last = target.last_name or ""
        
        downloaded_pfp = await YoUrSsS.download_profile_photo(target.id, file="target_pfp.jpg")
        
        await YoUrSsS(functions.account.UpdateProfileRequest(
            first_name=target_name,
            last_name=target_last,
            about=target_bio
        ))
        
        if downloaded_pfp:
            await YoUrSsS(functions.photos.UploadProfilePhotoRequest(
                file=await YoUrSsS.upload_file(downloaded_pfp)
            ))
            
        await event.edit("𝐈ᴅᴇɴᴛɪᴛʏ  𝐂ʟᴏɴᴇᴅ  𝐒ᴜᴄᴄᴇ𝘴𝘴ғᴜʟʟʏ ~")
        
    except Exception as e:
        await safe_edit(event, f"❌ 𝐂𝐥𝐨𝐧𝐞 𝐄𝐫𝐫𝐨𝐫: `{str(e)[:40]}`")
# ---------------------------
#UNCLONE COMMAND
# ---------------------------
@YoUrSsS.on(events.NewMessage(pattern=r"^\.unclone$", outgoing=True))
async def cmd_unclone(event):
    global MY_OLD_PFP, MY_OLD_NAME, MY_OLD_BIO
    if not MY_OLD_NAME:
        return await safe_edit(event, "𝐃ᴀᴛᴀ 𝐍ᴏᴛ 𝐀ᴠᴀɪʟᴀʙʟᴇ ~")
        
    try:
        await event.edit("𝐔ɴᴄʟᴏɴᴇ...")
              
        name_parts = MY_OLD_NAME.split(" ", 1)
        first_name = name_parts[0]
        last_name = name_parts[1] if len(name_parts) > 1 else ""
        
        await YoUrSsS(functions.account.UpdateProfileRequest(
            first_name=first_name,
            last_name=last_name,
            about=MY_OLD_BIO
        ))
                
        if MY_OLD_PFP:
            
            old_pfp_file = await YoUrSsS.download_media(MY_OLD_PFP, file="my_old_pfp.jpg")
            if old_pfp_file:
                await YoUrSsS(functions.photos.UploadProfilePhotoRequest(
                    file=await YoUrSsS.upload_file(old_pfp_file)
                ))
        
        await event.edit("𝐔ɴ𝐂ʟᴏɴᴇᴅ  𝐒ᴜᴄᴄᴇ𝘴𝘴ғᴜʟʟʏ ~")
                
        MY_OLD_NAME = ""
        MY_OLD_BIO = ""
        MY_OLD_PFP = None
        
    except Exception as e:
        await safe_edit(event, f"❌ 𝐔𝐧𝐜𝐥𝐨𝐧𝐞 𝐄𝐫𝐫𝐨𝐫: `{str(e)[:40]}`")
# ---------------------------
#SET SPAM SPEED (.speed)
# ---------------------------
@YoUrSsS.on(events.NewMessage(pattern=r"^\.speed (1\.[0-5]|0\.[5-9])$", outgoing=True))
async def cmd_set_speed(event):
    global SPAM_SPEED
    try:
        SPAM_SPEED = float(event.pattern_match.group(1))
        await event.edit(f"𝐒ᴘᴀᴍ 𝐒ᴘᴇᴇᴅ 𝐒ᴇᴛ ~`{SPAM_SPEED}`")
        await asyncio.sleep(1.5)
        await event.delete()
    except Exception as e:
        print("Speed Error:", e)
# ---------------------------
#SPAM COMMAND
# ---------------------------
@YoUrSsS.on(events.NewMessage(pattern=r"^\.spam (.*)", outgoing=True))
async def cmd_spam(event):
    global SPAM_ACTIVE, SPAM_SPEED, SPAM_MSG_IDS
    spam_text = event.pattern_match.group(1).strip()
    
    if not spam_text:
        return await safe_edit(event, "𝐒ᴘᴀᴍ |𝐓ᴇxᴛ|")
        
    SPAM_ACTIVE = True
    chat_id = event.chat_id
    await event.delete() 
    
    while SPAM_ACTIVE:
        try:
            
            sent_msg = await YoUrSsS.send_message(chat_id, spam_text)
            
            SPAM_MSG_IDS.append(sent_msg.id)
                        
            await asyncio.sleep(SPAM_SPEED) 
        except Exception as e:
            print("Spam Error:", e)
            break
# ---------------------------
# UNSPAM & DELETE
# ---------------------------
@YoUrSsS.on(events.NewMessage(pattern=r"^\.unspam$", outgoing=True))
async def cmd_unspam(event):
    global SPAM_ACTIVE, SPAM_MSG_IDS
    try:
        chat_id = event.chat_id
        SPAM_ACTIVE = False 
                
        await event.delete()
        
        if not SPAM_MSG_IDS:
            return
                    
        await YoUrSsS.delete_messages(chat_id, SPAM_MSG_IDS)
               
        SPAM_MSG_IDS.clear()
        
    except Exception as e:
        print("Unspam/Delete Error:", e)
# ---------------------------
#   MENU COMMAND WITH IMAGE
# ---------------------------
@YoUrSsS.on(events.NewMessage(pattern=r"^\.menu$", outgoing=True))
async def cmd_menu(event):
    try:
        
        await event.delete()
                
        EASY_MENU = """
        ╔═════════════════╗
          
          𝐘ᴏᴜ𝐑ꜱ𝐒ꜱ 𝐕17 𝐔sᴇʀ !!   
                                                 
╚═════════════════╝
       menu ~ 𝑆𝒉𝑜𝑤 𝑇𝒉𝑖𝑠 𝑀𝑒𝑛𝑢
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
addbots ~ |𝐀𝐝𝐝 𝐛𝐨𝐭𝐬|
admin ~ |𝐌𝐚𝐤𝐞 𝐛𝐨𝐭𝐬 𝐀𝐝𝐦𝐢𝐧|
raid ~ |𝐑𝐞𝐩𝐥𝐲 𝐦𝐨𝐝𝐞|
unraid ~ 𝐒𝐭𝐨𝐩
delay ~ 𝐒𝐞𝐭 𝐫𝐚𝐢𝐝 𝐝𝐚𝐥𝐚𝐲
delete ~ 𝐝𝐞𝐥𝐞𝐭𝐞 𝐫𝐚𝐢𝐝 𝐦𝐬𝐠
spam ~ |𝐓𝐞𝐱𝐭|
unspam ~ 𝐒𝐭𝐨𝐩
speed ~ 𝐒𝐞𝐭 𝐬𝐩𝐚𝐦 𝐝𝐞𝐥𝐚𝐲
group ~ |𝐂𝐫𝐞𝐚𝐭𝐞 𝐆𝐫𝐨𝐮𝐩𝐬|
clone ~ 𝕮𝖑𝖔𝖓𝖊
unclone ~ 𝖀𝖓𝖈𝖑ο𝖓𝖊
mute ~ 𝐦𝐮𝐭𝐞 𝐮𝐬𝐞𝐫
unmute ~ 𝐔𝐧𝐦𝐮𝐭𝐞 𝐮𝐬𝐞𝐫
lock ~  𝐋𝐨𝐜𝐤 𝐠𝐫𝐨𝐮𝐩
unlock ~ 𝐔𝐧𝐥𝐨𝐜𝐤 𝐠𝐫𝐨𝐮𝐩
react ~ |𝐄𝐦𝐨𝐣𝐢 𝐑𝐞𝐚𝐜𝐭|
unreact ~ 𝐒𝐭𝐨𝐩
send ~ |𝐃𝐞𝐥𝐞𝐭𝐞 𝐌𝐬𝐠|
unsend ~ 𝐒𝐭𝐨𝐩
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
╔═════════════════╗

          𝐅ᴇᴀʀ𝐎ғ𝐘ᴏᴜ𝐑ꜱ𝐒ꜱ !! 🪽

╚═════════════════╝"""
        
       
        await YoUrSsS.send_file(
            event.chat_id,
            MENU_IMAGE_URL,
            caption=EASY_MENU
        )
        
    except Exception as e:
        print("Menu Error:", e)
        
        try:
            await YoUrSsS.send_message(event.chat_id, EASY_MENU)
        except:
            pass
# -------------------------
#  GROUP CREATOR
# -------------------------
@YoUrSsS.on(events.NewMessage(pattern=r"^\.group(?:\s+(\d+))?$", outgoing=True))
async def cmd_group_creator(event):
    try:
        input_count = event.pattern_match.group(1)

        if not input_count:
            await event.edit(".𝐆c ~ |𝐍ᴜᴍʙᴇʀ|")
            return

        count = int(input_count)

        if count > 30:
            await event.edit("𝐎ɴʟʏ |30| 𝐆ʀᴏᴜᴘ's 𝐈ɴ 𝐎ɴᴇ 𝐓ɪᴍᴇ")
            return

        await event.edit("𝐆ʀᴏᴜᴘ 𝐂ʀᴇᴀᴛɪᴏɴ's 𝐎ɴ")

        created_count = 0

        from telethon.tl.functions.channels import CreateChannelRequest

        for _ in range(count):
            try:
                group_title = "𝐘ᴏᴜ𝐑ꜱ𝐒ꜱ !! 🪽"

                await YoUrSsS(CreateChannelRequest(
                    title=group_title,
                    about="𝐆ʀᴏᴜᴘ 𝐂ʀᴇᴀᴛᴇᴅ 𝐁ʏ 𝐘ᴏᴜ𝐑ꜱ𝐒ꜱ !! 🪽",
                    megagroup=True
                ))

                created_count += 1
                await asyncio.sleep(2.5)

            except Exception as chat_err:
                print(f"Failed to create group: {chat_err}")

                if "FloodWaitError" in str(chat_err):
                    await event.respond("Telegram Limit Hit!")
                    break

                continue

        await event.respond(
            f"𝐆ʀᴏᴜᴘ's 𝐂ʀᴇᴀᴛᴇᴅ 𝐒ᴜᴄᴄᴇssғᴜʟʟʏ {created_count}\n"
            f"𝐍ᴀᴍᴇ : 𝐘ᴏᴜ𝐑ꜱ𝐒ꜱ !! 🪽"
        )

    except Exception as e:
        print("Group Creator Error:", e)

        try:
            await event.edit("𝐒ᴇʀᴠᴇʀ 𝐄ʀʀᴏʀ ~")
        except Exception:
            pass        
# ---------------------------
#  DOT TRIGGER MODE
# ---------------------------
@YoUrSsS.on(events.NewMessage(pattern=r"^\.help$", incoming=True))
async def cmd_dot_trigger(event):
    try:
        
        await event.reply("𝐘ᴏᴜ𝐑ꜱ𝐒ꜱ !! 🪽 𝐊ᴏ 𝐁ᴀᴀᴘ 𝐁ᴀɴᴀ 𝐋ᴇ 𝐑ᴀɴᴅɪ 𝐊ᴇ  𝐁ᴀᴄʜᴇ ~")
    except Exception as e:
        print("Dot Trigger Error:", e)          
# ---------------------------
#                 START 
# ---------------------------
print("𝐘ᴏᴜ𝐑ꜱ𝐒ꜱ  𝐕17 𝐔sᴇʀ !!")
YoUrSsS.start()
print("𝐔sᴇʀ 𝐁ᴏᴛs 𝐎ɴʟɪɴᴇ")
YoUrSsS.run_until_disconnected()