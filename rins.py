# -*- coding: utf-8 -*-
import LINEPY
from LINEPY import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl

#aditmadzs = LineClient()
aditmadzs = LineClient(authToken='EwMOswNrySknlz9DLjP3.zp81iCnJRS6DWRFwE7rbCW.pjYodEkBT4a54+NUparCYdfQvGrY0Pgi/9JYhFwtU4E=')
aditmadzs.log("Auth Token : " + str(aditmadzs.authToken))
channel = LineChannel(aditmadzs)
aditmadzs.log("Channel Access Token : " + str(channel.channelAccessToken))

#ki = LineClient()
ki = LineClient(authToken='EwQwiT6DfOxNgVq4N5k4.6H/R+wrQy2yUyPPXaxh/na.6NRoxk5l1rhrVXJm/ELejdhCF8SP5CChXEVa60xwpic=')
ki.log("Auth Token : " + str(ki.authToken))
channel1 = LineChannel(ki)
ki.log("Channel Access Token : " + str(channel1.channelAccessToken))

#kk = LineClient()
kk = LineClient(authToken='Ew30YvWx8HLYgoafox1f.+llTyZYKm78j6la5VJ62dW.ni81UyZYBJHk7n3rFiy26jGrjPdf0drBE8oN1ywKM3k=')
kk.log("Auth Token : " + str(kk.authToken))
channel1 = LineChannel(kk)
kk.log("Channel Access Token : " + str(channel1.channelAccessToken))

#kc = LineClient()
kc = LineClient(authToken='EwbQ1uHV1VscXP22l6g3.OUlRzsF0pgECqaJ28bzZyW.DEpPFwOb8b8YwbBKjjdzcwop1K6H1uR5iCf+pOqgTdw=')
kc.log("Auth Token : " + str(kc.authToken))
channel1 = LineChannel(kc)
kc.log("Channel Access Token : " + str(channel1.channelAccessToken))

#km = LineClient()
km = LineClient(authToken='EwJkBZO4yMIWg0LLIpn4.isZS+Kbg898rFh+kmWKb1a.xpUABCfeHYY/6URqJnByQ+V3y42Sm8lj5deKtQKU9M8=')
km.log("Auth Token : " + str(km.authToken))
channel1 = LineChannel(km)
km.log("Channel Access Token : " + str(channel1.channelAccessToken))

#ks = LineClient()
ks = LineClient(authToken='EwLmlQvl5L2onz67a9be.xmuvUN9DywEZbNRmpsxChG.AQNksnA/k4V9IoaqgsLYj6Kb8bRi65hVAMXtAKuY82U=')
ks.log("Auth Token : " + str(ks.authToken))
channel1 = LineChannel(ks)
ks.log("Channel Access Token : " + str(channel1.channelAccessToken))

poll = LinePoll(aditmadzs)
call = aditmadzs
creator = ["uac8e3eaf1eb2a55770bf10c3b2357c33"]
owner = ["uac8e3eaf1eb2a55770bf10c3b2357c33"]
admin = ["uac8e3eaf1eb2a55770bf10c3b2357c33"]
staff = ["uac8e3eaf1eb2a55770bf10c3b2357c33"]
mid = aditmadzs.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = km.getProfile().mid
Emid = ks.getProfile().mid
KAC = [ki,kk,kc,km,ks]
ABC = [kc,km,ks]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid]
Aditmadzs = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []

welcome = []
simisimi = []
translateen = []
translateid = []
translateth = []
translatetw = []
translatear = []

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

aditProfile = aditmadzs.getProfile()
myProfile["displayName"] = aditProfile.displayName
myProfile["statusMessage"] = aditProfile.statusMessage
myProfile["pictureStatus"] = aditProfile.pictureStatus

responsename1 = aditmadzs.getProfile().displayName
responsename2 = ki.getProfile().displayName
responsename3 = kk.getProfile().displayName
responsename4 = kc.getProfile().displayName
responsename5 = km.getProfile().displayName
responsename6 = ks.getProfile().displayName

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "lurkt":{},
    "lurkp":{},
    "ROM":{}
}
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('admin.json', 'r') as fp:
    admin = json.load(fp)

Setbot1 = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot1)
Setbot2 = codecs.open("settings.json","r","utf-8")
settings = json.load(Setbot2)
Setbot3 = codecs.open("wait.json","r","utf-8")
wait = json.load(Setbot3)
#Setbot4 = codecs.open("read.json","r","utf-8")
#read = json.load(Setbot4)

mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

# DEF STARTED #
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))

def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def logError(text):
    aditmadzs.log("TERJADI ERROR : " + str(text))
    time_ = datetime.now()
    with open("errorlog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def sendCarousel(data):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/SendMessage"
    data = data
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.10.1'
    headers['Content-Type'] = 'application/json'
    return requests.Session().post(url,data=json.dumps(data),headers=headers)

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)
            time.sleep(0.1)
            page = page[end_content:]
    return items

def backupData():
    try:
        backup1 = Setmain
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup1, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup4 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup4, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def restartBot():
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit' % (days, hours, mins)
    #return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit' % (days, hours, mins)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "「 Mention 」\n Mentioning to {} Member\n\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n" + " //"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n< {} >".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n*Mentioned*"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Sider User 「 {} 」\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "  「 Member Joined 」\n" #.format(str(len(mid))+"」")
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = aditmadzs.getGroup(to)
            mention = "@x "
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nSelamat Datang di : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n {}".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n *yeayea"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Lost Time")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Lost Time")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "  「 Member Leaved 」\n" #.format(str(len(mid))+"」")
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = aditmadzs.getGroup(to)
            mention = "@x "
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"] #+" da: "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n {}".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n Yeayea"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = aditmadzs.getAllContactIds()
        gid = aditmadzs.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"\nTeman : "+str(len(teman))+"\nAktif dalam : \n < "+bot+" >"
        aditmadzs.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╭──「 HELPER 」──" + "\n" + \
                  "│ " + key + "\n" + \
                  "│ " + key + "[0] : Staff Only\n" + \
                  "│ " + key + "[1] : All Can Used\n" + \
                  "│ " + key + "\n" + \
                  "│ " + key + "[1] Tagall/Mentioning\n" + \
                  "│ " + key + "[1] Ceksider on/off\n" + \
                  "│ " + key + "[1] Ceksider\n" + \
                  "│ " + key + "[1] @bye [without induk]\n" + \
                  "│ " + key + "[1] @byeall [with induk]\n" + \
                  "│ " + key + "[1] About\n" + \
                  "│ " + key + "[0] Securelist\n" + \
                  "│ " + key + "[0] Securestatus\n" + \
                  "│ " + key + "[0] @Status\n" + \
                  "│ " + key + "[0] @Refresh\n" + \
                  "│ " + key + "[0] Muteall\n" + \
                  "│ " + key + "[0] Unmuteall\n" + \
                  "│ " + key + "\n" + \
                  "│ " + key + "[ Made with Loves by @! ]\n" + \
                  "╰──「 ENDED HELPER COMMANDS 」──"
    return helpMessage

def helpz():
    key = Setmain["keyCommand"]
    key = key.title()
    helpzMessage = "╭──「 // INSERT HELPER COMMANDS // 」──" + "\n" + \
                  "│ " + key + "Help\n" + \
                  "│ " + key + "Help bot\n" + \
                  "│ " + key + "Translate\n" + \
                  "│ " + key + "Meme\n" + \
                  "│ " + key + "Me\n" + \
                  "│ " + key + "Mymid\n" + \
                  "│ " + key + "Mid「@」\n" + \
                  "│ " + key + "Info 「@」\n" + \
                  "│ " + key + "Kick1 「@」\n" + \
                  "│ " + key + "Mybot\n" + \
                  "│ " + key + "Status\n" + \
                  "│ " + key + "Status translate\n" + \
                  "│ " + key + "About\n" + \
                  "│ " + key + "Restart\n" + \
                  "│ " + key + "Runtime\n" + \
                  "│ " + key + "Creator\n" + \
                  "│ " + key + "Respon\n" + \
                  "│ " + key + "Speed/Sp\n" + \
                  "│ " + key + "Sprespon\n" + \
                  "│ " + key + "Tagall\n" + \
                  "│ " + key + "join dit\n" + \
                  "│ " + key + "Assist join\n" + \
                  "│ " + key + "Ginfo\n" + \
                  "│ " + key + "Open\n" + \
                  "│ " + key + "Close\n" + \
                  "│ " + key + "Url grup\n" + \
                  "│ " + key + "Reject\n" + \
                  "│ " + key + "Gruplist\n" + \
                  "│ " + key + "Infogrup「angka」\n" + \
                  "│ " + key + "Infomem「angka」\n" + \
                  "│ " + key + "Lurking「on/off」\n" + \
                  "│ " + key + "Lurkers\n" + \
                  "│ " + key + "Sider「on/off」\n" + \
                  "│ " + key + "Updatefoto\n" + \
                  "│ " + key + "Updategrup\n" + \
                  "│ " + key + "Updatebot\n" + \
                  "│ " + key + "Broadcast:「Text」\n" + \
                  "│ " + key + "Setkey「New Key」\n" + \
                  "│ " + key + "Mykey\n" + \
                  "│ " + key + "Resetkey\n" + \
                  "╰───「 ENDED HELPER COMMANDS 」──"
    return helpzMessage

def fun():
    key = Setmain["keyCommand"]
    key = key.title()
    funMessage =  "╭──「 // INSERT FUN COMMANDS // 」──" + "\n" + \
                  "│ " + key + "Musik:「Judul Lagu」\n" + \
                  "│ " + key + "Musik2:「Judul Lagu」\n" + \
                  "│ " + key + "Playlist「Nama Penyanyi」\n" + \
                  "│ " + key + "Ytmp3:「Judul Lagu」\n" + \
                  "│ " + key + "Ytmp4:「Judul Video\n" + \
                  "│ " + key + "Meme@Nama@Teks1@Teks2\n" + \
                  "│ " + key + "1cak\n" + \
                  "│ " + key + "Profilesmule:「ID Smule」\n" + \
                  "│ " + key + "Randomnumber:「Nmor-Nmor」\n" + \
                  "│ " + key + "Gimage:「Keyword」\n" + \
                  "│ " + key + "Img food:「Nama Makanan」\n" + \
                  "│ " + key + "Cekig:「ID IG」\n" + \
                  "│ " + key + "Profileig:「Nama IG」\n" + \
                  "│ " + key + "Cekdate:「tgl-bln-thn」\n" + \
                  "│ " + key + "Spamtag:「jumlahnya」\n" + \
                  "│ " + key + "Spamtag「@」\n" + \
                  "│ " + key + "Spamcall:「jumlahnya」\n" + \
                  "│ " + key + "Spamcall\n" + \
                  "╰───「 // ENDED FUN COMMANDS // 」──"
    return funMessage

def protects():
    key = Setmain["keyCommand"]
    key = key.title()
    protectsMessage =  "╭──「 // INSERT PROTECT COMMANDS // 」──" + "\n" + \
                       "│ " + key + "Notag 「 on/off 」\n" + \
                       "│ " + key + "Proall 「 on/off 」\n" + \
                       "│ " + key + "Antiinviting  「 on/off 」\n" + \
                       "│ " + key + "Anticancelling 「 on/off 」\n" + \
                       "│ " + key + "Antijoin 「 on/off 」\n" + \
                       "│ " + key + "Antikicking 「 on/off 」\n" + \
                       "│ " + key + "Gticketpro 「 on/off 」\n" + \
                       "╰───「 // ENDED PROTECT COMMANDS // 」──"
    return protectsMessage

def sett():
    key = Setmain["keyCommand"]
    key = key.title()
    settMessage =  "╭──「 // INSERT SETTING COMMANDS // 」──" + "\n" + \
                   "│ " + key + "Unsend「on/off」\n" + \
                   "│ " + key + "Jointicket「on/off」\n" + \
                   "│ " + key + "Sticker「on/off」\n" + \
                   "│ " + key + "Respon「on/off」\n" + \
                   "│ " + key + "Respongift「on/off」\n" + \
                   "│ " + key + "Contact「on/off」\n" + \
                   "│ " + key + "Autojoin「on/off」\n" + \
                   "│ " + key + "Autoadd「on/off」\n" + \
                   "│ " + key + "Welcome「on/off」\n" + \
                   "│ " + key + "Simi「on/off」\n" + \
                   "│ " + key + "Autoleave「on/off」\n" + \
                   "╰───「 // ENDED SETTING COMMANDS // 」──"
    return settMessage

