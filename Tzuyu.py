import asyncio, discord
import random #randrange, shuffle
import math #math.ceil
import time #time.sleep
import urllib.request, urllib.parse, bs4

#Make a new discord account and use that info for below.
user = "email@email.com" #input email here
passw = "password" #input password here

notifications_file = open('Berknotifications.txt', 'r+')
notifications_dict = {}
for line in notifications_file:
    linesplit = line.split()
    notifications_dict[linesplit[0]] = linesplit[1:]
can_undo = False

version='8.3'

helpmessage = "Hi I'm ChaengBot v"+version+"! I was made by <@68661361537712128> and I have a shitload of kpop commands.\n\
To add a command: `!add [command] [link]`. For a list of commands: `!commands` or use `!search [x]`. \n\
Other commands: `!vlive [x], !random, !thumbsup, !say [x], !latest [#], !search [x]` \n\
Use -MomoBot for `!notification`"

thumbsup = ['https://i.imgur.com/hFttBo4.png','https://scontent.cdninstagram.com/hphotos-xfp1/t51.2885-15/s320x320/e35/12346292_1555213704768617_309988403_n.jpg',\
            'https://puu.sh/j18wM.jpg', 'https://57.media.tumblr.com/576937e2dc3e53298df6b26a4ec38d47/tumblr_ny8b06hBuQ1ti35kvo6_400.gif',\
            'https://i.imgur.com/hFttBo4.png', 'https://giant.gfycat.com/VacantFavoriteArrowcrab.gif','http://i.imgur.com/OoJLnCh.gifv']

client = discord.Client()

@client.async_event
def on_ready():
    print('Connected! (Version: '+version+')= !latest+pms, !search, join, prints+error, history, !vlive')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)
    print('--Server List--')
    for server in client.servers:
        print(server.name)
    print('---------------')
        
@client.async_event
def on_message(message):
    global can_undo
    if message.author == client.user:
        return
    if message.channel.is_private and message.content[0] not in ['!','$','&']:
        if 'discord.gg' in message.content:
            print('Joining new server!')
            yield from client.accept_invite(message.content)
            yield from client.send_message(message.channel, 'Joined! No error check tho')
        else:
            yield from client.send_message(message.channel, helpmessage)
    if '!servers' == message.content[0:8]:
        server_list = [server.name for server in client.servers]
        yield from client.send_message(message.channel, "Servers: " + str(server_list))
####### ^private messages^ ########
    try:
        if '<@139653425972510722>' in message.content or '<@!139653425972510722>' in message.content or '<@&133392980865318912>' in message.content:
            yield from client.send_message(message.channel, helpmessage)
####### vlive             ########
        yield from vlive(message)      
####### Tzuyucommands ########
        if message.content[0:5].lower() == '!add ':
            can_undo = True
            message_list = message.content.lower().split()
            if len(message_list) < 3:
                yield from client.send_message(message.channel, 'Please match the format `!add [command] [link]`')
            elif '\n' in message.content:
                yield from client.send_message(message.channel, 'Please keep the command on one line, do not use linebreaks (Shift-Enter)')
            else:
                check = True
                t = open('tzuyucommands.txt', 'r+')
                c = open('tzuyucommandslist.txt', 'r+')
                try:
                    newcommand = message_list[1].strip('!')
                    for line in t:
                        if newcommand == line.split()[0].lower():
                            check = False
                            yield from client.send_message(message.channel, "Command `{}` is already in the commands list.".format(newcommand) )
                    if check == True:
                        if message_list[1] == newcommand: #if no extra !
                            t.write('\n' + message.content[5:]) #adds link + stuff, not lowercase
                        else:
                            t.write('\n' + message.content[6:])
                        c2 = c.read()
                        c2 += newcommand + ' '
                        _rewrite(c, c2)
                        yield from client.send_message(message.channel, "Added `{}` to the commands list. `$undo` if you made an error, `!save` if correct.".format(newcommand) )
                        print(newcommand +' | added by: '+ message.author.name) #debug

                        ## History
                        h = open('tzuyuhistory.txt', 'r+', encoding="utf-8")
                        h.read()
                        h.write(newcommand +' | added by: '+ message.author.name + '\n')

                except IndexError:
                    yield from client.send_message(message.channel, 'Please match the format `!add [command] [link]`')
                finally:
                    t.close()
                    c.close()
        if message.content[0:5].lower() == '!save':
            can_undo = False
            temp_msg = yield from client.send_message(message.channel, "Locked last command from $undo.")
            yield from asyncio.sleep(3)
            yield from client.delete_message(temp_msg)
            yield from client.delete_message(message)
