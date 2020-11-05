from telethon import TelegramClient, sync, events, utils
from random import randint
from time import sleep
from telethon.tl.types import MessageEntityTextUrl
import requests
from bs4 import BeautifulSoup
from telethon.tl.functions.messages import StartBotRequest




energy =  {1269209704:{'full':1, 'loc': u'🏔 Этер', 'war':u'🤖Алтарь Тир'}, 1297379185:{'full':1,'loc': '🐥 11-20 Аванпост','war':'👩‍🚀Алтарь Гебо'}, 1422890561:{'full':1,'loc': '🐣1-10 Окрестности Ген. штаба','war':'🤖Алтарь Тир'}, 1454084350:{'full':1,'loc': '🐣1-10 Окрестности Ген. штаба','war':'🤖Алтарь Тир'}, 1451339857:{'full':1,'loc': u'🐣1-10 Окрестности Ген. штаба','war':'🤖Алтарь Тир'}, 1477310786:{'full':1,'loc': u'🐣1-10 Окрестности Ген. штаба','war':'🤖Алтарь Тир'},1383385498:{'full':1,'loc': '🐣1-10 Окрестности Ген. штаба','war':'🤖Алтарь Тир'}, 'run':1,'eter':0}

clients =[TelegramClient(username, api_id, api_hash), TelegramClient(username1, api_id1, api_hash1), TelegramClient(username2, api_id2, api_hash2), TelegramClient(username3, api_id3, api_hash3), TelegramClient(username4, api_id4, api_hash4), TelegramClient(username5, api_id5, api_hash5), TelegramClient(username6, api_id6, api_hash6)]
client1 = clients[0]
client2 = clients[1]
client3 = clients[2]
client4 = clients[3]
client5 = clients[4]
client0 = clients[5]
client6 = clients[6]
@client1.on(events.NewMessage(chats=('rf_telegram_bot')))
@client2.on(events.NewMessage(chats=('rf_telegram_bot')))
@client3.on(events.NewMessage(chats=('rf_telegram_bot')))
@client4.on(events.NewMessage(chats=('rf_telegram_bot')))
@client5.on(events.NewMessage(chats=('rf_telegram_bot')))
@client0.on(events.NewMessage(chats=('rf_telegram_bot')))
@client6.on(events.NewMessage(chats=('rf_telegram_bot')))
async def normal_handler(event):
    s_user_id=event.message.to_dict()['from_id']
    messag = event.message.to_dict()['message']
    to_id = event.message.to_dict()['to_id']['user_id']
    print("toooooo >>>>>>>> ",to_id)
    #print(event.message.stringify())
    mess =''
    client = event.client
    if s_user_id == 577009581:
        #print(messag.stringify())
        if energy['run']>0:
            if 'у вас встретился' in messag:
                mess= '🔪 Атаковать'
            if 'одержал победу' in messag:
                mess='🏛 В ген. штаб'
                if '0/5' in messag:
                    energy[to_id]['full']=0
            if 'дошел до локации' in messag:
                if energy[to_id]['full'] > 0: 
                    mess= '💖 Пополнить здоровье'
                else: 
                    mess="🌋 Краговые шахты"
            if 'контрольного' in messag:    
                mess="⛏Рудник"
            if ('4/5' in messag) or ('5/5' in messag):
                if energy[to_id]['full'] == 0:
                    mess= '🏛 В ген. штаб'
                    energy[to_id]['full']=1
            if ('пополнено' in messag) or ('Ты снова жив' in messag):
                if energy['eter']==0 :
                    mess=energy[to_id]['loc']
                else :
                    mess = "🏔 Этер"
            if 'время боевых действий' in messag:
                mess=energy[to_id]['war']
            if 'недостаточно энергии' in messag:    
                energy[to_id]['full']=0
                mess= '🏛 В ген. штаб'
            if 'направляет вас на официальный сайт ' in messag:    
                entities = event.message.entities
                for ent in entities:
                    if isinstance(ent,MessageEntityTextUrl):
                        if "rf-telegram.com/capcha" in ent.url:
                            proxies = { 'http': 'http://10.10.1.10:3128','https': 'http://10.10.1.10:1080'}

                            sleep(randint(2,5))
                            r = requests.get(ent.url,proxies=proxies)
                            print(r.content)
                            page = BeautifulSoup(r.text, features ="html.parser")
                            button = page.find("button",{"id":"btn"})
                            data_id = button.attrs['data-id']
                            data_test = button.attrs['data-test']
                            ref_start_link = button.attrs['data-id2']
                            sleep(randint(2,5))
                            print(ref_start_link)
                            r= requests.get('https://rf-telegram.com/capcha-approve/'+data_id +'::'+data_test, proxies=proxies)
                            print(r.content)
                            sleep(randint(2,5))
                            mess = '/start '+ref_start_link
                            
                           
   
            if mess :
                sleeptime = randint(2,15)
                print("sleeping for:", sleeptime, "seconds before ", mess) 

                sleep(sleeptime)
                
                message = await client.send_message(s_user_id,  mess)
    else:
        if '#stop' in messag:
            energy['run']=0
            print('stooooooop')
        if '#go' in messag:
            energy['run']=1
            print('g0000000000')
        if '#et' in mess :
            energy['eter']=1
            print( energy)
        if '#loc' in mess :
            energy['eter']=0
            print( energy)    

for client in clients: 
    client.start()

for client in clients: 
    client.run_until_disconnected()