def staffs():
    key = Setmain["keyCommand"]
    key = key.title()
    staffsMessage =  "╭──「 STAFFS COMMANDS 」──" + "\n" + \
                     "│ " + key + "Clearban\n" + \
                     "│ " + key + "Adminc\n" + \
                     "│ " + key + "Blc\n" + \
                     "│ " + key + "Staffc\n" + \
                     "│ " + key + "Botsc\n" + \
                     "│ " + key + "Proall\n" + \
                     "│ " + key + "Projoin\n" + \
                     "│ " + key + "Procancelling\n" + \
                     "│ " + key + "Proinviting\n" + \
                     "│ " + key + "Prokicking\n" + \
                     "│ " + key + "Progticket\n" + \
                     "│ " + key + "???\n" + \
                     "│ " + key + "rin spro\n" + \
                     "│ " + key + "rin admins\n" + \
                     "│ " + key + "rin botlist\n" + \
                     "│ " + key + "rin bye\n" + \
                     "│ " + key + "allleave to\n" + \
                     "│ " + key + "2leave to\n" + \
                     "│ " + key + "1leave to\n" + \
                     "│ " + key + "ndchange 1\n" + \
                     "│ " + key + "rinchange\n" + \
                     "│ " + key + "infomem (numb)\n" + \
                     "│ " + key + "infogrup (number)\n" + \
                     "│ " + key + "resetprefix\n" + \
                     "│ " + key + "setprefix\n" + \
                     "│ " + key + "myprefix\n" + \
                     "│ " + key + "rinbc:\n" + \
                     "│ " + key + "Info @\n" + \
                     "│ " + key + "Status\n" + \
                     "│ " + key + "2j\n" + \
                     "│ " + key + "2bye\n" + \
                     "│ " + key + "sini\n" + \
                     "│ " + key + "Admin:add\n" + \
                     "│ " + key + "Admin:rem\n" + \
                     "│ " + key + "Staff:add\n" + \
                     "│ " + key + "Staff:rem\n" + \
                     "│ " + key + "Bot:add\n" + \
                     "│ " + key + "Bot:rem\n" + \
                     "│ " + key + "Adminadd「@」\n" + \
                     "│ " + key + "Adminrem「@」\n" + \
                     "│ " + key + "Staffadd「@」\n" + \
                     "│ " + key + "Staffrem「@」\n" + \
                     "│ " + key + "Botadd「@」\n" + \
                     "│ " + key + "Botrem「@」\n" + \
                     "│ " + key + "Refresh\n" + \
                     "│ " + key + "Listbot\n" + \
                     "│ " + key + "Listadmin\n" + \
                     "│ " + key + "Listprotect\n" + \
                     "│ " "< Refresh > After Use!\n" + \
                     "╰───「 ENDED STAFF COMMANDS 」──"
    return staffsMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "╭──「 // INSERT RINDA'S COMMANDS // 」──" + "\n" + \
                   "│ " + key + "Mytoken\n" + \
                   "│ " + key + "Cek sider\n" + \
                   "│ " + key + "Cek spam\n" + \
                   "│ " + key + "Cek pesan\n" + \
                   "│ " + key + "Cek respon\n" + \
                   "│ " + key + "Cek welcome\n" + \
                   "│ " + key + "Cek leave\n" + \
                   "│ " + key + "Set sider:「Text」\n" + \
                   "│ " + key + "Set spam:「Text」\n" + \
                   "│ " + key + "Set pesan:「Text」\n" + \
                   "│ " + key + "Set respon:「Text」\n" + \
                   "│ " + key + "Set welcome:「Text」\n" + \
                   "│ " + key + "Set leave:「Text」\n" + \
                   "│ " + key + "Myname:「Nama」\n" + \
                   "│ " + key + "Rinda:「Nama」\n" + \
                   "│ " + key + "Rin:「Nama」\n" + \
                   "│ " + key + "Rindachange\n" + \
                   "│ " + key + "Rinchange\n" + \
                   "│ " + key + "Gift:「Mid korban」「Jumlah」\n" + \
                   "│ " + key + "Spam:「Mid korban」「Jumlah」\n" + \
				   "│ " + key + "Spamtag:「jumlahnya」\n" + \
                   "│ " + key + "Spamcall:「jumlahnya」\n" + \
                   "│ " + key + "Spamcall\n" + \
				   "│ " + key + "Updatefoto\n" + \
                   "│ " + key + "Updategrup\n" + \
                   "│ " + key + "Updatebot\n" + \
                   "│ " + key + "Broadcast:「Text」\n" + \
                   "│ " + key + "Setkey「New Key」\n" + \
                   "│ " + key + "Mykey\n" + \
                   "│ " + key + "Resetkey\n" + \
				   "│ " + key + "Hapus chat\n" + \
                   "│ " + key + "Remove chat\n" + \
				   "│ " + key + "Leave:「Namagrup」\n" + \
                   "│ " + key + "Blc\n" + \
                   "│ " + key + "Ban:on\n" + \
                   "│ " + key + "Unban:on\n" + \
                   "│ " + key + "Ban「@」\n" + \
                   "│ " + key + "Unban「@」\n" + \
                   "│ " + key + "Talkban「@」\n" + \
                   "│ " + key + "Untalkban「@」\n" + \
                   "│ " + key + "Talkban:on\n" + \
                   "│ " + key + "Untalkban:on\n" + \
                   "│ " + key + "Banlist\n" + \
                   "│ " + key + "Talkbanlist\n" + \
                   "│ " + key + "Clearban\n" + \
                   "│ " + key + "Refresh\n" + \
                   "╰───「 // ENDED RINDA'S COMMANDS // 」──"
    return helpMessage1

def terj():
    key = Setmain["keyCommand"]
    key = key.title()
    terjMessage =  "╭──「 // INSERT TRANSL COMMANDS // 」──" + "\n" + \
                   "│ " + key + "\n" + \
                   "│ " + key + "Terjemah ke Arab on/off\n" + \
                   "│ " + key + "Terjemah ke Indo on/off\n" + \
                   "│ " + key + "Terjemah ke Eng on/off\n" + \
                   "│ " + key + "\n" + \
                   "│ " + key + "[ Rinda Made with Loves by @! ]\n" + \
                   "╰───「 // ENDED TRANSL COMMANDS // 」──"
    return terjMessage

def terjemahan():
    terjemahanMessage2 = """
╭──「 // INSERT TRANSL COMMANDS // 」──
│
│ Terjemah ke indo on/off
│ Terjemah ke eng on/off
│ Terjemah ke arab on/off
│
╰───「 // ENDED TRANSL COMMANDS // 」──
"""
    return terjemahanMessage2

def infomeme():
    helpMessage2 = """
──「 // INSERT MEME COMMANDS // 」──
│ Buzz
│ Spongebob
│ Patrick
│ Doge
│ Joker
│ Xzibit
│ You_tried
│ blb
│ wonka
│ keanu
│ cryingfloor
│ disastergirl
│ facepalm
│ fwp
│ grumpycat
│ captain
│ mmm
│ rollsafe
│ sad-obama
│ sad-clinton
│ aag
│ sarcasticbear
│ sk
│ sparta
│ sad
│ contoh:
│ Meme@buzz@lu tau?@gatau
╰───「 // ENDED MEME COMMANDS // 」──
"""
    return helpMessage2

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return

        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if aditmadzs.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            aditmadzs.reissueGroupTicket(op.param1)
                            X = aditmadzs.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            aditmadzs.updateGroup(X)
                            aditmadzs.sendMessage(op.param1, "Oops, Qr Secure アクティブ")
                            aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ki.updateGroup(X)
                                aditmadzs.sendMessage(op.param1, "Oops, Qr Secure アクティブ")
                                aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kk.updateGroup(X)
                                    aditmadzs.sendMessage(op.param1, "Oops, Qr Secure アクティブ")
                                    aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kc.updateGroup(X)
                                        aditmadzs.sendMessage(op.param1, "Oops, Qr Secure アクティブ")
                                        aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if ks.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            ks.reissueGroupTicket(op.param1)
                                            X = ks.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            ks.updateGroup(X)
                                            aditmadzs.sendMessage(op.param1, "Oops, Qr Secure アクティブ")
                                            aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if km.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                km.reissueGroupTicket(op.param1)
                                                X = km.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                km.updateGroup(X)
                                                aditmadzs.sendMessage(op.param1, "Oops, Qr Secure アクティブ")
                                                aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        pass

        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ginfo = aditmadzs.getGroup(op.param1)
                        aditmadzs.sendMessage(op.param1,"さようなら\n   " +str(ginfo.name))
                        aditmadzs.leaveGroup(op.param1)
                    else:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ginfo = aditmadzs.getGroup(op.param1)
                        aditmadzs.sendMessage(op.param1,"こんにちはすべて " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ginfo = aditmadzs.getGroup(op.param1)
                        aditmadzs.sendMessage(op.param1,"こんにちはすべて")
                    else:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ginfo = aditmadzs.getGroup(op.param1)
                        aditmadzs.sendMessage(op.param1,"こんにちはすべて")
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"さようなら\n   " +str(ginfo.name))
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"こんにちはすべて " + str(ginfo.name))
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.sendMessage(op.param1,"さようなら\n   " +str(ginfo.name))
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.sendMessage(op.param1,"こんにちはすべて " + str(ginfo.name))

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = aditmadzs.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                        aditmadzs.sendMessage(op.param1, "Opps, Cancel Invite アクティブ")
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                            aditmadzs.sendMessage(op.param1, "Opps, Cancel Invite アクティブ")
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                aditmadzs.sendMessage(op.param1, "Opps, Cancel Invite アクティブ")
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                    aditmadzs.sendMessage(op.param1, "Opps, Cancel Invite アクティブ")
                                except:
                                    pass

        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = aditmadzs.getGroup(op.param1)
                contact = aditmadzs.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])
                aditmadzs.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                aditmadzs.sendMessage(op.param1, "Opps, Is Listed on Blacklist im sorry.")
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = aditmadzs.getGroup(op.param1)
                contact = aditmadzs.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                welcomeMembers(op.param1, [op.param2])
                aditmadzs.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        aditmadzs.sendMessage(op.param1, wait["message"])
                        #sendMention(op.param1, wait["message"])
                        #sendMentions(op.param1, "Hei @!\nTerimakasi sudah menambahkan Rinda sebagai Teman.")
                        #AutoAddMsgs(op.param1)

#===========KICK============#
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    aditmadzs.sendMessage(op.param1, "Oops, Secure2 アクティブです im sorry.")
                    aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                else:
                    pass