################
        if message.content[0:8].lower() == '&&delete' or message.content[0:8].lower() == '!delete ':
            if message.content[0:7].lower() == '!delete' and message.author.id != '68661361537712128':
                yield from client.send_message(message.channel, "Must be Bot Owner (Berk).")
            else:
                willdelete=0
                t = open('tzuyucommands.txt', 'r+')
                c = open('tzuyucommandslist.txt', 'r+')
                new = message.content.lower().split()
                newt = '#tzuyu_commands#'
                for line in t:
                    if new[1] == line.split()[0].lower():
                        willdelete=1 # Skips line + confirms delete
                    elif line != '#tzuyu_commands#\n':
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
                    c.close()

                    ## History
                    h = open('tzuyuhistory.txt', 'r+', encoding="utf-8")
                    h.read()
                    h.write(new[1] +' | deleted by: '+ message.author.name + '\n')

                    yield from client.send_message(message.channel, "Deleted `{}`".format(new[1]) )
                    try:
                        print('&&delete on {} by {}'.format(new[1], message.author.name) )
                    except:
                        print('&&delete on {}'.format(new[1]) )
                else:
                    yield from client.send_message(message.channel, "Couldn't find.")

################
        if message.content.split()[0].lower() == '$undo':
            try:
                t = open('tzuyucommands.txt', 'r+')
                c = open('tzuyucommandslist.txt', 'r+')
                if can_undo == False:
                    temp_msg = yield from client.send_message(message.channel, "No new command was added recently.")
                    yield from asyncio.sleep(3)
                    yield from client.delete_message(temp_msg)
                    yield from client.delete_message(message)
                else:
                    can_undo = False
                    #t = open('tzuyucommands.txt', 'r+')
                    #c = open('tzuyucommandslist.txt', 'r+')
                    line_count = file_len('tzuyucommands.txt')
                    new = message.content.split()
                    newt = '#tzuyu_commands#'
                    count = 0
                    for line in t:
                        count += 1
                        if count == line_count: ## if final line, skip
                            pass
                        elif line != '#tzuyu_commands#\n':
                            newt += '\n' + line.strip('\n')

                    _rewrite(t, newt)
                    c2 = c.read()
                    clist = c2.split()
                    undo = clist.pop()
                    c2 = ''
                    for thing in clist:
                        c2 += thing + ' '
                    _rewrite(c,c2)
                    t.close()
                    c.close()

                    # History
                    h = open('tzuyuhistory.txt', 'r+', encoding="utf-8")
                    h.read()
                    h.write('Undid {} at line {} by {}'.format(undo, count, message.author.name) + '\n')

                    temp_msg = yield from client.send_message(message.channel, "Undid `{}`".format(undo))
                    yield from asyncio.sleep(3)
                    yield from client.delete_message(temp_msg)
                    yield from client.delete_message(message)
                    
                    try:
                        if message.channel.is_private:
                            print('Undid {} at line {} by {}'.format(undo, count, message.author.name))
                        else:
                            print('Undid {} at line {} by {} in {}'.format(undo, count, message.author.name, message.server.name))
                    except:
                        print('Undid {} at line {}'.format(undo, count))
            finally:
                t.close()
                c.close()
