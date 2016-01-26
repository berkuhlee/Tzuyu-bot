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
##    if message.content[0:7] == '!random':
##        t = open('tzuyucommands.txt', 'r+')
##        lines = file_len('tzuyucommands.txt', 'r')
##        r = random.randrange(0, lines)
##
##        
##        yield from client.send_message(message.channel, random_command)
##        
##        
##        if message.content.lower()[1:] == line.split()[0]:
##            new = line.split()
##            user_command = ''
##            for x in new[1:]:
##                user_command += x + ' '
##            yield from client.send_message(message.channel, user_command)

#Make a new discord account and use that info for below.
user = "berkuhlee@live.com" #input email here
passw = "iuiu123" #input password here

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
    thumbsup2 = []
    if message.author == client.user:
        return
    if message.channel.is_private:
        yield from client.send_message(message.channel, 'You cannot use this bot in private messages.')
    ##Tzuyucommands
    if message.content[0:4] == '!add':
        check = True
        new = message.content.split()
        t = open('tzuyucommands.txt', 'r+')
        c = open('commandslist.txt', 'r+')
        try:
            for line in t:
                    if new[1] == line.split()[0]:
                        check = False
                        yield from client.send_message(message.channel, "Command `" + new[1] + "` is already in the commands list.")
            if check == True:
                t.write('\n' + new[1] + ' ' + new[2])
                c2 = c.read()
                c2 = c2[0:(len(c2)-1)]
                c2 += ' ' + new[1]
                print(c2[len(c2)-25:])
                c.truncate(0)
                c.seek(0)
                c.write(c2)
                yield from client.send_message(message.channel, "Added `" + new[1] + "` to the commands list.")

        except IndexError:
            yield from client.send_message(message.channel, 'Please match the format `!add [command] [link]`')
        finally:
            t.close()
            c.close()
    ##Tzuyucommands
    if '!thumbsup' in message.content.lower():
        thumbsup2 = list(thumbsup)
        shuffle(thumbsup2)
        yield from client.send_message(message.channel, thumbsup2.pop())
    elif '!creator' in message.content.lower():
        yield from client.send_message(message.channel,'I was coded by Berk c:')
    elif '!help' in message.content.lower():
        yield from client.send_message(message.channel, helpmessage)
    elif '!commands' in message.content.lower():
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
    elif '!master' in message.content.lower():
        yield from client.send_message(message.channel, 'My master is Berk oppa')
    elif '!minaboys' in message.content.lower():
        yield from client.send_message(message.channel, '(◕‿◕✿) M I N A B O Y S (◠‿◠)✌')
    elif '!iljinsol' in message.content.lower():
        yield from client.send_message(message.channel, 'https://i.imgur.com/1HV4khy.png')
    elif '!2/10' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/tV8dKP1.jpg')
    elif '!freetzuyu' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/X8W4TRj.jpg')
    elif '!yoga' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/9UQuGiT.png')
    elif '!poormina' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/skaJjeM.png')
    elif '!chappa' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/zc6zymM.jpg')
    elif '!server' in message.content.lower():
        yield from client.send_message(message.channel, '`Old Man Cho`')
    elif '!kkt' in message.content.lower():
        yield from client.send_message(message.channel, '`CREDS TO JAY:` http://i.imgur.com/ats5h3v.jpg')
    elif '!balance' in message.content.lower():
        yield from client.send_message(message.channel, "`rip slots, have this instead:` http://40.media.tumblr.com/tumblr_m4mn1rKgWA1rq9gbpo1_540.png")
    elif '!dafuq' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/Zc5Axan.gif")    
    elif '!omo' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/95cTuVx.gif")   
    elif '!xf' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/izoDUtQ.jpg")  
    elif '!bbasae' in message.content.lower():
        yield from client.send_message(message.channel, "https://media.giphy.com/media/26tnkSb3oByAHRXY4/giphy.gif") 
    elif '!waytogo' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/7UsUVHO.gif")  
    elif '!diet' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/fTmOGRL.gif")  
    elif '!pie' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/mg1v2mM.jpg")  
    elif '!fraudy' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/7lYedhK.gif")  
    elif '!treudy' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/27PucbC.gif")  
    elif '!tease' in message.content.lower():
        yield from client.send_message(message.channel, "https://giant.gfycat.com/FortunateMeatyAgama.gif")  
    elif '!weinthere' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/LEHsLeo.gif")  
    elif '!bye' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/DKcQyeo.gif")  
    elif '!gtfo' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/Uh2UN4M.gif")  
    elif '!gyuri' in message.content.lower():
        yield from client.send_message(message.channel, "https://pbs.twimg.com/media/B-2yofOWkAIruY5.jpg")  
    elif '!monstercock' in message.content.lower():
        yield from client.send_message(message.channel, "http://giphy.com/gifs/WAmyJDl6qSR0Y")  
    elif '!joy' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/TkogKax.jpg")
    elif '!taecyeon' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/l6g0bGN.gif")
    elif '!babyboo' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/HYrlyVR.gif")
    elif '!heart' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/JvLvRP9.gif")
    elif '!topmadam' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/aAwItD1.gif")
    elif '!kasper' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/gq3eW8j.gif")
    elif '!gfriend' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/JIgNyiv.jpg")
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

