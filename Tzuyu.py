import asyncio
import discord
import re
import datetime
import youtube_dl
import os
import traceback
from random import shuffle
import random

#testing random

#Make a new discord account and use that info for below.
user = "email@email.com" #input email here
passw = "password" #input password here

helpmessage = "I was made to meme and track tzuyu. To add a command: `!add [command] [link]. `!commands` for a list of commands slide into your dms."

thumbsup = ['https://i.imgur.com/hFttBo4.png','https://scontent.cdninstagram.com/hphotos-xfp1/t51.2885-15/s320x320/e35/12346292_1555213704768617_309988403_n.jpg',\
            'https://puu.sh/j18wM.jpg', 'https://57.media.tumblr.com/576937e2dc3e53298df6b26a4ec38d47/tumblr_ny8b06hBuQ1ti35kvo6_400.gif',\
            'https://i.imgur.com/hFttBo4.png', 'https://giant.gfycat.com/VacantFavoriteArrowcrab.gif','http://i.imgur.com/OoJLnCh.gifv']

client = discord.Client()

@client.async_event
def on_ready():
    print('Connected! Ready to track tzuyu.')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)
    print('--Server List--')
    for server in client.servers:
        print(server.name)
        
@client.async_event
def on_message(message):
    if message.author == client.user:
        return
    if message.channel.is_private:
        yield from client.send_message(message.channel, 'You sneaky')
    ##Tzuyucommands
    if message.content[0:4] == '!add':
        check = True
        duplicate = False
        new = message.content.split()
        t = open('tzuyucommands.txt', 'r+')
        c = open('commandslist.txt', 'r+')
        try:
            for line in t:
                if new[1] == line.split()[0]:
                    check = False
                    yield from client.send_message(message.channel, "Command `" + new[1] + "` is already in the commands list.")
            if check == True:
                t.write('\n' + message.content[5:])
                c2 = c.read()
                clist = c2.split()
                for x in clist:
                    if new[1] == x:
                        duplicate = True
                        yield from client.send_message(message.channel, "Edited `" + new[1] + "`")
                        
                if duplicate == False:
                    c2 += new[1] + ' ' 
                    print(c2[len(c2)-25:]) #debug
                    _rewrite(c, c2)
                    yield from client.send_message(message.channel, "Added `" + new[1] + "` to the commands list.")

        except IndexError:
            yield from client.send_message(message.channel, 'Please match the format `!add [command] [link]`')
        finally:
            t.close()
            c.close()
    ########
    if message.content[0:7] == '$delete':
        willdelete=0
        t = open('tzuyucommands.txt', 'r+')
        c = open('commandslist.txt', 'r+')
        new = message.content.split()
        newt = 'placeholder'
        for line in t:
            if new[1] == line.split()[0]:
                willdelete=1
            elif line != '':
                newt += '\n' + line.strip('\n')
                
        if willdelete == 1:
            _rewrite(t, newt)
            c2 = c.read()
            clist = c2.split()
            if new[1] in clist:
                clist.remove(new[1])
                c2 = ''
                for thing in clist:
                    c2 += thing + ' '
                _rewrite(c, c2)

            yield from client.send_message(message.channel, "Deleted.")
        else:
            yield from client.send_message(message.channel, "Couldn't find.")

    ########
    if message.content[0:7] == '!random':
        t = open('tzuyucommands.txt', 'r+')
        lines = file_len('tzuyucommands.txt')
        r = random.randrange(0, lines)
        z=0
        for line in t:
            z+=1
            if z == r:
                new = line.split()
                random_command = ''
                for x in new:
                    random_command += x + ' '
                yield from client.send_message(message.channel, random_command)
    ##Tzuyucommands
    thumbsup2 = []
    if '!thumbsup' in message.content.lower():
        thumbsup2 = list(thumbsup)
        shuffle(thumbsup2)
        yield from client.send_message(message.channel, thumbsup2.pop())
    elif '!creator' in message.content.lower():
        yield from client.send_message(message.channel,'I was coded by Berk c:')
    elif '!help' in message.content.lower():
        yield from client.send_message(message.channel, helpmessage)
    elif '!commands' in message.content.lower():
        try:
            c = open('commandslist.txt', 'r+')
            c1 = c.read()
            if len(c1) >= 2000:
                c2 = c1[2000:4000]
                c3 = c1[4000:6000]
                c4 = c1[6000:8000]
                c1 = c1[:2000]
            c.close()
            yield from client.send_message(message.author, c1)
            yield from client.send_message(message.author, c2)
            yield from client.send_message(message.author, c3)
            yield from client.send_message(message.author, c4)
        except:
            pass
    elif '!master' in message.content.lower():
        yield from client.send_message(message.channel, 'My master is Berk oppa')
    elif '!minaboys' in message.content.lower():
        yield from client.send_message(message.channel, '(◕‿◕✿) M I N A B O Y S (◠‿◠)✌')
    elif '!2/10' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/tV8dKP1.jpg')
    elif '!freetzuyu' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/X8W4TRj.jpg')
    elif '!yoga' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/9UQuGiT.png')
    elif '!poormina' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/skaJjeM.png')
    elif '!server' in message.content.lower():
        yield from client.send_message(message.channel, '`Old Man Cho`')
    elif '!kkt' in message.content.lower():
        yield from client.send_message(message.channel, '`CREDS TO JAY:` http://i.imgur.com/ats5h3v.jpg')
    elif '!balance' in message.content.lower():
        yield from client.send_message(message.channel, "`rip slots, have this instead:` http://40.media.tumblr.com/tumblr_m4mn1rKgWA1rq9gbpo1_540.png")
    elif '!dafuq' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/Zc5Axan.gif")
    elif '!xf' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/izoDUtQ.jpg")  
    elif '!bbasae' in message.content.lower():
        yield from client.send_message(message.channel, "https://media.giphy.com/media/26tnkSb3oByAHRXY4/giphy.gif") 
    elif '!waytogo' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/7UsUVHO.gif")    
    elif '!pie' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/mg1v2mM.jpg")  
    elif '!fraudy' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/7lYedhK.gif")  
    elif '!treudy' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/27PucbC.gif")    
    elif '!weinthere' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/LEHsLeo.gif") 
    elif '!gtfo' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/Uh2UN4M.gif")  
    elif '!gyuri' in message.content.lower():
        yield from client.send_message(message.channel, "https://pbs.twimg.com/media/B-2yofOWkAIruY5.jpg")  
    elif '!monstercock' in message.content.lower():
        yield from client.send_message(message.channel, "http://giphy.com/gifs/WAmyJDl6qSR0Y")  
    elif '!taecyeon' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/l6g0bGN.gif")
    elif '!babyboo' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/HYrlyVR.gif")
    elif '!topmadam' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/aAwItD1.gif")
    elif '!kasper' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/gq3eW8j.gif")
    elif '!sheets' in message.content.lower():
        yield from client.send_message(message.channel, "(◕‿◕✿) Aegyo in the streets. Noona in the sheets (◕‿-)")
    elif '!berkgirl' in message.content.lower():
        yield from client.send_message(message.channel, '(◠‿◠)✌ ʜᴇʟʟᴏ ʙᴇʀᴋ, ɪ ᴀᴍ ᴀ ʏᴏᴜɴɢ ʙᴇᴀᴜᴛɪғᴜʟ ᴋᴏʀᴇᴀɴ ɢɪʀʟ  (◡‿◡✿) \
ᴀɴᴅ ɪ ᴡᴏᴜʟᴅ ᴊᴜsᴛ ʟɪᴋᴇ ᴛᴏ ʟᴇᴛ ʏᴏᴜ ᴋɴᴏᴡ ᴛʜᴀᴛ ɪ ᴀᴅᴍɪʀᴇ ʏᴏᴜ ᴇᴠᴇʀʏ ᴅᴀʏ ᴀɴᴅ ɢɪɢɢʟᴇ ᴛᴏ ᴍʏsᴇʟғ \
ʙᴇᴄᴀᴜsᴇ ᴏғ ʜᴏᴡ ɢᴏᴏᴅ ʏᴏᴜ ᴀʀᴇ ᴀᴛ ᴄᴏᴅɪɴɢ ʙᴏᴛꜱ (｡♥‿♥｡).  ɪ ʜᴏᴘᴇ ᴏɴᴇ ᴅᴀʏ ʏᴏᴜ ᴄᴀɴ ᴛᴇᴀᴄʜ ᴍᴇ sᴏᴍᴇᴛʜɪɴɢ (◕‿-)')
    else:
        try:
            if (message.content.lower()[0] == '!') and (message.content.lower() != '!'):
                for line in open('tzuyucommands.txt', 'r+'):
                        if message.content.lower()[1:] == line.split()[0]:
                            new = line.split()
                            user_command = ''
                            for x in new[1:]:
                                user_command += x + ' '
                            yield from client.send_message(message.channel, user_command)
        except IndexError:
            pass

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def _rewrite(file, newfile):
    file.truncate(0)
    file.seek(0)
    file.write(newfile)

@asyncio.coroutine
def playlist_update():
    yield from client.wait_until_ready()
    count = 0
    time = 0
                
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(client.login(user, passw))
    loop.run_until_complete(client.connect())
except Exception:
    loop.run_until_complete(client.close())
finally:
    loop.close()