################
        if message.content[0:7].lower() == '!random' and message.channel.id != '133389185988952064':
            t = open('tzuyucommands.txt', 'r+')
            lines = file_len('tzuyucommands.txt')
            rand_num = random.randrange(0, lines)
            line_num = 0
            for line in t:
                line_num += 1
                if line_num == rand_num:
                    new = line.split()
                    random_command = ''
                    for x in new:
                        random_command += x + ' '
                    yield from client.send_message(message.channel, random_command)
################
        if message.content[0:4] == '!say' and message.channel.id != '185164155592900608' and \
           message.channel.id != '133461932828000257' and message.channel.id != '215359644300869633':
            msg = yield from client.send_message(message.channel, message.content[5:])
################
        if message.content[0:5] == '!eyes':
            msg = yield from client.send_message(message.channel, '<:flippedEyes:211271868643147777>')
            yield from asyncio.sleep(1)
            yield from client.edit_message(msg, ':eyes:')
################
        if message.content[0:5] == '!last' or message.content[0:7] == '!latest':
            t = open('tzuyucommands.txt', 'r+')
            lines = file_len('tzuyucommands.txt')
            msglist = message.content.split()
            skip=0
            if len(msglist) != 1:
                if int(msglist[1]) > lines:
                    yield from client.send_message(message.channel, "Number is too large.")
                    skip=1
                lines -= int(msglist[1])
                print('!last {} used by {}'.format(msglist[1], message.author.name))
            else:
                print('!last command used by {}'.format(message.author.name))

            if skip == 0:
                line_num = 0
                for line in t:
                    line_num += 1
                    if lines == line_num: # if final line
                        new = line.split()
                        command = ''
                        for x in new:
                            command += x + ' '
                        yield from client.send_message(message.channel, command)
################
        if message.content[0:7] == '!search' and message.channel.id != '185164155592900608' and \
           message.channel.id != '133461932828000257' and message.channel.id != '215359644300869633':
            
            msglist = message.content.split()
            if len(msglist) != 2:
                yield from client.send_message(message.channel, 'Please match the format `!search [keyword]`, no brackets.')
            else:
                c = open('tzuyucommandslist.txt', 'r+')
                c2 = c.read()
                command_list = c2.split()
                return_list = []
                for command_name in command_list:
                    if msglist[1] in command_name:
                        return_list.append(command_name)
                c.close()
                if len(str(return_list)) < 2000:
                    yield from client.send_message(message.channel, str(return_list))
                else:
                    yield from client.send_message(message.channel, 'List is too long.')
####### Tzuyucommands End #####
        thumbsup2 = []
        if '!thumbsup' in message.content.lower():
            thumbsup2 = list(thumbsup)
            random.shuffle(thumbsup2)
            yield from client.send_message(message.channel, thumbsup2.pop())
        elif message.content[0:5].lower() == '!help':
            if not message.channel.is_private:
                print('!help command used by {} in {}'.format(message.author.name, message.channel.name))
            yield from client.send_message(message.channel, helpmessage)
        elif message.content[0:9].lower() == '!commands':
            try:
                c = open('tzuyucommandslist.txt', 'r+')
                c0 = c.read()
                yield from client.send_message(message.author, c0[:2000])
                if len(c0) >= 2000:
                    #               1 -> 2 if round returns 3, which prints 3msgs
                    for i in range(1, math.ceil(len(c0)/2000) ):
                        c1 = c0[i*2000:(i+1)*2000]
                        yield from client.send_message(message.author, c1)
                c.close()
            except:
                pass
        elif '!shock' in message.content.lower():
            yield from client.send_file(message.channel, fp='shock.png')
        elif '!thinking' in message.content.lower():
            yield from client.send_file(message.channel, fp='thinking.png')
        elif '!doodoomchit' in message.content.lower():
            yield from client.send_message(message.channel, \
"(＼ヽ                      C\n\
　  ＼＼ .Λ＿Λ.        R\n\
　　  ＼(　ˇωˇ)　     A\n\
　　　   >　⌒ヽ           Y\n\
　　　 / 　 へ＼              O\n\
　　  /　　/　＼＼            N\n\
　　 ﾚ　ノ　　 ヽつ\n\
　　/　/\n\
　 /　/|        P\n\
　(　(ヽ          O\n\
　|　|、＼           P\n\
　| 丿 ＼ ⌒)\n\
　| |　　) /\n\
`ノ ) 　 Lﾉ\n\
(_／")
########################### Handles all commands in the textfile ####################
        else:
            if (message.content[0] == '!') and (message.content != '!'):
                if message.author.id == '68661361537712128' or not message.channel.id == '133389185988952064': #main-chat2: or message.channel.id == '195732639724994560'
                    yield from handle_commands(message)
                    
    except IndexError:
        pass #inline uploads cause this, need to do nothing here
    except discord.errors.Forbidden:
        print('Missing Permissions in {}'.format(message.channel.name) )
    