@asyncio.coroutine
def playlist_update():
    yield from client.wait_until_ready()
    count = 0
    time = 0
    while count!= -1:
        if isPlaying is False and firstTime is False and option != 'pause':
            if playlist:
                vce = client.voice
                thing = playlist[0]
                try:
                    path = download_song(thing)
                    if path!='butts!':
                        player = vce.create_ffmpeg_player(path, options='''-filter:a "volume={}"'''.format(volume))
                        
                        player.start()
                        isPlaying = True
                        while thing in playlist: playlist.remove(thing)
                        option = 'sleep'
                    else:
                        while thing in playlist: playlist.remove(thing)
                except:
                    while thing in playlist: playlist.remove(thing)
            elif backuplist:
                shuffle(backuplist)
                thing = backuplist[0]
                try:
                    path = download_song(thing)
                    if path!='butts!':
                        player = vce.create_ffmpeg_player(path, options='''-filter:a "volume={}"'''.format(volume))
                        
                        player.start()
                        isPlaying = True
                        while thing in backuplist: backuplist.remove(thing)
                        option = 'sleep'
                    else:
                        while thing in backuplist: backuplist.remove(thing)
                except:
                    while thing in backuplist: backuplist.remove(thing)
            else:
                with open('backuplist.txt') as f:
                    backuplist = f.readlines()
                for i, item in enumerate(backuplist):
                    backuplist[i] = item.rstrip()
                shuffle(backuplist)
                thing = backuplist[0]
                try:
                    path = download_song(thing)
                    if path!='butts!':
                        player = vce.create_ffmpeg_player(path, options='''-filter:a "volume={}"'''.format(volume))
                        
                        player.start()
                        isPlaying = True
                        while thing in backuplist: backuplist.remove(thing)
                        option = 'sleep'
                    else:
                        while thing in backuplist: backuplist.remove(thing)
                except:
                    while thing in backuplist: backuplist.remove(thing)
        if option == 'sleep' or option == 'skip':
            while option!='skip' and player.is_playing():
                if option == 'pause':
                    player.pause()
                elif option == 'resume':
                    player.resume()
                    option = 'sleep'
                else:
                    yield from asyncio.sleep(1)
            player.stop()
            currentlyPlaying = ''
            isPlaying = False
        elif option == 'pause':
            player.pause()
            while option!='resume':
                yield from asyncio.sleep(1)
            player.resume()
        else:
            yield from asyncio.sleep(1)

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(client.login(user, passw))
    loop.run_until_complete(client.connect())
except Exception:
    loop.run_until_complete(client.close())
finally:
    loop.close()
