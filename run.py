from telethon import TelegramClient, sync, events
from random import randint
from time import sleep
from telethon.tl.types import MessageEntityTextUrl
import requests
from bs4 import BeautifulSoup

api_id = 1920005
api_hash = "a3b652af03811e45a1529defda863cb2"
username = "uhhhh"

api_id1 = 1980765
api_hash1 = "43e2c03697d120ff9aede51d13442e67"
username1 = "olij"

api_id2 = 1857486
api_hash2 = "c18f271b7502c6547d4ec396662d38e9"
username2 = "anat"

energy =  {1269209704:{'full':1}, 1297379185:{'full':1}, 1430412043:{'full':1}, 'run':1,'eter':0}

clients =[TelegramClient(username, api_id, api_hash), TelegramClient(username1, api_id1, api_hash1), TelegramClient(username2, api_id2, api_hash2)]
client1 = clients[0]
client2 = clients[1]
client3 = clients[2]
@client1.on(events.NewMessage(chats=('rf_telegram_bot')))
@client2.on(events.NewMessage(chats=('rf_telegram_bot')))
@client3.on(events.NewMessage(chats=('rf_telegram_bot')))
async def normal_handler(event):
    s_user_id=event.message.to_dict()['from_id']
    messag = event.message.to_dict()['message']
    to_id = event.message.to_dict()['to_id']['user_id']
    print("toooooo >>>>>>>> ",to_id)
    print(energy[to_id])
    print(energy['run']>0)
    mess =''
    if s_user_id == 577009581:
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
                    mess='🐣1-10 Окрестности Ген. штаба'
                else :
                    mess = "🏔 Этер"
            if 'недостаточно энергии' in messag:    
                energy[to_id]['full']=0
                mess= '🏛 В ген. штаб'
            if 'направляет вас на официальный сайт ' in messag:    
                entities = event.message.entities
                for ent in entities:
                    if isinstance(ent,MessageEntityTextUrl):
                        if "rf-telegram.com/capcha" in ent.url:
                            sleep(randint(5,15))
                            r = requests.get(ent.url)
                            print(r)
                            page = BeautifulSoup(r.text, features ="html.parser")
                            button = page.find("button",{"id":"btn"})
                            data_id = button.attrs['data-id']
                            data_test = button.attrs['data-test']
                            ref_start_link = button.attrs['data-id2']
                            sleep(randint(2,5))
                            r= requests.get('https://rf-telegram.com/capcha-approve/'+data_id +'::'+data_test)
                            mess = '/start '+ref_start_link
   
            if mess :
                sleeptime = randint(5,35)
                print("sleeping for:", sleeptime, "seconds before ", mess) 

                sleep(sleeptime)
                client = event.client
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