def handle_commands(message):
    for line in open('tzuyucommands.txt', 'r+'):
        if message.content.lower()[1:] == line.split()[0].lower():
            new = line.split()
            user_command = ''
            for x in new[1:]:
                user_command += x + ' '
            yield from client.send_message(message.channel, user_command)

############################### Helper Methods

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def _rewrite(file, newfile):
    file.truncate(0)
    file.seek(0)
    file.write(newfile)

############################### VLIVE
def vlive(message):
    try:
        if message.content[0:6].lower() == "!vlive":
            if not message.channel.is_private:
                print('{} used by {} in {}'.format(message.content, message.author.name, message.channel.name))
                
            # if this below function raises TypeError, it found no channel, so it defaults to vlive search instead.
            yield from client.send_message(message.channel, 'Found channel. Latest video: ' + getLatestVideo(message.content[7:]) )
                
    except TypeError:
        print('TypeError, trying search')
        try:
            yield from client.send_message(message.channel, 'No Channel found, used vlive search: '+searchVLIVE(message.content[7:]) )
        except TypeError:
            print('TypeError during searchVLIVE. No results.')
            yield from client.send_message(message.channel, "No Channel and No Search Results" )
    except UnicodeEncodeError:
        print('UnicodeUser did: '+ message.content)
        yield from client.send_message(message.channel, 'Found channel. Latest video: ' + getLatestVideo(message.content[7:]) )

# credits to tac
def searchVLIVE(group):
    #search for group page
    search = urllib.request.urlopen("http://www.vlive.tv/search/all?query=" + urllib.parse.quote(group));
    #parse it with bs4
    searchItems = bs4.BeautifulSoup(search.read(), "html.parser");
    #thumb_area holds the latest videos
    firstVid = searchItems.find('a', "thumb_area");
    #data-seq is the url for latest video
    return "http://www.vlive.tv/video/" + firstVid["data-seq"];

# credits to tac
def getLatestVideo(group):
    #search for group page
    search = urllib.request.urlopen("http://www.vlive.tv/search/all?query=" + urllib.parse.quote(group));
    #parse it with bs4
    searchItems = bs4.BeautifulSoup(search.read(), "html.parser");
    #ct_box holds the channel
    channels = searchItems.find_all('a', "ct_box");
    for c in channels:
        if c["data-name"].lower() == group:
            chan = c
            break
    else:
        chan = searchItems.find('a', "ct_box");
    #open channel
    channel = urllib.request.urlopen("http://www.vlive.tv" + chan["href"]);
    chanVids = bs4.BeautifulSoup(channel.read(), "html.parser");
    firstVid = chanVids.find('a', "thumb_area");
    live = firstVid.find("span", "ico_live")
    if live:
        return "```css\nLIVE```\n http://www.vlive.tv/video/" + firstVid["data-seq"];
    return "http://www.vlive.tv/video/" + firstVid["data-seq"];

###############################

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(client.login(user, passw))
    loop.run_until_complete(client.connect())
except Exception:
    loop.run_until_complete(client.close())
finally:
    loop.close()
