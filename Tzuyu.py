import asyncio
import discord
import re
import datetime
import youtube_dl
import os
import traceback
from random import shuffle
import random

#Make a new discord account and use that info for below.
user = "berkuhlee@live.com" #input email here
passw = "iuiu123" #input password here

helpmessage = "`I was made to meme and track tzuyu. !commands`"
commands = "`creator help tzuyu freetzuyu twice myb iljinsol eatshit yoga feels poormina 2/10 chappa redvelvet server jyp kkt thumbsup balance [twicememberhere]\
bae dafuq omo seulgi xf bbasae waytogo diet pie fraudy treudy tease weinthere bye gtfo gyuri dance eunji monstercock joy taecyeon babyboo heart topmadam saranghae\
sheets`"

thumbsup = ['https://i.imgur.com/hFttBo4.png','https://scontent.cdninstagram.com/hphotos-xfp1/t51.2885-15/s320x320/e35/12346292_1555213704768617_309988403_n.jpg',\
            'https://puu.sh/j18wM.jpg', 'https://57.media.tumblr.com/576937e2dc3e53298df6b26a4ec38d47/tumblr_ny8b06hBuQ1ti35kvo6_400.gif',\
            'https://i.imgur.com/hFttBo4.png', 'https://giant.gfycat.com/VacantFavoriteArrowcrab.gif','http://i.imgur.com/OoJLnCh.gifv']
##random = thumbsup[random.randint(0,len(thumbsup)-1)]

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
    if '!thumbsup' in message.content.lower():
        thumbsup2 = list(thumbsup)
        shuffle(thumbsup2)
        yield from client.send_message(message.channel, thumbsup2.pop())
    elif '!creator' in message.content.lower():
        yield from client.send_message(message.channel,'I was coded by Berk c:')
    elif '!help' in message.content.lower():
        yield from client.send_message(message.channel, helpmessage)
    elif '!commands' in message.content.lower():
        yield from client.send_message(message.channel, commands)
    elif '!tzuyu' in message.content.lower():
        yield from client.send_message(message.channel, 'http://www.istzuyustillintwice.com/ http://i.imgur.com/5ccTbp3.png')
    elif '!twice' in message.content.lower():
        yield from client.send_message(message.channel, 'http://puu.sh/mvc45.mp3 http://i.imgur.com/tLoZM5w.png')
    elif '!iljinsol' in message.content.lower():
        yield from client.send_message(message.channel, 'https://i.imgur.com/1HV4khy.png')
    elif '!feels' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/rvyDrsG.png')
    elif '!2/10' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/tV8dKP1.jpg')
    elif '!freetzuyu' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/X8W4TRj.jpg')
    elif '!eatshit' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/kJC6lMr.png')
    elif '!myb' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/WuhxJz7.png')
    elif '!yoga' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/9UQuGiT.png')
    elif '!myb2' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/M6C0knj.png')
    elif '!poormina' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/skaJjeM.png')
    elif '!chappa' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/zc6zymM.jpg')
    elif '!redvelvet' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/1AwZ8vH.png')
    elif '!server' in message.content.lower():
        yield from client.send_message(message.channel, '`Old Man Cho`')
    elif '!jyp' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/Tji2H6D.png')
    elif '!kkt' in message.content.lower():
        yield from client.send_message(message.channel, '`CREDS TO JAY:` http://i.imgur.com/ats5h3v.jpg')
    elif '!balance' in message.content.lower():
        yield from client.send_message(message.channel, "`rip slots, have this instead:` http://40.media.tumblr.com/tumblr_m4mn1rKgWA1rq9gbpo1_540.png")
    elif '!chaeyoung' in message.content.lower():
        yield from client.send_message(message.channel, 'http://i.imgur.com/8inTuJ0.png')
    elif '!momo' in message.content.lower():
        yield from client.send_message(message.channel, 'https://i.imgur.com/2MJaqOe.jpg')
    elif '!sana' in message.content.lower():
        yield from client.send_message(message.channel, 'https://i.imgur.com/dk9TxHl.gifv')
    elif '!mina' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/56a1Qfg.jpg")
    elif '!dahyun' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/GMNlLiU.gifv")
    elif '!jihyo' in message.content.lower():
        yield from client.send_message(message.channel, "https://i.imgur.com/91N9Ww0.gifv")
    elif '!jungyeon' in message.content.lower():
        yield from client.send_message(message.channel, "https://38.media.tumblr.com/1ddcc1e3e0def97fd05d1b04a5728d09/tumblr_nwh4wl5bUp1qi59tso4_540.gif")
    elif '!nayeon' in message.content.lower():
        yield from client.send_message(message.channel, "https://i.imgur.com/NWdSMmx.gifv")
    elif '!bae' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/1USUvjm.gif")
    elif '!dafuq' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/Zc5Axan.gif")    
    elif '!omo' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/95cTuVx.gif")  
    elif '!seulgi' in message.content.lower():
        yield from client.send_message(message.channel, "https://giant.gfycat.com/PeriodicEvilAdeliepenguin.gif")  
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
    elif '!dance' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/jHZgsB6.gif")  
    elif '!eunji' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/axVUOot.jpg")  
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
    elif '!saranghae' in message.content.lower():
        yield from client.send_message(message.channel, "http://i.imgur.com/I80O2pJ.gif")
    elif '!sheets' in message.content.lower():
        yield from client.send_message(message.channel, "(◕‿◕✿) Aegyo in the streets. Noona in the sheets (◕‿-)")



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