#===========Cancel============#

        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[Zmid])
                            ki.sendMessage(op.param1, "Oops, Secure3 アクティブです im sorry")
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[Zmid])
                                kk.sendMessage(op.param1, "Oops, Secure3 アクティブです im sorry")
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[Zmid])
                                    kc.sendMessage(op.param1, "Oops, Secure3 アクティブです im sorry")
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        km.kickoutFromGroup(op.param1,[op.param2])
                                        km.inviteIntoGroup(op.param1,[Zmid])
                                        km.sendMessage(op.param1, "Oops, Secure3 アクティブです im sorry")
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            ks.kickoutFromGroup(op.param1,[op.param2])
                                            ks.inviteIntoGroup(op.param1,[Zmid])
                                            ks.sendMessage(op.param1, "Oops, Secure3 アクティブです im sorry")
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                                aditmadzs.inviteIntoGroup(op.param1,[Zmid])
                                                aditmadzs.sendMessage(op.param1, "Oops, Secure3 アクティブです im sorry")
                                        except:
                                            pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            aditmadzs.acceptGroupInvitation(op.param1)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                aditmadzs.acceptGroupInvitation(op.param1)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    km.inviteIntoGroup(op.param1,[op.param3])
                                    aditmadzs.acceptGroupInvitation(op.param1)
                                    km.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ks.inviteIntoGroup(op.param1,[op.param3])
                                        aditmadzs.acceptGroupInvitation(op.param1)
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            ki.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)
                                            aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.kickoutFromGroup(op.param1,[op.param2])                                    
                                            G = ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            ki.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                aditmadzs.acceptGroupInvitation(op.param1)
                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                    aditmadzs.acceptGroupInvitation(op.param1)
                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    km.inviteIntoGroup(op.param1,[op.param3])
                                    ki.acceptGroupInvitation(op.param1)
                                    km.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ks.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = kk.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kk.updateGroup(G)
                                            Ticket = kk.reissueGroupTicket(op.param1)
                                            aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.kickoutFromGroup(op.param1,[op.param2])                                    
                                            G = kk.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kk.updateGroup(G)
                                            Ticket = kk.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kk.inviteIntoGroup(op.param1,[op.param3])
                                                ki.acceptGroupInvitation(op.param1)
                                                kk.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                    ki.acceptGroupInvitation(op.param1)
                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    km.inviteIntoGroup(op.param1,[op.param3])
                                    kk.acceptGroupInvitation(op.param1)
                                    km.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ks.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = kc.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kc.updateGroup(G)
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                            aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            G = kc.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kc.updateGroup(G)
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kc.inviteIntoGroup(op.param1,[op.param3])
                                                kk.acceptGroupInvitation(op.param1)
                                                kc.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                                    kk.acceptGroupInvitation(op.param1)
                                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        km.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                        km.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    km.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                    km.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ks.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = km.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            km.updateGroup(G)
                                            Ticket = km.reissueGroupTicket(op.param1)
                                            aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            G = km.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            km.updateGroup(G)
                                            Ticket = km.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                km.inviteIntoGroup(op.param1,[op.param3])
                                                kc.acceptGroupInvitation(op.param1)
                                                km.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                                    kc.acceptGroupInvitation(op.param1)
                                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ks.inviteIntoGroup(op.param1,[op.param3])
                        km.acceptGroupInvitation(op.param1)
                        ks.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            km.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                km.acceptGroupInvitation(op.param1)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    km.inviteIntoGroup(op.param1,[op.param3])
                                    km.acceptGroupInvitation(op.param1)
                                    km.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ks.inviteIntoGroup(op.param1,[op.param3])
                                        km.acceptGroupInvitation(op.param1)
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = ks.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            ks.updateGroup(G)
                                            Ticket = ks.reissueGroupTicket(op.param1)
                                            aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            G = ks.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            ks.updateGroup(G)
                                            Ticket = ks.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                ks.inviteIntoGroup(op.param1,[op.param3])
                                                km.acceptGroupInvitation(op.param1)
                                                ks.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                                    km.acceptGroupInvitation(op.param1)
                                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    pass
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        aditmadzs.findAndAddContactsByMid(op.param1,admin)
                        aditmadzs.inviteIntoGroup(op.param1,admin)
                        aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        km.findAndAddContactsByMid(op.param1,admin)
                                        km.inviteIntoGroup(op.param1,admin)
                                        km.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ks.findAndAddContactsByMid(op.param1,admin)
                                            ks.inviteIntoGroup(op.param1,admin)
                                            ks.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.findAndAddContactsByMid(op.param1,staff)
                            kk.inviteIntoGroup(op.param1,staff)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.findAndAddContactsByMid(op.param1,staff)
                                kc.inviteIntoGroup(op.param1,staff)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    km.findAndAddContactsByMid(op.param1,staff)
                                    km.inviteIntoGroup(op.param1,staff)
                                    km.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ks.findAndAddContactsByMid(op.param1,staff)
                                        ks.inviteIntoGroup(op.param1,staff)
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass

                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["ADITMADZSreadPoint"]:
                   if op.param2 in Setmain["ADITMADZSreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["ADITMADZSreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                random.choice(ABC).sendMessage(op.param1, "In the Blacklist User im sorry")
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = aditmadzs.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = aditmadzs.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        aditmadzs.sendImageWithURL(op.param1, image)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == '// Image Below //':
                                ginfo = aditmadzs.getGroup(at)
                                arifAR = aditmadzs.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "╭─「 Pesan Dihapus 」\n│ Pengirim : "
                                ret_ = "│ Di Grup : {}".format(str(ginfo.name))
                                ret_ += "\n│ Tipe Pesan : "
                                ret_ += "\n╰────────"
                                ry = str(arifAR.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':arifAR.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                aditmadzs.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                aditmadzs.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = aditmadzs.getGroup(at)
                                arifAR = aditmadzs.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "╭──「 Pesan Dihapus 」\n"
                                ret_ += "│ Pengirim : {}".format(str(arifAR.displayName))
                                ret_ += "\n│ Di Grup : {}".format(str(ginfo.name))
                                #ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n│ Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                ret_ += "\n│ Tipe Pesan : Teks"
                                ret_ += "\n╰────────"
                                aditmadzs.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = aditmadzs.getGroup(at)
                                arifAR = aditmadzs.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "╭──「 Pesan Dihapus 」\n"
                                ret_ += "│ Pengirim : {}".format(str(arifAR.displayName))
                                ret_ += "\n│ Di Grup : {}".format(str(ginfo.name))
                                ret_ += "\n│ Tipe Pesan : Stiker"
                                #ret_ += "\n╰────────"
                                #ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                #aditmadzs.sendMessage(at, str(ret_), contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                #sendMention(at, str(ret_))
                                aditmadzs.sendMessage(at, str(ret_))
                                aditmadzs.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 25:
           if wait["selfbot"] == True:
               msg = op.message
               if msg.to in simisimi:
                   try:
                       if msg.text is not None:
                           simi = msg.text
                           r = requests.get("http://corrykalam.pw/api/chatbot.php?text="+simi)
                           data = r.text
                           data = json.loads(data)
                           if data["status"] == 200:
                               aditmadzs.sendMessage(msg.to, str(data["answer"]))
                   except Exception as error:
                       pass

               if msg.to in translateen:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='en')
                           A = hasil.text
                           aditmadzs.sendMessage(msg.to, "Inggris : "+A+" \n\nJika ingin Mematikan AutoTranslate ketik\nTransto eng*off")
                   except Exception as error:
                       pass

               if msg.to in translateid:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='id')
                           A = hasil.text
                           aditmadzs.sendMessage(msg.to, "Indonesia : "+A+" \n\nJika ingin Mematikan AutoTranslate ketik\nTransto indo*off")
                   except Exception as error:
                       pass

               if msg.to in translatear:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='ar')
                           A = hasil.text
                           aditmadzs.sendMessage(msg.to, "Arab : "+A+" \n\nJika ingin Mematikan AutoTranslate ketik\nTransto arab*off")
                   except Exception as error:
                       pass

        if op.type == 25 or op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           aditmadzs.sendMessage(msg.to, wait["Respontag"])
                           aditmadzs.sendMessage(msg.to, None, contentMetadata={"STKID":"21715710","STKPKGID":"9662","STKVER":"2"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentiongift"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           idth = ["a0768339-c2d3-4189-9653-2909e9bb6f58","ec4a14ea-7437-407b-aee7-96b1cbbc1b4b","f35bd31f-5ec7-4b2f-b659-92adf5e3d151","ba1d5150-3b5f-4768-9197-01a3f971aa34","2b4ccc45-7309-47fe-a006-1a1edb846ddb","168d03c3-dbc2-456f-b982-3d6f85f52af2","d4f09a5f-29df-48ac-bca6-a204121ea165","517174f2-1545-43b9-a28f-5777154045a6","762ecc71-7f71-4900-91c9-4b3f213d8b26","2df50b22-112d-4f21-b856-f88df2193f9e"]
                           plihth = random.choice(idth)
                           jenis = ["5","6","7","8"]
                           plihjenis = random.choice(jenis)
                           aditmadzs.sendMessage(msg.to, "Hah?\nCek Pm")
                           aditmadzs.sendMessage(msg._from, None, contentMetadata={"PRDID":plihth,"PRDTYPE":"THEME","MSGTPL":plihjenis}, contentType=9)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           aditmadzs.sendMessage(msg.to, "Jgn tag Rindaaaaaaaaa")
                           aditmadzs.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,"  「 ID Sticker 」\nSTKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = aditmadzs.getContact(msg.contentMetadata["mid"])
                        path = aditmadzs.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        aditmadzs.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        aditmadzs.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}

            if msg.contentType == 1:
                    path = aditmadzs.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'// Image Below //',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n│ Alamat Stiker : line://shop/detail/{}".format(pkg_id)
                   #ret_ = "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n╰────────"
                   #ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   #ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   #ret_ += "\n <Sticker Url> : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = aditmadzs.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}


            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = aditmadzs.getContact(msg.contentMetadata["mid"])
                        path = aditmadzs.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        aditmadzs.sendMessage(msg.to," Nama : " + msg.contentMetadata["displayName"] + "\n MID : " + msg.contentMetadata["mid"] + "\n Status : " + contact.statusMessage + "\n Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        aditmadzs.sendImageWithURL(msg.to, image)
#===========ADD BOT============#
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        aditmadzs.sendMessage(msg.to,"Sudah menjadi Bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        aditmadzs.sendMessage(msg.to,"+1 Bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        aditmadzs.sendMessage(msg.to,"-1 Bot")
                    else:
                        wait["dellbots"] = True
                        aditmadzs.sendMessage(msg.to,"Bukan Teman Rinda")
#===========ADD STAFF============#
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        aditmadzs.sendMessage(msg.to,"Dia staff Rinda:3")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        aditmadzs.sendMessage(msg.to,"+1 Rinda Staffs")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        aditmadzs.sendMessage(msg.to,"-1 Rinda Staffs")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        aditmadzs.sendMessage(msg.to,"Bukan staff Rinda:3")
#===========ADD ADMIN============#
                 if msg._from in owner:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        aditmadzs.sendMessage(msg.to,"Dia Admin Rinda:3")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        aditmadzs.sendMessage(msg.to,"+1 Rinda Admins")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        aditmadzs.sendMessage(msg.to,"-1 Rinda Admins")
                    else:
                        wait["delladmin"] = True
                        aditmadzs.sendMessage(msg.to,"Bukan Admin Rinda:3")
#===========ADD BLACKLIST============#
                 if msg._from in owner:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        aditmadzs.sendMessage(msg.to,"Dia sudah masuk Blacklist Rindaaaa")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        aditmadzs.sendMessage(msg.to,"+1 BL Rinda")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        aditmadzs.sendMessage(msg.to,"-1 BL Rinda")
                    else:
                        wait["dblacklist"] = True
                        aditmadzs.sendMessage(msg.to,"Dia Tidak ada di BL Rindaaaa")
#===========TALKBAN============#
                 if msg._from in owner:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        aditmadzs.sendMessage(msg.to,"Dia sudah masuk ke Tban Rindaaa")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        aditmadzs.sendMessage(msg.to,"+1 Tban Rinda")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        aditmadzs.sendMessage(msg.to,"-1 Tban Rinda")
                    else:
                        wait["Talkdblacklist"] = True
                        aditmadzs.sendMessage(msg.to,"Dia Tidak ada di Tban Rindaa")
#===========UPDATE FOTO============#
               if msg.contentType == 1:
                 if msg._from in owner:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = aditmadzs.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            aditmadzs.sendMessage(msg.to, "Gambar Ditambahkan")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in owner:
                   if settings["groupPicture"] == True:
                     path = aditmadzs.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     #G = aditmadzs.getGroup(msg.to)
                     aditmadzs.updateGroupPicture(msg.to, path)
                     aditmadzs.sendMessage(msg.to, "Foto grup berhasil Diterapkan menjadi")
                     #aditmadzs.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)

               if msg.contentType == 1:
                   if msg._from in owner:
                       if mid in Setmain["ADITMADZSfoto"]:
                            path = aditmadzs.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][mid]
                            aditmadzs.updateProfilePicture(path)
                            aditmadzs.sendMessage(msg.to,"Gambar berhasil Diterapkan")

               if msg.contentType == 1:
                 if msg._from in owner:
                        if Amid in Setmain["ADITMADZSfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Gambar berhasil diterapkan menjadi")

               if msg.contentType == 1:
                 if msg._from in owner:
                   if settings["changePicture"] == True:
                     path1 = aditmadzs.downloadObjectMsg(msg_id)
                     path2 = ki.downloadObjectMsg(msg_id)
                     path3 = kk.downloadObjectMsg(msg_id)
                     path4 = kc.downloadObjectMsg(msg_id)
                     path5 = km.downloadObjectMsg(msg_id)
                     path6 = ks.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     aditmadzs.updateProfilePicture(path1)
                     ki.updateProfilePicture(path2)
                     kk.updateProfilePicture(path3)
                     kc.updateProfilePicture(path4)
                     km.updateProfilePicture(path5)
                     ks.updateProfilePicture(path6)
                     aditmadzs.sendMessage(msg.to, "Ava telah Diubah")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        aditmadzs.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               helpMessage = help()
                               poey = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                               creator = aditmadzs.getContact(poey)
                               sendMentions(to, str(helpMessage), [poey])
                              #aditmadzs.sendMessage(msg.to, str(helpMessage))

                        if cmd == "Terjemahans":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               terjMessage = terj()
                               aditmadzs.sendMessage(msg.to, str(terjMessage))

                        if cmd == "helpz":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpzMessage = helpz()
                               aditmadzs.sendMessage(msg.to, str(helpzMessage))

                        if cmd == "more sett":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               settMessage = sett()
                               aditmadzs.sendMessage(msg.to, str(settMessage))

                        if cmd == "more fun":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               funMessage = fun()
                               aditmadzs.sendMessage(msg.to, str(funMessage))

                        if cmd == "more protect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               protectsMessage = protects()
                               aditmadzs.sendMessage(msg.to, str(protectsMessage))

                        if cmd == "more staff":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               staffsMessage = staffs()
                               aditmadzs.sendMessage(msg.to, str(staffsMessage))

                        if cmd == "unmuteall":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                aditmadzs.sendMessage(msg.to, "Aktif Kembaliiii")

                        elif cmd == "muteall":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                aditmadzs.sendMessage(msg.to, "Dimatikan Sementara")

                        elif cmd == "look errorlog":
                            if msg._from in admin:
                                with open('logError.txt', 'r') as er:
                                        error = er.read()
                                aditmadzs.sendMessage(to, str(error))

                        elif cmd == "more":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               aditmadzs.sendMessage(msg.to, str(helpMessage1))

                        elif cmd == "meme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage2 = infomeme()
                               aditmadzs.sendMessage(msg.to, str(helpMessage2))

                        elif cmd == "translate":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpTranslate = translate()
                               aditmadzs.sendMessage(msg.to, str(helpTranslate))

                        if cmd == "unsend on":
                            if msg._from in admin:
                                wait["unsend"] = True
                                aditmadzs.sendMessage(msg.to, "Deteksi Unsend Diaktifkan")

                        if cmd == "unsend off":
                            if msg._from in admin:
                                wait["unsend"] = False
                                aditmadzs.sendMessage(msg.to, "Deteksi Unsend Dinonaktifkan")

                        elif cmd == "@status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "\n  「 STATUS 」\n"
                                if wait["unsend"] == True: md+="Unsend 「 ON 」\n"
                                else: md+="Unsend 「 OFF 」\n"
                                if wait["sticker"] == True: md+="Sticker 「 ON 」\n"
                                else: md+="Sticker 「 OFF 」\n"
                                if wait["contact"] == True: md+="Contact 「 ON 」\n"
                                else: md+="Contact 「 OFF 」\n"
                                if wait["talkban"] == True: md+="Talkban 「 ON 」\n"
                                else: md+="Talkban 「OFF 」\n"
                                if wait["Mentionkick"] == True: md+="Notag 「 ON 」\n"
                                else: md+="Notag 「 OFF 」\n"
                                if wait["detectMention"] == True: md+=" Respon 「 ON 」\n"
                                else: md+="Respon 「 OFF 」\n"
                                if wait["Mentiongift"] == True: md+="Respongift 「 ON 」\n"
                                else: md+="Respongift 「 OFF 」\n"
                                if wait["autoJoin"] == True: md+="Autojoin 「 ON 」\n"
                                else: md+="Autojoin 「 OFF 」\n"
                                if settings["autoJoinTicket"] == True: md+="Jointicket 「 ON 」\n"
                                else: md+="Jointicket 「 OFF 」\n"
                                if wait["autoAdd"] == True: md+="Autoadd 「 ON 」\n"
                                else: md+="Autoadd 「 OFF 」\n"
                                if msg.to in welcome: md+="Welcome 「 ON 」\n"
                                else: md+="Welcome 「 OFF 」\n"
                                if msg.to in simisimi: md+="Simisimi 「 ON 」\n"
                                else: md+="Simisimi 「 OFF 」\n"
                                if wait["autoLeave"] == True: md+="Autoleave 「 ON 」\n"
                                else: md+="Autoleave 「 OFF 」\n"
                                if msg.to in protectqr: md+="S5 「 ON 」\n"
                                else: md+="S5 「 OFF 」\n"
                                if msg.to in protectjoin: md+="S4 「 ON 」\n"
                                else: md+="S4 「 OFF 」\n"
                                if msg.to in protectkick: md+="S2 「 ON 」\n"
                                else: md+="S2 「 OFF 」\n"
                                if msg.to in protectcancel: md+="S3 「 ON 」\n"
                                else: md+="S3 「 OFF 」\n"
                                if msg.to in protectinvite: md+="S1 「 ON 」\n"
                                else: md+="S1 「 OFF 」\n"
                                aditmadzs.sendMessage(msg.to, md)

                        elif cmd == "status translate":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "\n  「 STATUS TRANSLATE 」\n"
                                if msg.to in translateen: md+="English 「 ON 」\n"
                                else: md+="English「 OFF 」\n"
                                if msg.to in translateid: md+="Indonesia 「 ON 」\n"
                                else: md+="Indonesia「 OFF 」\n"
                                if msg.to in translatear: md+="Arab 「 ON 」\n"
                                else: md+="Arab「 OFF 」\n"
                                aditmadzs.sendMessage(msg.to, md)

                        elif cmd.startswith("aboutszs"):
                            try:
                                arr = []
                                Ownerz = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                creator = aditmadzs.getContact(Ownerz)
                                #contact = aditmadzs.getContact(puyMid)
                                grouplist = aditmadzs.getGroupIdsJoined()
                                contactlist = aditmadzs.getAllContactIds()
                                blockedlist = aditmadzs.getBlockedContactIds()
                                ret_ = " "
                                ret_ += " Bot Name : {}".format(contact.displayName)
                                ret_ += "\n  In Groups : {}".format(str(len(grouplist)))
                                ret_ += "\n  Friends : {}".format(str(len(contactlist)))
                                ret_ += "\n  Blocked Account : {}".format(str(len(blockedlist)))
                                #ret_ += "\n  [ About Selfbot ]"
                                #ret_ += "\n  Version : Premium"
                                #ret_ += "\n  Creator : {}".format(creator.displayName)
                                #ret_ += "\n  Creator : @!".format(Owner)
                                aditmadzs.sendMessage(to, str(ret_))
                                #puy.sendMessage(to, "「 Read Text Below 」")
                                sendMentions(to, "「 About Rinda 」\n\nThe Beginning of this Bot Comes from Helloworld, I'm just Reworked This!\n\nOf Course Special Thanks To HelloWorld, And the Friends Around Me!\n\n*Rinda:3 Made with Loves by @!", [Ownerz])
                            except Exception as e:
                                aditmadzs.sendMessage(msg.to, str(e))

                        elif text.lower() == "Haisz":
                            #key = eval(msg.contentMetadata["MENTION"])
                            #key1 = key["MENTIONEES"][0]["M"]
                            mii = aditmadzs.getContact(sender)
                            aditmadzs.sendMessage(sender, "Hai juga "+str(mii.displayName))

                        elif text.lower() == "about":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               poey = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                               creator = aditmadzs.getContact(poey)
                               sendMentions(to, "「 About 」\n\nThe Beginning of this Bot Comes from Helloworld, I'm just Reworked This!\n\nOf Course Special Thanks To HelloWorld, And the Friends Around Me!\n\n*Made with Loves by @!", [poey])

                        elif text.lower() == "mymid":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = aditmadzs.getContact(key1)
                               aditmadzs.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = aditmadzs.getContact(key1)
                               aditmadzs.sendMessage(msg.to, " Nama : "+str(mi.displayName)+"\n Mid : " +key1+"\n Status : "+str(mi.statusMessage))
                               #aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               #if "videoProfile='{" in str(aditmadzs.getContact(key1)):
                               #    aditmadzs.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               #else:
                               #    aditmadzs.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "teams":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Dmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Emid}
                               aditmadzs.sendMessage1(msg)

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   aditmadzs.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   ki.removeAllMessages(op.param2)
                                   aditmadzs.sendMessage(msg.to,"Chat dibersihkan...")
                               except:
                                   pass

                        elif cmd.startswith("rinbc: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = aditmadzs.getGroupIdsJoined()
                               for group in saya:
                                   aditmadzs.sendMessage(group, pesan)

                        elif text.lower() == "myprefix":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「 Prefix 」\nPrefix sekarang 「 " + str(Setmain["keyCommand"]) + " 」")

                        elif cmd.startswith("setprefix "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   aditmadzs.sendMessage(msg.to, "Gagal menerapkan Prefix")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   aditmadzs.sendMessage(msg.to, "「 Prefix 」\nPrefix diterapkan menjadi 「 {} 」".format(str(key).lower()))

                        elif text.lower() == "resetprefix":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               aditmadzs.sendMessage(msg.to, "「 Prefix 」\nPrefix telah direset")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               aditmadzs.sendMessage(msg.to, "Restarted")
                               Setmain["restartPoint"] = msg.to
                               restartBot()

                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "  「 Runtime 」\n" +waktu(eltime)
                               aditmadzs.sendMessage(msg.to,bot)

                        elif cmd == "get latest announce":
                          if wait["selfbot"] == True:
                            try:
                                gett = aditmadzs.getChatRoomAnnouncements(msg.to)
                                for a in gett:
                                    aa = aditmadzs.getContact(a.creatorMid).displayName
                                    bb = a.contents
                                    cc = bb.link
                                    textt = bb.text
                                    aditmadzs.sendText(msg.to, "「 Announcement 」\n\nFind Text Here - \n" + str(cc) + "\n\nDari: " + str(aa))
                                    break
                            except Exception as e:
                                aditmadzs.sendText(msg.to, "  「 Announcement 」\nAnnounce Tidak Ditemukan:((((")

                        elif cmd == "ginfo2":
                          if msg._from in admin:
                            try:
                                G = aditmadzs.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(aditmadzs.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(int(G.createdTime) / 1000)))
                                aditmadzs.sendMessage(msg.to, " 「 GRUP INFO 」\n\n Nama : {}".format(G.name)+ "\n ID : {}".format(G.id)+ "\n Pembuat : {}".format(G.creator.displayName)+ "\n Dibuat Pada : {}".format(str(timeCreated))+ "\n Anggota : {}".format(str(len(G.members)))+ "\n Calon Anggota : {}".format(gPending)+ "\n Url : {}".format(gQr)+ "\n Ticket : {}".format(gTicket) + "\nKontak Pembuat Grup Below")
                                aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                #aditmadzs.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                aditmadzs.sendMessage(msg.to, str(e))

                        elif cmd.startswith("ginfo "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = aditmadzs.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = aditmadzs.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(aditmadzs.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += " 「 GRUP INFO 」"
                                ret_ += "\n Nama : {}".format(G.name)
                                ret_ += "\n ID : {}".format(G.id)
                                ret_ += "\n Pembuat : {}".format(gCreator)
                                ret_ += "\n Dibuat Pada : {}".format(str(timeCreated))
                                ret_ += "\n Anggota : {}".format(str(len(G.members)))
                                ret_ += "\n Calon Anggota : {}".format(gPending)
                                ret_ += "\n Url : {}".format(gQr)
                                ret_ += "\n Ticket : {}".format(gTicket)
                                ret_ += ""
                                aditmadzs.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd == "love":
                            _session = requests.session()
                            url = " https://game.linefriends.com/cdn/jbp-lcs/"
                            headers = {
                             "Content-Type": "application/json",
                             "User-Agent": "Mozilla/5.0 (Linux;Android 5.1.1; SM-J320G Build/LMY47V; wv)AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 Line/8.2.0"
                            }
                            data = {
                             "cc": "4C4M/U0Dh/enUIYeJk/36rzWRcfg+yDaxKKObQjA3TYvwacjzXQQIfvpERQ/Wx276v5K67WCC3mq5X2KVZmncPAtXpfV3qe4boi7oPxxq3gQPnUJgmuz56XmkhiGZWF8zCur1/oREnxaKf5N3hVxYFrheXM9MvLESulavEelOsZhExzJl6a8FXi9x5QdrOuPIitk+TuXQ4g6O9nhG8aQurl0Cm0ykve/WFUl4JuFqcMFzv8awDdbJmUfmDCjvn5YHA3PNnObgr6xeUnqZuBRB6ookxI4/Oh+Iu+tjT0VtP0X9D5GdtDpAjpu1WmVwkB61cnSDAiiUPGsFyAifO5fHQ8bF3m1gacbCbsYcl+i1IQ",
                             "to": to,
                             "messages": [
                              {
                               "type": "image",
                               "size": "full",
                               "originalContentUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/27342584/IOS/sticker_animation@2x.png",
                               "previewImageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/27342584/IOS/sticker_animation@2x.png"
                              }
                            ]
                          }

                            anu = _session.get(url, headers=headers)
                            data = json.dumps(data)
                            send = _session.post("https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage", data=data, headers=headers)
                            print(send.json())

                        elif cmd == "hue":
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "4C4M/U0Dh/enUIYeJk/36rzWRcfg+yDaxKKObQjA3TYvwacjzXQQIfvpERQ/Wx276v5K67WCC3mq5X2KVZmncPAtXpfV3qe4boi7oPxxq3gQPnUJgmuz56XmkhiGZWF8zCur1/oREnxaKf5N3hVxYFrheXM9MvLESulavEelOsZhExzJl6a8FXi9x5QdrOuPIitk+TuXQ4g6O9nhG8aQurl0Cm0ykve/WFUl4JuFqcMFzv8awDdbJmUfmDCjvn5YHA3PNnObgr6xeUnqZuBRB6ookxI4/Oh+Iu+tjT0VtP0X9D5GdtDpAjpu1WmVwkB61cnSDAiiUPGsFyAifO5fHQ8bF3m1gacbCbsYcl+i1IQ",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                        "type": "text",
                                                        "text": "Helloooooooo",
                                                        "size": "md",
                                                        "align": "center",
                                                        "color": "#ff0000",
                                                        #"wrap": true,
                                                  }
                                                ]
                                              },
                                              "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "spacer",
                                                    "size": "xl"
                                                  },
                                                  {
                                                    "type": "button",
                                                    "action": {
                                                      "type": "uri",
                                                      "label": "Tap",
                                                      "uri": "line.me/ti/p/~yapuy"
                                                    },
                                                    "style": "primary",
                                                    "color": "#0000ff"
                                                  }
                                                ]
                                            }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)

                        elif cmd == "hure":
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "4C4M/U0Dh/enUIYeJk/36rzWRcfg+yDaxKKObQjA3TYvwacjzXQQIfvpERQ/Wx276v5K67WCC3mq5X2KVZmncPAtXpfV3qe4boi7oPxxq3gQPnUJgmuz56XmkhiGZWF8zCur1/oREnxaKf5N3hVxYFrheXM9MvLESulavEelOsZhExzJl6a8FXi9x5QdrOuPIitk+TuXQ4g6O9nhG8aQurl0Cm0ykve/WFUl4JuFqcMFzv8awDdbJmUfmDCjvn5YHA3PNnObgr6xeUnqZuBRB6ookxI4/Oh+Iu+tjT0VtP0X9D5GdtDpAjpu1WmVwkB61cnSDAiiUPGsFyAifO5fHQ8bF3m1gacbCbsYcl+i1IQ",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "carousel",
                                        "contents": [
                                          {
                                            "type": "bubble",
                                            "body": {
                                              "type": "box",
                                              "layout": "horizontal",
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "Heiii",
                                                  #"wrap": "true"
                                                }
                                              ]
                                            },
                                            "footer": {
                                              "type": "box",
                                              "layout": "horizontal",
                                              "contents": [
                                                {
                                                  "type": "button",
                                                  "style": "primary",
                                                  "action": {
                                                    "type": "uri",
                                                    "label": "Go",
                                                    "uri": "https://example.com"
                                                  }
                                                }
                                              ]
                                            }
                                          },
                                          {
                                            "type": "bubble",
                                            "body": {
                                              "type": "box",
                                              "layout": "horizontal",
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "Hello, World!",
                                                  #"wrap": "true"
                                                }
                                              ]
                                            },
                                            "footer": {
                                              "type": "box",
                                              "layout": "horizontal",
                                              "contents": [
                                                {
                                                  "type": "button",
                                                  "style": "primary",
                                                  "action": {
                                                    "type": "uri",
                                                    "label": "Go",
                                                    "uri": "https://example.com"
                                                  }
                                                }
                                              ]
                                            }
                                          }
                                        ]
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)

                        elif cmd == "huee":
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "4C4M/U0Dh/enUIYeJk/36rzWRcfg+yDaxKKObQjA3TYvwacjzXQQIfvpERQ/Wx276v5K67WCC3mq5X2KVZmncPAtXpfV3qe4boi7oPxxq3gQPnUJgmuz56XmkhiGZWF8zCur1/oREnxaKf5N3hVxYFrheXM9MvLESulavEelOsZhExzJl6a8FXi9x5QdrOuPIitk+TuXQ4g6O9nhG8aQurl0Cm0ykve/WFUl4JuFqcMFzv8awDdbJmUfmDCjvn5YHA3PNnObgr6xeUnqZuBRB6ookxI4/Oh+Iu+tjT0VtP0X9D5GdtDpAjpu1WmVwkB61cnSDAiiUPGsFyAifO5fHQ8bF3m1gacbCbsYcl+i1IQ",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                     "type": "image",
                                                     "url": "https://d1xmenocyxrtc7.cloudfront.net/wp-content/uploads/2018/01/lulu1.jpg",
                                                     "size": "full"
                                                  }
                                                ]
                                              },
                                              "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "spacer",
                                                    "size": "xl"
                                                  },
                                                  {
                                                    "type": "button",
                                                    "action": {
                                                      "type": "uri",
                                                      "label": "Tap",
                                                      "uri": "line.me/ti/p/~yapuy"
                                                    },
                                                    "style": "primary",
                                                    "color": "#0000ff"
                                                  }
                                                ]
                                            }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)

                        elif cmd == "flexie":
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "4C4M/U0Dh/enUIYeJk/36rzWRcfg+yDaxKKObQjA3TYvwacjzXQQIfvpERQ/Wx276v5K67WCC3mq5X2KVZmncPAtXpfV3qe4boi7oPxxq3gQPnUJgmuz56XmkhiGZWF8zCur1/oREnxaKf5N3hVxYFrheXM9MvLESulavEelOsZhExzJl6a8FXi9x5QdrOuPIitk+TuXQ4g6O9nhG8aQurl0Cm0ykve/WFUl4JuFqcMFzv8awDdbJmUfmDCjvn5YHA3PNnObgr6xeUnqZuBRB6ookxI4/Oh+Iu+tjT0VtP0X9D5GdtDpAjpu1WmVwkB61cnSDAiiUPGsFyAifO5fHQ8bF3m1gacbCbsYcl+i1IQ",
                                "to": to,
                                "messages": [
                                    {
                                      "type": "bubble",
                                      "hero": {
                                        "type": "image",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_2_restaurant.png",
                                        "size": "full",
                                        "aspectRatio": "20:13",
                                        "aspectMode": "cover",
                                        "action": {
                                          "type": "uri",
                                          "uri": "https://linecorp.com"
                                        }
                                      },
                                      "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "md",
                                        "action": {
                                          "type": "uri",
                                          "uri": "https://linecorp.com"
                                        },
                                        "contents": [
                                          {
                                            "type": "text",
                                            "text": "Brown's Burger",
                                            "size": "xl",
                                            "weight": "bold"
                                          },
                                          {
                                            "type": "box",
                                            "layout": "vertical",
                                            "spacing": "sm",
                                            "contents": [
                                              {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                  {
                                                    "type": "icon",
                                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_regular_32.png"
                                                  },
                                                  {
                                                    "type": "text",
                                                    "text": "$10.5",
                                                    "weight": "bold",
                                                    "margin": "sm"
                                                    #"flex": 0
                                                  },
                                                  {
                                                    "type": "text",
                                                    "text": "400kcl",
                                                    "size": "sm",
                                                    "align": "end",
                                                    "color": "#aaaaaa"
                                                  }
                                                ]
                                              },
                                              {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                  {
                                                    "type": "icon",
                                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_large_32.png"
                                                  },
                                                  {
                                                    "type": "text",
                                                    "text": "$15.5",
                                                    "weight": "bold",
                                                    "margin": "sm"
                                                    #"flex": 0
                                                  },
                                                  {
                                                    "type": "text",
                                                    "text": "550kcl",
                                                    "size": "sm",
                                                    "align": "end",
                                                    "color": "#aaaaaa"
                                                  }
                                                ]
                                              }
                                            ]
                                          },
                                          {
                                            "type": "text",
                                            "text": "Sauce, Onions, Pickles, Lettuce & Cheese",
                                            #"wrap": true,
                                            "color": "#aaaaaa",
                                            "size": "xxs"
                                          }
                                        ]
                                      },
                                      "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                          {
                                            "type": "spacer",
                                            "size": "xxl"
                                          },
                                          {
                                            "type": "button",
                                            "style": "primary",
                                            "color": "#905c44",
                                            "action": {
                                              "type": "uri",
                                              "label": "Add to Cart",
                                              "uri": "https://linecorp.com"
                                            }
                                          }
                                        ]
                                      }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)

                        elif cmd == "hueez":
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "4C4M/U0Dh/enUIYeJk/36rzWRcfg+yDaxKKObQjA3TYvwacjzXQQIfvpERQ/Wx276v5K67WCC3mq5X2KVZmncPAtXpfV3qe4boi7oPxxq3gQPnUJgmuz56XmkhiGZWF8zCur1/oREnxaKf5N3hVxYFrheXM9MvLESulavEelOsZhExzJl6a8FXi9x5QdrOuPIitk+TuXQ4g6O9nhG8aQurl0Cm0ykve/WFUl4JuFqcMFzv8awDdbJmUfmDCjvn5YHA3PNnObgr6xeUnqZuBRB6ookxI4/Oh+Iu+tjT0VtP0X9D5GdtDpAjpu1WmVwkB61cnSDAiiUPGsFyAifO5fHQ8bF3m1gacbCbsYcl+i1IQ",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "image",
                                                    "url": "https://example.com/flex/images/image.jpg",
                                                    "size": "full"
                                                  }
                                                ]
                                              },
                                              "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "spacer",
                                                    "size": "xl"
                                                  },
                                                  {
                                                    "type": "button",
                                                    "action": {
                                                      "type": "uri",
                                                      "label": "Tap",
                                                      "uri": "line.me/ti/p/~yapuy"
                                                    },
                                                    "style": "primary",
                                                    "color": "#0000ff"
                                                  }
                                                ]
                                            }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)

                        elif cmd == "sad":
                              try:
                                  arr = "line://ti/p/~{}".format(aditmadzs.getProfile().userid)
                                  data = {
                                    "cc": "4C4M/U0Dh/enUIYeJk/36rzWRcfg+yDaxKKObQjA3TYvwacjzXQQIfvpERQ/Wx276v5K67WCC3mq5X2KVZmncPAtXpfV3qe4boi7oPxxq3gQPnUJgmuz56XmkhiGZWF8zCur1/oREnxaKf5N3hVxYFrheXM9MvLESulavEelOsZhExzJl6a8FXi9x5QdrOuPIitk+TuXQ4g6O9nhG8aQurl0Cm0ykve/WFUl4JuFqcMFzv8awDdbJmUfmDCjvn5YHA3PNnObgr6xeUnqZuBRB6ookxI4/Oh+Iu+tjT0VtP0X9D5GdtDpAjpu1WmVwkB61cnSDAiiUPGsFyAifO5fHQ8bF3m1gacbCbsYcl+i1IQ",
                                    "to": to,
                                    "messages": [{
                                        "type": "template",
                                        "altText": "Mengirim Sticker",
                                        "template": {
                                            "type": "image_carousel",
                                            "columns": [
                                                {
                                                  "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/21831484/IOS/sticker_animation@2x.png;compress=true",
                                                  "action": {
                                                  "type": "uri",
                                                  " ": " ",
                                                  "uri": "http://line.me/ti/p/~yapuy"
                                                  }
                                                }
                                            ]
                                        }
                                    }]
                                  }
                                  sendCarousel(data)
                              except Exception as error:
                                  aditmadzs.sendMessage(msg.to, "error\n" + str(error))

                        if cmd == "heii":
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "4C4M/U0Dh/enUIYeJk/36rzWRcfg+yDaxKKObQjA3TYvwacjzXQQIfvpERQ/Wx276v5K67WCC3mq5X2KVZmncPAtXpfV3qe4boi7oPxxq3gQPnUJgmuz56XmkhiGZWF8zCur1/oREnxaKf5N3hVxYFrheXM9MvLESulavEelOsZhExzJl6a8FXi9x5QdrOuPIitk+TuXQ4g6O9nhG8aQurl0Cm0ykve/WFUl4JuFqcMFzv8awDdbJmUfmDCjvn5YHA3PNnObgr6xeUnqZuBRB6ookxI4/Oh+Iu+tjT0VtP0X9D5GdtDpAjpu1WmVwkB61cnSDAiiUPGsFyAifO5fHQ8bF3m1gacbCbsYcl+i1IQ",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "template",
                                        "altText": "Puy",
                                        "template": {
                                            "type": "carousel",
                                            "actions": [],
                                            "columns": [
                                                {
                                                    "thumbnailImageUrl": "https://media1.tenor.com/images/b84ff412072364cc6e73d841d08b6cbd/tenor.gif",
                                                    "title": "My Instagram",
                                                    "text": " ",
                                                    "actions": [
                                                        {
                                                            "type": "uri",
                                                            "label": "Visit",
                                                            "uri": "https://instagram.com/muh.khadaffy"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "thumbnailImageUrl": "https://media1.tenor.com/images/64fc8769fecea1d3446b1e9039b22e4c/tenor.gif",
                                                    "title": "My Github",
                                                    "text": " ",
                                                    "actions": [
                                                        {
                                                            "type": "uri",
                                                            "label": "Visit",
                                                            "uri": "http://github.com/heefpuy"
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)

                        elif cmd.startswith("imagehd "):
                            query = text.replace("imagehd ","")
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            #query = text.replace("imagehd ","")
                            cond = query.split("|")
                            search = str(cond[0])
                            result = requests.get("https://api.eater.tech/wallp/{}".format(str(search)))
                            data = result.text
                            data = json.loads(data)
                            if data["result"] != []:
                                ret_ = []
                                for fn in data["result"]:
                                    if 'http://' in fn["link"]:
                                        pass
                                    else:
                                        if len(ret_) >= 20:
                                            pass
                                        else:
                                            ret_.append({
                                                "imageUrl": "{}".format(str(fn["link"])),
                                                "action": {
                                                    "type": "uri",
                                                    "label": "View detail",
                                                    "uri": "{}".format(str(fn["link"]))
                                                    }
                                                }
                                            )
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {
                                        "cc": "4C4M/U0Dh/enUIYeJk/36rzWRcfg+yDaxKKObQjA3TYvwacjzXQQIfvpERQ/Wx276v5K67WCC3mq5X2KVZmncPAtXpfV3qe4boi7oPxxq3gQPnUJgmuz56XmkhiGZWF8zCur1/oREnxaKf5N3hVxYFrheXM9MvLESulavEelOsZhExzJl6a8FXi9x5QdrOuPIitk+TuXQ4g6O9nhG8aQurl0Cm0ykve/WFUl4JuFqcMFzv8awDdbJmUfmDCjvn5YHA3PNnObgr6xeUnqZuBRB6ookxI4/Oh+Iu+tjT0VtP0X9D5GdtDpAjpu1WmVwkB61cnSDAiiUPGsFyAifO5fHQ8bF3m1gacbCbsYcl+i1IQ",
                                        "to": to,
                                        "messages": [{
                                            "type": "template",
                                            "altText": "Puy",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }]
                                    }
                                    data = json.dumps(data)
                                    sendPost = _session.post(url, data=data, headers=headers)

                        elif cmd == "image carousel":
                            _session = requests.session()
                            image = "https://img00.deviantart.net/14c2/i/2015/238/b/4/we_bare_bears____by_katnay-d978qh9.png"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "4C4M/U0Dh/enUIYeJk/36rzWRcfg+yDaxKKObQjA3TYvwacjzXQQIfvpERQ/Wx276v5K67WCC3mq5X2KVZmncPAtXpfV3qe4boi7oPxxq3gQPnUJgmuz56XmkhiGZWF8zCur1/oREnxaKf5N3hVxYFrheXM9MvLESulavEelOsZhExzJl6a8FXi9x5QdrOuPIitk+TuXQ4g6O9nhG8aQurl0Cm0ykve/WFUl4JuFqcMFzv8awDdbJmUfmDCjvn5YHA3PNnObgr6xeUnqZuBRB6ookxI4/Oh+Iu+tjT0VtP0X9D5GdtDpAjpu1WmVwkB61cnSDAiiUPGsFyAifO5fHQ8bF3m1gacbCbsYcl+i1IQ",
                                "to": to,
                                "messages": [
                                    {
                                            "type": "template",
                                            "altText": "Imagez",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": [
                                                    {
                                                        "imageUrl": image,
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": image
                                                        }
                                                    }
                                                ]
                                            }
                                        }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)

                        elif cmd == "meh":
                            _session = requests.session()
                            url = " https://game.linefriends.com/cdn/jbp-lcs/"
                            headers = {
                             "Content-Type": "application/json",
                             "User-Agent": "Mozilla/5.0 (Linux;Android 5.1.1; SM-J320G Build/LMY47V; wv)AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 Line/8.2.0"
                            }
                            data = {
                             "cc": "4C4M/U0Dh/enUIYeJk/36rzWRcfg+yDaxKKObQjA3TYvwacjzXQQIfvpERQ/Wx276v5K67WCC3mq5X2KVZmncPAtXpfV3qe4boi7oPxxq3gQPnUJgmuz56XmkhiGZWF8zCur1/oREnxaKf5N3hVxYFrheXM9MvLESulavEelOsZhExzJl6a8FXi9x5QdrOuPIitk+TuXQ4g6O9nhG8aQurl0Cm0ykve/WFUl4JuFqcMFzv8awDdbJmUfmDCjvn5YHA3PNnObgr6xeUnqZuBRB6ookxI4/Oh+Iu+tjT0VtP0X9D5GdtDpAjpu1WmVwkB61cnSDAiiUPGsFyAifO5fHQ8bF3m1gacbCbsYcl+i1IQ",
                             "to": to,
                             "messages": [
                              {
                               "type": "template",
                               "altText": "Heiii",
                               "template": {
                                 "type": "buttons",
                                 "thumbnailImageUrl": "https://s.kaskus.id/images/2017/11/11/6274608_20171111081955.gif",
                                 #"title": "             My instagram",
                                 "text": " ",
                                 "actions": [
                                   {
                                     "type": "uri",
                                     "label": "My Insta",
                                     "uri": "https://instagram.com/muh.khadaffy",
                                   },
                                   {
                                     "type": "uri",
                                     "label": "My Github",
                                     "uri": "https://github.com/heefpuy",
                                   },
                                   {
                                     "type": "uri",
                                     "label": "Camera",
                                     "uri": "line://nv/camera",
                                   },
                                   {
                                     "type": "uri",
                                     "label": "Profile",
                                     "uri": "line://nv/profile"
                                   }
                                 ]
                               }
                             }
                           ]
                         }

                            anu = _session.get(url, headers=headers)
                            data = json.dumps(data)
                            send = _session.post("https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage", data=data, headers=headers)
                            print(send.json())
                          #if msg.contentType == 7:
                           #stkid = msg.contentMetadata["STKID"]
                           #print(stkid)

                        elif cmd == "mehh":
                            _session = requests.session()
                            url = " https://game.linefriends.com/cdn/jbp-lcs/"
                            headers = {
                             "Content-Type": "application/json",
                             "User-Agent": "Mozilla/5.0 (Linux;Android 5.1.1; SM-J320G Build/LMY47V; wv)AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 Line/8.2.0"
                            }
                            data = {
                             "cc": "4C4M/U0Dh/enUIYeJk/36rzWRcfg+yDaxKKObQjA3TYvwacjzXQQIfvpERQ/Wx276v5K67WCC3mq5X2KVZmncPAtXpfV3qe4boi7oPxxq3gQPnUJgmuz56XmkhiGZWF8zCur1/oREnxaKf5N3hVxYFrheXM9MvLESulavEelOsZhExzJl6a8FXi9x5QdrOuPIitk+TuXQ4g6O9nhG8aQurl0Cm0ykve/WFUl4JuFqcMFzv8awDdbJmUfmDCjvn5YHA3PNnObgr6xeUnqZuBRB6ookxI4/Oh+Iu+tjT0VtP0X9D5GdtDpAjpu1WmVwkB61cnSDAiiUPGsFyAifO5fHQ8bF3m1gacbCbsYcl+i1IQ",
                             "to": to,
                             "messages": [
                              {
                               "type": "template",
                               "altText": "Heii",
                               "template": {
                                 "type": "buttons",
                                 "thumbnailImageUrl": "https://media1.tenor.com/images/4a54404d97232c2cfd7b30bb5575e29c/tenor.gif",
                                 #"title": "             Instagram",
                                 "text": " ",
                                 "actions": [
                                   {
                                     "type": "uri",
                                     "label": "Grrrrrrrah",
                                     "uri": "https://media1.tenor.com/images/4a54404d97232c2cfd7b30bb5575e29c/tenor.gif"
                                   }
                                 ]
                               }
                             }
                           ]
                         }

                            anu = _session.get(url, headers=headers)
                            data = json.dumps(data)
                            send = _session.post("https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage", data=data, headers=headers)
                            print(send.json())

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = aditmadzs.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = aditmadzs.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "! "+ str(no) + ". " + mem.displayName
                                aditmadzs.sendMessage(to," Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]" + ret_ + "\n\n「 %i Members 」" % len(G.members))
                            except:
                                pass

                        elif cmd == "fiendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = aditmadzs.getAllContactIds()
                               for i in gid:
                                   G = aditmadzs.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += " " + str(a) + ". " +G.displayName+ "\n"
                               aditmadzs.sendMessage(msg.to,"[ FRIEND LIST ]\n\n"+ma+"\n[ Ada "+str(len(gid))+" Friends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = aditmadzs.getGroupIdsJoined()
                               for i in gid:
                                   G = aditmadzs.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += " " + str(a) + ". " +G.name+ "\n"
                               aditmadzs.sendMessage(msg.to,"[ GROUP LIST ]\n\n"+ma+"\n[ Ada "+str(len(gid))+" Grup ]")

                        elif cmd == "gruplist2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += " " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"「 GROUP LIST 」\n\n"+ma+"\n[ Ada "+str(len(gid))+" Grup ]")


                        elif cmd == "buka":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = ki.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   ki.updateGroup(X)
                                   ki.sendMessage(msg.to, " 「 Url 」\nUrl Terbuka")

                        elif cmd == "tutup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = ki.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   ki.updateGroup(X)
                                   ki.sendMessage(msg.to, " 「 Url 」\nUrl Tertutup")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = ki.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      ki.updateGroup(x)
                                   gurl = ki.reissueGroupTicket(msg.to)
                                   ki.sendMessage(msg.to, ""+str(x.name)+ "\n 「 http://line.me/R/ti/g/"+gurl+" 」")

                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                              ginvited = aditmadzs.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      aditmadzs.rejectGroupInvitation(gid)
                                  aditmadzs.sendMessage(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                              else:
                                  aditmadzs.sendMessage(to, "Tidak ada undangan yang tertunda")

#===========BOT UPDATE============#
                        elif cmd == "change 2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                aditmadzs.sendMessage(msg.to,"Fotonya?")

                        elif cmd.startswith("changer"):
                          if wait["selfbot"] == True:
                            aditmadzs.sendMessage(msg.to,"  「 Changer Menu 」\n\n[0] Staff Only\n[1] All Can Used\n\n1. BotPicture[0]\n2. GroupPicture[1]\n3. BotName[0]\n\n 'Sample : Change 2 (send 1 image)'")

                        elif cmd == "ndchange 1":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                ki.sendMessage(msg.to,"Fotonya?")

                        elif cmd == "dpchange":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                aditmadzs.sendMessage(msg.to,"Fotonya?")

                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][mid][Amid][Bmid][Cmid][Dmid] = True
                                aditmadzs.sendMessage(msg.to,"Fotonya?")

                        elif cmd.startswith("cn "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = aditmadzs.getProfile()
                                profile.displayName = string
                                aditmadzs.updateProfile(profile)
                                ki.updateProfile(profile)
                                kk.updateProfile(profile)
                                kc.updateProfile(profile)
                                km.updateProfile(profile)
                                ks.updateProfile(profile)
                                aditmadzs.sendMessage(msg.to,"Dn diterapkan menjadi " + string + "")
#===========BOT UPDATE============#
                        elif cmd == "tagall" or text.lower() == 'mentioning' or text.lower() == 'tag all':
                          if wait["selfbot"] == True:
                               group = aditmadzs.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (80, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm4)

                        elif cmd == "botlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n  '
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + " "
                                aditmadzs.sendMessage(msg.to," 「 Rinda BOT List 」\n"+ma+" ")

                        elif cmd == "devlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                #a = 0
                                b = 0
                                c = 0
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n  '
                                    mb += "「" + str(b) + "」 " +aditmadzs.getContact(m_id).displayName + " "
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n  「'
                                    mc += "「" + str(c) + "」 " +aditmadzs.getContact(m_id).displayName + " "
                                aditmadzs.sendMessage(msg.to," 「 Rinda Dev List 」\n\n Admin :\n"+mb+"\n\n Staff :\n"+mc+" ")

                        elif cmd == "securestatus":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n  '
                                    ma += "「" + str(a) + "」 " +aditmadzs.getGroup(group).name + " "
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n  '
                                    mb += "「" + str(b) + "」 " +aditmadzs.getGroup(group).name + " "
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n  '
                                    md += "「" + str(d) + "」 " +aditmadzs.getGroup(group).name + " "
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n  '
                                    mc += "「" + str(c) + "」 " +aditmadzs.getGroup(group).name + " "
                                gid = protectinvite
                                for group in gid:
                                    e = e + 1
                                    end = '\n  '
                                    me += "「" + str(e) + "」 " +aditmadzs.getGroup(group).name + " "
                                aditmadzs.sendMessage(msg.to," 「 Secures Activity 」\n\n$ Secure [1] Active in:\n"+me+"\n\n$ Secure [2] Active in:\n"+mb+"\n\n$ Secure [3] Active in:\n"+mc+"\n\n$ Secure [4] Active in:\n"+md+"\n\n$ Secure [5] Active in:\n"+ma+" ")

                        elif cmd.startswith("securelist"):
                          if msg._from in admin:
                            aditmadzs.sendMessage(msg.to, " 「 Secures List 」\n\n Secure 1 : Inviting\n Secure 2 : Kicking\n Secure 3 : Cancelling\n Secure 4 : MemJoined\n Secure 5 : Qr Update")
# Secure 1 : Anti Inviting, Secure 2 : Anti Kicking, Secure 3 : Anti Cancelling, Secure 4 : Anti Joined, Secure 5 : Anti Qr Update

                        elif cmd == "respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                aditmadzs.sendMessage(msg.to,"こんにちは。1")
                                ki.sendMessage(msg.to,"こんにPUYちは。")
                                kk.sendMessage(msg.to,"こんにPUYちは。")
                                kc.sendMessage(msg.to,"こんにPUYちは。")
                                km.sendMessage(msg.to,"こんにPUYちは。")
                                ks.sendMessage(msg.to,"こんにPUYちは。")

                        elif cmd == "???":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid]
                                    aditmadzs.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                except:
                                    pass

                        elif cmd == "-_-":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                km.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                                #G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                aditmadzs.updateGroup(G)
                                ks.sendMessage(to, "すべてのこんにちは、私はPUY")

                        elif cmd == "@bye":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ks.sendMessage(msg.to, "もう一度会いましょう\n"+str(G.name))
                                #aditmadzs.leaveGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                km.leaveGroup(msg.to)
                                ks.leaveGroup(msg.to)

                        elif cmd == "@byeall":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                aditmadzs.sendMessage(msg.to, "もう一度会いましょう\n"+str(G.name))
                                aditmadzs.leaveGroup(msg.to)

                        elif cmd == "2bye":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                G = ki.getGroup(msg.to)
                                ki.sendMessage(msg.to, "Dadah "+str(G.name))
                                #aditmadzs.leaveGroup(msg.to)
                                ki.leaveGroup(msg.to)

                        elif cmd == "3bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = kk.getGroup(msg.to)
                                kk.sendMessage(msg.to, "Dadah "+str(G.name))
                                kk.leaveGroup(msg.to)

                        elif cmd == "4bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = kc.getGroup(msg.to)
                                kc.sendMessage(msg.to, "Dadah "+str(G.name))
                                kc.leaveGroup(msg.to)

                        elif cmd == "5bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = km.getGroup(msg.to)
                                km.sendMessage(msg.to, "Dadah "+str(G.name))
                                km.leaveGroup(msg.to)

                        elif cmd == "6bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = ks.getGroup(msg.to)
                                ks.sendMessage(msg.to, "Dadah "+str(G.name))
                                ks.leaveGroup(msg.to)

                        elif cmd.startswith("4leave to "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = kc.getGroupIdsJoined()
                                for i in gid:
                                    h = kc.getGroup(i).name
                                    if h == ng:
                                        kc.sendMessage(i, "Undang Kembali jika Butuh")
                                        kc.leaveGroup(i)
                                        kc.sendMessage(to,"berhasil Keluar dari Grup\n" +h)

                        elif cmd.startswith("5leave to "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = km.getGroupIdsJoined()
                                for i in gid:
                                    h = km.getGroup(i).name
                                    if h == ng:
                                        km.sendMessage(i, "Undang Kembali jika Butuh")
                                        km.leaveGroup(i)
                                        km.sendMessage(to,"berhasil Keluar dari Grup\n" +h)

                        elif cmd.startswith("6leave to "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = ks.getGroupIdsJoined()
                                for i in gid:
                                    h = ks.getGroup(i).name
                                    if h == ng:
                                        ks.sendMessage(i, "Undang Kembali jika Butuh")
                                        ks.leaveGroup(i)
                                        ks.sendMessage(to,"berhasil Keluar dari Grup\n" +h)

                        elif cmd.startswith("3leave to "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = kk.getGroupIdsJoined()
                                for i in gid:
                                    h = kk.getGroup(i).name
                                    if h == ng:
                                        kk.sendMessage(i, "Undang Kembali jika Butuh")
                                        kk.leaveGroup(i)
                                        kk.sendMessage(to,"berhasil Keluar dari Grup\n" +h)

                        elif cmd.startswith("2leave to "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = ki.getGroupIdsJoined()
                                for i in gid:
                                    h = ki.getGroup(i).name
                                    if h == ng:
                                        ki.sendMessage(i, "Undang Kembali jika Butuh")
                                        ki.leaveGroup(i)
                                        ki.sendMessage(to,"berhasil Keluar dari Grup\n" +h)

                        elif cmd.startswith("1leave to "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = aditmadzs.getGroupIdsJoined()
                                for i in gid:
                                    h = aditmadzs.getGroup(i).name
                                    if h == ng:
                                        aditmadzs.sendMessage(i, "dipaksa out oleh Owner,\nUndang Kembali jika Butuh:((((((")
                                        aditmadzs.leaveGroup(i)
                                        aditmadzs.sendMessage(to,"berhasil Keluar dari Grup\n" +h)
                                        ki.sendMessage(to,"berhasil Keluar dari Grup\n" +h)

                        elif cmd.startswith("allleave to "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = aditmadzs.getGroupIdsJoined()
                                for i in gid:
                                    h = aditmadzs.getGroup(i).name
                                    if h == ng:
                                        aditmadzs.sendMessage(i, "Undang Kembali jika Butuh")
                                        aditmadzs.leaveGroup(i)
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        km.leaveGroup(i)
                                        ks.leaveGroup(i)
                                        aditmadzs.sendMessage(to, "Berhasil Keluar dari Grup\n" +h)

                        elif cmd == "2j":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)
                                ki.sendMessage(to, "Hai")

                        elif cmd == "3j":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)
                                kk.sendMessage(to, "Hai")

                        elif cmd == "4j":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)
                                kc.sendMessage(to, "Hai")

                        elif cmd == "5j":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                km.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = km.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                km.updateGroup(G)
                                km.sendMessage(to, "Hai")

                        elif cmd == "6j":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ks.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ks.updateGroup(G)
                                ks.sendMessage(to, "Hai")

                        elif cmd.startswith("unsendsas"):
                            cond=text.split(" ")
                            if len(cond)==2:
                                def unsendMessage(num):
                                    msgid=[]
                                    for message in aditmadzs.talk.getRecentMessagesV2(to,101):
                                        if len(msgid)==int(num):
                                            break
                                        else:
                                            if message._from==aditmadzs.getProfile().mid:
                                                if 'UNSENT' not in message.contentMetadata:
                                                    msgid.append(message.id)
                                                    continue
                                    def unsMes(id):
                                        aditmadzs.unsendMessage(id)
                                    no=0
                                    for a in msgid:
                                        no=no+1
                                        thread1 = threading.Thread(target=unsMes, args=(a,))
                                        thread1.start()
                                        thread1.join()
                                    return no
                                aditmadzs.sendMessage(to,'Sucess Unsend {} message'.format(str(unsendMessage(int(cond[1])))))

                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = aditmadzs.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = aditmadzs.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = aditmadzs.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                aditmadzs.sendMessage(msg.to, "Responding Speed\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               start = time.time()
                               aditmadzs.sendMessage(msg.to, "「 Sending Speed 」\n  Creating...")
                               #time.sleep(2.0)
                               elapsed_time = time.time() - start
                               aditmadzs.sendMessage(msg.to, "「 Speed 」\n {}".format(str(elapsed_time)))

                        elif cmd == "ceksider on":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['ADITMADZSreadPoint'][msg.to] = msg_id
                                 Setmain['ADITMADZSreadMember'][msg.to] = {}
                                 #aditmadzs.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                 aditmadzs.sendMessage(msg.to, "Ceksider Aktif.")

                        elif cmd == "ceksider off":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['ADITMADZSreadPoint'][msg.to]
                                 del Setmain['ADITMADZSreadMember'][msg.to]
                                 #aditmadzs.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                 aditmadzs.sendMessage(msg.to, "Ceksider Tidak Aktif.")

                        elif cmd == "ceksider":
                          #if msg._from in admin:
                            if msg.to in Setmain['ADITMADZSreadPoint']:
                                if Setmain['ADITMADZSreadMember'][msg.to] != {}:
                                    nad = []
                                    for x in Setmain['ADITMADZSreadMember'][msg.to]:
                                        nad.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  「 Ceksider 」\n\n1. "
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in nad:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(nad):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(aditmadzs.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\n  「 {} 」 Readers Found".format(str(len(nad)))
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        aditmadzs.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['ADITMADZSreadPoint'][msg.to]
                                        del Setmain['ADITMADZSreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['ADITMADZSreadPoint'][msg.to] = msg.id
                                    Setmain['ADITMADZSreadMember'][msg.to] = {}
                                else:
                                    aditmadzs.sendMessage(msg.to, "Tidak satupun.")
                            else:
                                aditmadzs.sendMessage(msg.to, "Aktifin dulu lah")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  aditmadzs.sendMessage(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  aditmadzs.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  aditmadzs.sendMessage(msg.to, "Sudak tidak aktif")

#===========Hiburan============#

                        elif cmd.startswith("musik: "):
                          if msg._from in admin:
                            try:
                                search = msg.text.replace("musik: ","")
                                r = requests.get("https://farzain.xyz/api/premium/joox.php?apikey=al11241519&id={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = "「 Hasil Musik 」\n"
                                hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                hasil += "\nJudul : {}".format(str(info["judul"]))
                                hasil += "\nAlbum : {}".format(str(info["album"]))
                                hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                                hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                                hasil += "\n\nLink : \n3. M4A : {}".format(str(audio["m4a"]))
                                aditmadzs.sendImageWithURL(msg.to, str(data["gambar"]))
                                aditmadzs.sendMessage(msg.to, str(hasil))
                                aditmadzs.sendMessage(msg.to, "Downloading...")
                                aditmadzs.sendMessage(msg.to, "「 Result MP3 」")
                                aditmadzs.sendAudioWithURL(msg.to, str(audio["mp3"]))
                                aditmadzs.sendMessage(msg.to, "「 Result M4A 」")
                                aditmadzs.sendVideoWithURL(msg.to, str(audio["m4a"]))
                                aditmadzs.sendMessage(msg.to, str(data["lirik"]))
                                aditmadzs.sendMessage(msg.to, "Success Download...")
                            except Exception as error:
                            	aditmadzs.sendMessage(msg.to, "「 Result Error 」\n" + str(error))

                        elif cmd.startswith("randomnumber: "):
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                angka = msg.text.replace(separate[0] + " ","")
                                tgb = angka.split("-")
                                num1 = tgb[0]
                                num2 = tgb[1]
                                r = requests.get("https://farzain.xyz/api/random.php?min="+num1+"&max="+num2)
                                data = r.json()
                                aditmadzs.sendMessage(msg.to,"Hasil : "+str(data["url"]))


                        elif cmd.startswith("1cak"):
                          if msg._from in admin:
                              r=requests.get("https://api-1cak.herokuapp.com/random")
                              data=r.text
                              data=json.loads(data)
                              print(data)
                              hasil = "Result :\n"
                              hasil += "\nID : " +str(data["id"])
                              hasil += "\nTitle : " + str(data["title"])
                              hasil += "\nUrl : " + str(data["url"])
                              hasil += "\nVotes : " + str(data["votes"])
                              aditmadzs.sendMessage(msg.to, str(hasil))

                        elif cmd.startswith("musik2: "):
                          if msg._from in admin:
                            try:
                                dan = msg.text.replace("musik2: ","")
                                r = requests.get("http://corrykalam.pw/api/joox.php?song={}"+urllib.parse.quote(dan))
                                data = r.json()
                                l = data["lyric"].replace("ti:","Judul: ")
                                i = l.replace("ar:","Penyanyi: ")
                                r = i.replace("al:","Album: ")
                                ii = r.replace("[by:]","")
                                k = ii.replace("[offset:0]","")
                                lirik = k.replace("***Lirik didapat dari pihak ketiga***\n","")
                                aditmadzs.sendImageWithURL(msg.to, data["image"])
                                t = "[ Music ]"
                                t += "\n\nJudul: "+str(data["title"])
                                t+="\nPenyanyi: "+str(data["singer"])
                                t+="\n\n[ Finish ]\n\n"+str(lirik)
                                aditmadzs.sendMessage(msg.to, str(t))
                                aditmadzs.sendAudioWithURL(msg.to, data["url"])
                            except Exception as error:
                                pass

                        elif cmd.startswith("playlist "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(":")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "━━━━[ List Lagu ]━━━━"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n  ━━[ Total {} Lagu ]━━".format(str(len(data["result"])))
                                    ret_ += "\n\nUntuk Melihat Details Musik, Silahkan Ketik \n❧「 {}Playlist {}:nomor 」 ".format(str(),str(search))
                                    ret_ += "\n❧「 {}Lirik {}:nomor 」 ".format(str(),str(search))
                                    aditmadzs.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "┏━━━━[ Detail Musik ]━━━━"
                                            ret_ += "\n┃┃ Title : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n┃┃ Album : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n┃┃ Size : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n┗━━[ Tunggu Audionya ]━━━"
                                            aditmadzs.sendMessage(msg.to, str(ret_))
                                            aditmadzs.sendAudioWithURL(msg.to, str(data["result"]["mp3"][0]))
                            except Exception as error:
                                pass

                        elif cmd.startswith("lirik "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(":")
                                search = cond[0]
                                api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "━━━━[ List Lirik ]━━━━"
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n {}. {}".format(str(num), str(lyric["single"]))
                                    ret_ += "\n  ━━[ Total {} Lagu ]━━".format(str(len(data["results"])))
                                    ret_ += "\n\nUntuk Melihat Details Musik, Silahkan Ketik \n❧「 {}Lirik {}:nomor 」".format(str(),str(search))
                                    ret_ += "\n❧「 {}Playlist {}:nomor 」 ".format(str(),str(search))
                                    aditmadzs.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["results"]):
                                        lyric = data["results"][num - 1]
                                        api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                        data = api.text
                                        data = json.loads(data)
                                        lyrics = data["results"]["lyric"]
                                        lyric = lyrics.replace('ti:','Title - ')
                                        lyric = lyric.replace('ar:','Artist - ')
                                        lyric = lyric.replace('al:','Album - ')
                                        removeString = "[1234567890.:]"
                                        for char in removeString:
                                            lyric = lyric.replace(char,'')
                                        aditmadzs.sendMessage(msg.to, str(lyric))
                            except Exception as error:
                                pass

                        elif cmd.startswith("img food: "):
                          if msg._from in admin:
                                query = msg.text.replace("img food: ","")
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + query + "?offset=1")
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    for food in data:
                                        aditmadzs.sendImageWithURL(msg.to, str(food["url"]))

                        elif cmd.startswith("getsmule "):
                          #if msg._from in admin:
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                #aditmadzs.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(0.2)
                                aditmadzs.sendMessage(msg.to, "ID Smule : "+smule+"\n"+links)
                                aditmadzs.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass

                        elif cmd.startswith("meme"):
                          if msg._from in admin:
                            txt = msg.text.split("*")
                            image = ("http://memegen.link/"+txt[1].replace(" ","_")+"/"+txt[2].replace(" ","_")+"/"+txt[3].replace(" ","_")+".jpg?watermark=none")
                            aditmadzs.sendImageWithURL(msg.to, image)


                        elif cmd.startswith("ytmp4 "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n Author : ' + str(vid.author)
                                    durasi = '\n Duration : ' + str(vid.duration)
                                    suka = '\n Likes : ' + str(vid.likes)
                                    rating = '\n Rating : ' + str(vid.rating)
                                    deskripsi = '\n Deskripsi : ' + str(vid.description)
                                aditmadzs.sendVideoWithURL(msg.to, me)
                                aditmadzs.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                aditmadzs.sendMessage(msg.to,str(e))

                        elif cmd.startswith("ytmp3 "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n Author : ' + str(vid.author)
                                    durasi = '\n Duration : ' + str(vid.duration)
                                    suka = '\n Likes : ' + str(vid.likes)
                                    rating = '\n Rating : ' + str(vid.rating)
                                    deskripsi = '\n Deskripsi : ' + str(vid.description)
                                aditmadzs.sendImageWithURL(msg.to, me)
                                aditmadzs.sendAudioWithURL(msg.to, shi)
                                aditmadzs.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                aditmadzs.sendMessage(msg.to,str(e))

                        elif cmd.startswith("instainfo "):
                          #if msg._from in admin:
                            query = cmd.replace("instainfo ","")
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                html = requests.get('https://www.instagram.com/' + instagram + '/?')
                                soup = BeautifulSoup(html.text, 'html.parser')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                AR = text1[0].replace("s150x150/","")
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Visit here " + "https://www.instagram.com/" + instagram
                                detail = "  「 IG Profile " + query + " 」\n"
                                #details = "\n========INSTAGRAM INFO ========"
                                aditmadzs.sendMessage(msg.to, detail + user + user1 + followers + following + post + link)
                                #aditmadzs.sendImageWithURL(msg.to, AR)
                            except Exception as njer:
                                aditmadzs.sendMessage(msg.to, str(njer))

                        elif cmd.startswith("cekdate: "):
                          #if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91ARs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            aditmadzs.sendMessage(msg.to," I N F O R M A S I \n\n"+" Date Of Birth : "+lahir+"\n Age : "+usia+"\n Ultah : "+ultah+"\n Zodiak : "+zodiak)

                        elif cmd.startswith("spamtag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["ADITMADZSlimit"] = num
                                aditmadzs.sendMessage(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                aditmadzs.sendMessage(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["ADITMADZSlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                aditmadzs.sendMessage1(msg)
                                            except Exception as e:
                                                aditmadzs.sendMessage(msg.to,str(e))
                                    else:
                                        aditmadzs.sendMessage(msg.to,"Jumlah melebihi 1000")

## DIR ##
                        elif text.lower() == 'rin screen':
                          if msg._from in admin:
                            process = os.popen('screen -list')
                            a = process.read()
                            aditmadzs.sendMessage(to, "{}".format(a))
                            process.close()
                        elif text.lower() == 'rin look akad':
                          if msg._from in admin:
                            process = os.popen('cd akad && ls')
                            a = process.read()
                            aditmadzs.sendMessage(msg.to," 「 RINDA AKAD FOLDER 」\n\n" +str(a)+" ")
                            #process.close()
                        elif text.lower() == 'rin look linepy':
                          if msg._from in admin:
                            process = os.popen('cd LINEPY && ls')
                            a = process.read()
                            aditmadzs.sendMessage(msg.to," 「 RINDA LINEPY FOLDER 」\n\n" +str(a)+" ")
                            process.close()
                        elif text.lower() == 'rin look thrift':
                          if msg._from in admin:
                            process = os.popen('cd thrift && ls')
                            a = process.read()
                            aditmadzs.sendMessage(msg.to," 「 RINDA THRIFT FOLDER 」\n\n" +str(a)+" ")
                            process.close()
                        elif text.lower() == 'rin ls':
                          if msg._from in admin:
                            process = os.popen('ls')
                            a = process.read()
                            aditmadzs.sendMessage(to, " 「 RINDA LS 」\n\n{}".format(a)+" ")
                            process.close()

                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = aditmadzs.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                aditmadzs.sendMessage(msg.to, "Mengundang {} Undangan Fcg".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        aditmadzs.sendMessage(msg.to,str(e))
                                else:
                                    aditmadzs.sendMessage(msg.to,"Kebanyakan :((((")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      aditmadzs.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '5'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      aditmadzs.sendMessage(midd, str(Setmain["ADITMADZSmessage1"]))
                                      ki.sendMessage(midd, str(Setmain["ADITMADZSmessage1"]))

                        elif 'Rin look token' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              aditmadzs.sendMessage(msg.to,"「 Token Rinda 」\n"+aditmadzs.authToken)
                              #aditmadzs.sendMessage(msg.to,"KI\n"+ki.authToken)

                        elif 'Indri look token' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              ki.sendMessage(msg.to,"「 Token Indri 」\n"+ki.authToken)

#==============================================================================#
#===========Settings============#
                        elif 'Simiz ' in msg.text:
                              spl = msg.text.replace('Simiz ','')
                              if spl == 'on':
                                  if msg.to in simisimi:
                                       msgs = "Simi-simi sudah aktif"
                                  else:
                                       simisimi.append(msg.to)
                                       ginfo = ki.getGroup(msg.to)
                                       msgs = "Simi-simi Diaktifkan\nDi Group : " +str(ginfo.name)
                                  ki.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in simisimi:
                                         simisimi.remove(msg.to)
                                         ginfo = ki.getGroup(msg.to)
                                         msgs = "Simi-simi Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Simi-simi Sudah Tidak Aktif"
                                    ki.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Transto eng*' in msg.text:
                              spl = msg.text.replace('Transto eng*','')
                              if spl == 'on':
                                  if msg.to in translateen:
                                       msgs = "Terjemah langsung Status Aktif"
                                  else:
                                       translateen.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Terjemah Langsung Diaktifkan"
                                  aditmadzs.sendMessage(msg.to, "  「 Translate to English 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateen:
                                         translateen.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Terjemah Langsung Dinonaktifkan"
                                    else:
                                         msgs = "Terjemah langsung Sudah Tidak Aktif"
                                    aditmadzs.sendMessage(msg.to, "  「 Translate to English 」\n" + msgs)

                        elif 'Transto indo*' in msg.text:
                              spl = msg.text.replace('Transto indo*','')
                              if spl == 'on':
                                  if msg.to in translateid:
                                       msgs = "Terjemah langsung Status Aktif"
                                  else:
                                       translateid.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Terjemah Langsung Diaktifkan"
                                  aditmadzs.sendMessage(msg.to, "  「 Translate to Indonesia 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateid:
                                         translateid.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Terjemah Langsung Dinonaktifkan"
                                    else:
                                         msgs = "Terjemah langsung Sudah Tidak Aktif"
                                    aditmadzs.sendMessage(msg.to, "  「 Translate to Indonesia 」\n" + msgs)

                        elif 'Transto arab*' in msg.text:
                              spl = msg.text.replace('Transto arab*','')
                              if spl == 'on':
                                  if msg.to in translatear:
                                       msgs = "Terjemah langsung Status Aktif"
                                  else:
                                       translatear.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Terjemah langsung Diaktifkan" #\n< " +str(ginfo.name + " >")
                                  aditmadzs.sendMessage(msg.to, "  「 Translate to Arab 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translatear:
                                         translatear.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Terjemah Langsung Dinonaktifkan" #\n< " +str(ginfo.name + " >")
                                    else:
                                         msgs = "Terjemah langsung Sudah Tidak Aktif"
                                    aditmadzs.sendMessage(msg.to, "  「 Translate to Arab 」\n" + msgs)

                        elif 'Welcomemsg ' in msg.text:
                           if msg._from in owner:
                              spl = msg.text.replace('Welcomemsg ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Diaktifkan" #\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "  「 Welcome Messages 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Dinonaktifkan" #\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "  「 Welcome Messages 」\n" + msgs)

#===========Protection============#

                        elif 'S5 ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('S5 ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protection Ticket Group Status is Actived"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Diaktifkan"
                                  aditmadzs.sendMessage(msg.to, "  「 QrSecure 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                       protectqr.remove(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Dinonaktifkan"
                                    else:
                                         msgs = "Protection Ticket Group Status is UnActived"
                                    aditmadzs.sendMessage(msg.to, "  「 QrSecure 」\n" + msgs)

                        elif 'S2 ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('S2 ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protection Anti Kick Status is Actived"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Diaktifkan"
                                  aditmadzs.sendMessage(msg.to, "  「 KickingSecure 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                       protectkick.remove(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Dinonaktifkan"
                                    else:
                                         msgs = "Protection Anti Kick Status is UnActived"
                                    aditmadzs.sendMessage(msg.to, "  「 KickingSecure 」\n" + msgs)

                        elif 'S4 ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('S4 ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protection Member Joined Status is Actived"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Diaktifkan"
                                  aditmadzs.sendMessage(msg.to, "  「 JoiningSecure 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                       protectjoin.remove(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Dinonaktifkan"
                                    else:
                                         msgs = "Protection Member Joined Status is UnActived"
                                    aditmadzs.sendMessage(msg.to, "  「 JoiningSecure 」\n" + msgs)

                        elif 'S3 ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('S3 ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protection Anti Cancel Status is Actived"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Diaktifkan"
                                  aditmadzs.sendMessage(msg.to, "  「 CancellingSecure 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                       protectcancel.remove(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Dinonaktifkan"
                                    else:
                                         msgs = "Protection Anti Cancel Status is UnActived"
                                    aditmadzs.sendMessage(msg.to, "  「 CancellingSecure 」\n" + msgs)

                        elif 'S1 ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('S1 ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protection Anti Invite Status is Actived"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Diaktifkan"
                                  aditmadzs.sendMessage(msg.to, "  「 InvitingSecure 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                       protectinvite.remove(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Dinonaktifkan"
                                    else:
                                         msgs = "Protection Anti Invite Status is UnActived"
                                    aditmadzs.sendMessage(msg.to, "  「 InvitingSecure 」\n" + msgs)

                        elif 'Allsecure ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allsecure ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = aditmadzs.getGroup(msg.to)
                                      msgs = "All Secure Telah Aktif"
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = aditmadzs.getGroup(msg.to)
                                      msgs = "Berhasil Mengaktifkan"
                                  aditmadzs.sendMessage(msg.to, "  「 All Secure 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "All Secure tidak Aktif"
                                    else:
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Berhasil Menonaktifkan"
                                    aditmadzs.sendMessage(msg.to, "  「 All Secure 」\n" + msgs)

#===========KICKOUT============#

                        elif ("Kicking " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin[target] = True
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           aditmadzs.sendMessage(msg.to,"+1 Admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           aditmadzs.sendMessage(msg.to,"+1 Staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           aditmadzs.sendMessage(msg.to,"+1 Bot")
                                       except:
                                           pass

                        elif ("Adminrem " in msg.text):
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del admin[target]
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           aditmadzs.sendMessage(msg.to,"-1 Admin")
                                       except:
                                           pass

                        elif ("Staffrem " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Aditmadzs:
                                       try:
                                           staff.remove(target)
                                           aditmadzs.sendMessage(msg.to,"-1 Staff")
                                       except:
                                           pass

                        elif ("Botrem " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Aditmadzs:
                                       try:
                                           Bots.remove(target)
                                           aditmadzs.sendMessage(msg.to,"-1 Bot")
                                       except:
                                           pass

                        elif cmd == "admin:add" or text.lower() == 'admin:add':
                            if msg._from in owner:
                                wait["addadmin"] = True
                                aditmadzs.sendMessage(msg.to,"Kontaknya?")

                        elif cmd == "admin:rem" or text.lower() == 'admin:rem':
                            if msg._from in owner:
                                wait["delladmin"] = True
                                aditmadzs.sendMessage(msg.to,"Kontaknya?")

                        elif cmd == "staff:add" or text.lower() == 'staff:add':
                            if msg._from in owner:
                                wait["addstaff"] = True
                                aditmadzs.sendMessage(msg.to,"Kontaknya?")

                        elif cmd == "staff:rem" or text.lower() == 'staff:rem':
                            if msg._from in owner:
                                wait["dellstaff"] = True
                                aditmadzs.sendMessage(msg.to,"Kontaknya?")

                        elif cmd == "bot:add" or text.lower() == 'bot:add':
                            if msg._from in owner:
                                wait["addbots"] = True
                                aditmadzs.sendMessage(msg.to,"Kontaknya?")

                        elif cmd == "bot:rem" or text.lower() == 'bot:rem':
                            if msg._from in owner:
                                wait["dellbots"] = True
                                aditmadzs.sendMessage(msg.to,"Kontaknya?")

                        elif cmd == "rinda upgrade" or text.lower() == '@refresh':
                            if msg._from in owner:
                                aditmadzs.sendMessage(msg.to, "「 お待ちください 4s 」")
                                time.sleep(4.0)
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                #sendMentions(to, "// Hei @! Upgrade Done //")
                                aditmadzs.sendMessage(msg.to, "「 Refresh ステータス : 成功 」")
                                #aditmadzs.sendMessage(msg.to,"// Hei Upgrade Done //")

                        elif cmd == "adminc" or text.lower() == 'contact admins':
                                ma = ""
                                for i in owner:
                                    ma = ki.getContact(i)
                                    ki.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "staffc" or text.lower() == 'contact staffs':
                                ma = ""
                                for i in staff:
                                    ma = ki.getContact(i)
                                    ki.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "botc" or text.lower() == 'contact bots':
                                ma = ""
                                for i in Bots:
                                    ma = ki.getContact(i)
                                    ki.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Mentionkick"] = True
                                aditmadzs.sendMessage(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Mentionkick"] = False
                                aditmadzs.sendMessage(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = True
                                aditmadzs.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = False
                                aditmadzs.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = True
                                aditmadzs.sendMessage(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = False
                                aditmadzs.sendMessage(msg.to,"Auto respon dinonaktifkan")

                        elif cmd == "respongift on" or text.lower() == 'respongift on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Mentiongift"] = True
                                aditmadzs.sendMessage(msg.to,"Auto respon gift diaktifkan")

                        elif cmd == "respongift off" or text.lower() == 'respongift off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Mentiongift"] = False
                                aditmadzs.sendMessage(msg.to,"Auto respon gift dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoJoin"] = True
                                aditmadzs.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoJoin"] = False
                                aditmadzs.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoLeave"] = True
                                aditmadzs.sendMessage(msg.to,"Auto Leave Diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoLeave"] = False
                                aditmadzs.sendMessage(msg.to,"Auto Leave Dimatikan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = True
                                aditmadzs.sendMessage(msg.to,"Auto Add Diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = False
                                aditmadzs.sendMessage(msg.to,"Auto Add Dimatikan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = True
                                aditmadzs.sendMessage(msg.to,"Detect Sticker Diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = False
                                aditmadzs.sendMessage(msg.to,"Detect Sticker Dimatikan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                settings["autoJoinTicket"] = True
                                aditmadzs.sendMessage(msg.to,"Auto Join Ticket Diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                settings["autoJoinTicket"] = False
                                aditmadzs.sendMessage(msg.to,"Auto Join Ticket Dimatikan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           aditmadzs.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           aditmadzs.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Talkwblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"Kontaknya?")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Talkdblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"Kontaknya?")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           aditmadzs.sendMessage(msg.to,"+1 Blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           aditmadzs.sendMessage(msg.to,"-1 Blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["wblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"Kontaknya?")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["dblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"Kontaknya?")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              if wait["blacklist"] == {}:
                                aditmadzs.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendMessage(msg.to," 「 Rinda Blacklist User 」\n\n"+ma+"\n 「 %s Target 」 " %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              if wait["Talkblacklist"] == {}:
                                aditmadzs.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendMessage(msg.to," 「 Talkban User 」\n\n"+ma+"\n 「 %s 」 Rinda Tban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "banlist2" or text.lower() == 'banlist2':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              if wait["blacklist"] == {}:
                                    aditmadzs.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = aditmadzs.getContact(i)
                                        aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              wait["blacklist"] = {}
                              ragets = aditmadzs.getContacts(wait["blacklist"])
                              mc = "  Saat ini ada 「 %i 」 Blacklist" % len(ragets)
                              aditmadzs.sendMessage(msg.to,"Sukses membersihkan Blist \n" +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in owner:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Pesan Message")
                              else:
                                  wait["message"] = spl
                                  aditmadzs.sendMessage(msg.to, " 「 Pesan Msg 」\nPesan Message diterapkan menjadi :\n\n「 {} 」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in owner:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Welcome Message")
                              else:
                                  wait["welcome"] = spl
                                  aditmadzs.sendMessage(msg.to, " 「 Welcome Msg 」\nWelcome Message diterapkan menjadi :\n\n「 {} 」".format(str(spl)))

                        elif 'Set leave: ' in msg.text:
                           if msg._from in owner:
                              spl = msg.text.replace('Set leave: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Leave Message")
                              else:
                                  wait["leave"] = spl
                                  aditmadzs.sendMessage(msg.to, " 「 Leave Msg 」\nLeave Message diterapkan menjadi :\n\n「 {} 」".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in owner:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Respon Message")
                              else:
                                  wait["Respontag"] = spl
                                  aditmadzs.sendMessage(msg.to, " 「Respon Msg」\nRespon Message diterapkan menjadi :\n\n「 {} 」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in owner:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["ADITMADZSmessage1"] = spl
                                  aditmadzs.sendMessage(msg.to, " 「 Spam Msg 」\nSpam Message diterapkan menjadi :\n\n「 {} 」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in owner:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Sider Message")
                              else:
                                  wait["mention"] = spl
                                  aditmadzs.sendMessage(msg.to, " 「 Sider Msg 」\nSider Message diterapkan menjadi :\n\n「 {} 」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in owner:
                               aditmadzs.sendMessage(msg.to, " 「 Pesan Msg 」\nPesan Message terkini :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in owner:
                               aditmadzs.sendMessage(msg.to, "「Welcome Msg」\nWelcome Message terkini :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "cek leave":
                            if msg._from in owner:
                               aditmadzs.sendMessage(msg.to, "「Leave Msg」\nLeave Message terkini :\n\n「 " + str(wait["leave"]) + " 」")

                        elif text.lower() == "cek respon":
                            if msg._from in owner:
                               aditmadzs.sendMessage(msg.to, "「Respon Msg」\nRespon Message terkini :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in owner:
                               aditmadzs.sendMessage(msg.to, "「Spam Msg」\nSpam Message terkini :\n\n「 " + str(Setmain["ADITMADZSmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in owner:
                               aditmadzs.sendMessage(msg.to, "「Sider Msg」\nSider Message terkini :\n\n「 " + str(wait["mention"]) + " 」")
#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = aditmadzs.findGroupByTicket(ticket_id)
                                     aditmadzs.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     aditmadzs.sendMessage(msg.to, "ke : %s" % str(group.name))
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendMessage(msg.to, "ke : %s" % str(group.name))


    except Exception as error:
        print (error)

while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
