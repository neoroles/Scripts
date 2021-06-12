import requests, time, secrets , datetime , webbrowser
from colorama import Fore
from instabot import Bot
from instabot import api
from tqdm import tqdm
R=Fore.RED
P=Fore.GREEN
sd=Fore.LIGHTGREEN_EX
s=Fore.BLACK
y=Fore.LIGHTYELLOW_EX
u=Fore.LIGHTRED_EX
a=Fore.LIGHTCYAN_EX
asd=Fore.LIGHTMAGENTA_EX
bot=Bot()
fill=datetime.datetime.now()
print(f'''
              {asd} 888 {asd}.d88b       
              {u}  8  {y}8P          
              {u}  8  {y}8b  d8       
              {asd} 888 {asd}`Y88P'
{y}*======================================*********
{y}*[1]->{a}get full info about your account   {y}*
{y}*[2]->{a}delete profile pic                 {y}*
{y}*[3]->{a}get user id from username          {y}*
{y}*[4]->{a}get post id from url               {y}*
{y}*[5]->{a}block + {asd}unblock + {u}unfollow         {y}* 
{y}*[6]->{a}get post info ig                   {y}*
{y}*[7]->{a}get full info about user           {y}*
{y}*[8]->{a}CHECKERS IG                        {y}*
{y}*=====================================**********
''')

print(u+'\n'+f'''
{fill}
𝙥𝙧𝙤𝙜𝙧𝙖𝙢𝙚𝙙-𝗙𝗶𝗹𝘇𝗮_𝟱𝟬𝟳
𝖈𝖍➥𝑻𝒘𝒆𝒂𝒌𝑷𝒀
MY TELE:@Filza_507 and @Filza5
MY BOT ON TELE:@Filza_Chating_bot
ch:https://t.me/TweakPY
''')
webbrowser.open('https://t.me/TweakPY')
print(y+f'NOT FOR SELL{u}')
for _ in tqdm(
        range(50),
        desc="Login..",):
    time.sleep(0.1)
print('\nDone L0GIN')
mod = input('Enter num ➦:\n')

if mod=='1':
    print(y + 'ACC INFO')
    print(s+'=================================================')
    user = input(u + "user➦:")
    pess = input(u + "pass➦:")
    print(y + '===============================================')
    print(u+'now get the info..')
    bot.login(username=user, password=pess)
    print(s+'done the full info is saved in file named config')
elif mod=='2':
    print(y + 'PIC REMOVE')
    print(y + '=================================================')
    user = input(u + "user➦:")
    pess = input(u + "pass➦:")
    print(y + '=================================================')
    bot.login(username=user, password=pess)
    print(P+'remove the pic now.....')
    print(P+'the pic removed.')
    bot.api.remove_profile_picture()
elif mod=='3':
    print(y + 'USER ID ')
    print(y+'=======================================')
    user = input(R + "user➦:")
    pess = input(R + "pass➦:")
    print(y+'=======================================')
    print(u + 'login..')
    bot.login(username=user, password=pess)
    print(u+'login done now enter user to get the id')
    ad=input(P+'username➦:')
    op=bot.get_user_id_from_username(username=ad)
    print(P + 'ID IS ➦:' + op)
elif mod=='4':
    print(y + 'POST ID')
    print(u+'================================')
    ol = input(P + f'post{s} url:' + '\n')
    rafa = bot.get_media_id_from_link(link=ol)
    print(P+f'now getting{u} the info...')
    print(y+f'THE POST{R} ID IS {u}->:' + '\n', rafa)
    print(u + '================================')
elif mod=='5':
    print('''(1)block user\n(2)unblock user\n(3)unfollow user''')
    mode=input("➦:\n")
    if mode=='1':
        print(y + 'INSTA BLOCK')
        print(y + '=======================================')
        user = input(R + "user➦:")
        pess = input(R + "pass➦:")
        print(y + '=======================================')
        print(u + 'login..')
        bot.login(username=user, password=pess)
        print(u + 'login done now enter user id to block him')
        ks = input(P + "user id➦:")
        bot.api.block(user_id=ks)
        print(y + '* block on his face *')
        print(P + 'done.')
    elif mode=="2":
        print(y + 'INSTA UNBLOCK')
        print(y + '=======================================')
        user = input(R + "user➦:")
        pess = input(R + "pass➦:")
        print(y + '=======================================')
        print(u + 'login..')
        bot.login(username=user, password=pess)
        print(u + 'login done now enter user id to unblock him')
        ks = input(P + "user id➦:")
        bot.api.unblock(user_id=ks)
        print(y + '* unblock done. *')
    elif mode=="3":
        print(y + 'INSTA UNFOLLOW')
        print(y + '=======================================')
        user = input(R + "user➦:")
        pess = input(R + "pass➦:")
        print(y + '=======================================')
        print(u + 'login..')
        bot.login(username=user, password=pess)
        print(u + 'login done now enter user id to unfollow him')
        ks = input(P + "user id➦:")
        bot.api.unfollow(user_id=ks)
        print(y + '* unfollow done. *')
elif mod=='6':
    print(y + 'POST INFO')
    print(y + '=======================================')
    will = input(R + 'post url ➦:')
    print(y + '=======================================')
    url = will
    filza = requests.get(url)
    FID = filza.content
    content = (FID)
    LHK = requests.get(url)
    filza5555 = requests.get(url)
    cokies = (filza.cookies)
    WeB = requests.get(url)
    head = (WeB.headers)
    with open("POST_INFO", 'a') as x:
        x.write(f'{FID}\n{content}\n{head}\n{cokies}\n{LHK}\n{filza5555}')
        print(y + '*-- done  --*')
        print(y + '*-- file has been saved  --*')
elif mod=='7':
    print(y + 'INSTA info')
    head = {
        'HOST': "www.instagram.com",
        'KeepAlive': 'True',
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
        'Cookie': 'cookie',
        'Accept': "*/*",
        'ContentType': "application/x-www-form-urlencoded",
        "X-Requested-With": "XMLHttpRequest",
        "X-IG-App-ID": "936619743392459",
        "X-Instagram-AJAX": "missing",
        "X-CSRFToken": "missing",
        "Accept-Language": "en-US,en;q=0.9"}
    while 1:
        cookie = secrets.token_hex(8) * 2
        r = requests.Session()
        print(u + "==============================")
        target = input('[+] Enter User ➦ : ')
        print(u + "==============================")
        url_id = f'https://www.instagram.com/{target}/?__a=1'
        req_id = r.get(url_id, headers=head).json()
        bio = str(req_id['graphql']['user']['biography'])
        url = str(req_id['graphql']['user']['external_url'])
        nam = str(req_id['graphql']['user']['full_name'])
        idd = str(req_id['graphql']['user']['id'])
        isp = str(req_id['graphql']['user']['is_private'])
        isv = str(req_id['graphql']['user']['is_verified'])
        pro = str(req_id['graphql']['user']['profile_pic_url'])
        print(y+"==============================")
        print(f'[-]  :)\n[-] Name : {nam}\n[-] Id : {idd}\n[-] private : {isp}\n[-] verified : {isv}\n[-] Bio : {bio}\n[-] Profile picture : {pro}')
        print(y+"==============================")
elif mod=='8':
    print(y+"(1)CHECK IG\n(2)CHECK IG 2")
    modee=input(u+"Enter num➦:")
    if modee=='1':
        print(y+'INSTA checker')
        x2 = '[🖤] @TweakPY - @Filza5'
        j = '''
        [☑️] INSTAGRAM USER:︎︎
        '''
        print(y + "==============================")
        idd = input(R+"enter id➦:")
        token = input(R+"enter token➦:")
        print(y + "==============================")
        username = "user.txt"
        ff = username
        file = open(ff).read().splitlines()
        for file in file:
            url_checker = 'https://www.instagram.com/accounts/login/ajax/'
            headers_checker = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                'content-length': '301',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_did=D37E2F4F-6193-4E76-B7C6-6FDBE4A0C230; mid=X_3LtAALAAFAdQMURlFUf_U68Q6H; ig_nrcb=1; shbid=11548; shbts=1614375967.569843; rur=RVA; csrftoken=F5iBJQbC6vTjOfgvA01urbEOsfgzgZBX',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/login/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
                'x-csrftoken': 'F5iBJQbC6vTjOfgvA01urbEOsfgzgZBX',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR1Y1dEsDcV-xq-u_7U0XISuyjCpWSS-VvmOhVU2N6rp9zKR',
                'x-instagram-ajax': '0edc1000e5e7',
                'x-requested-with': 'XMLHttpRequest'
            }
            data_checker = {
                'username': file,
                'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1613414957:dsbvhdbvdsvbsdh',
                'queryParams': '{}',
                'optIntoOneTap': 'false'
            }
            req = requests.post(url_checker, data=data_checker, headers=headers_checker).text
            if '"user":false' in req:
                print(P+f'[✅] متاح ==> :{file}')
                with open('متاحات.txt', 'a') as x:
                    x.write(file + '\n')
                    tele = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={idd}&text={j}\n𖡃 𝚄𝚂𝙴𝚁: {file}\n\n{x2}')
                    re = requests.post(tele)
            else:
                print(u+f'[❌] غير متاح ==> : {file}')
    elif modee=='2':
        print(y + 'INSTA checker')
        r = requests.session()
        x2 = '[🖤] @TweakPY - @Filza5'
        j = '''
            [☑️] INSTAGRAM USER:︎︎
            '''
        print("==============================")
        idd = input("enter id➦:")
        token = input("enter token➦:")
        print("==============================")
        username = "user.txt"
        ff = username
        file = open(ff).read().splitlines()
        for file in file:
         url = f'https://instagram.com/{file}'
         req = r.get(url)

         if req.status_code == 404:
             print(P+f'[✅] متاح ==> :{file}')
             tele = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={idd}&text={j}\n𖡃 𝚄𝚂𝙴𝚁: {file}\n\n{x2}')
             re = requests.post(tele)
             with open('متاحات.txt', 'a') as x:
                 x.write(file + '\n')


         elif req.status_code == 200:
             print(u + f'[❌] غير متاح ==> : {file}')

         else:
             print(u + f'[❌] غير متاح ==> : {file}')
else:
    print(u+f"ERROR{y}➦NOT FOUND")
    print(u+f"ERROR{y}➦0")
    print(u+f"ERROR{y}➦ERROR")
    print(u+f"ERROR{y}➦ERROR")
    print(u+f"ERROR{y}➦BAD NUM")
    print(u+f"ERROR{y}➦BAD GATE")
    print(u+f"ERROR{y}➦BAD GETAWAY")
    print(u+f"ERROR{y}➦ERROR")
    print(u+f"ERROR{y}➦ERROR")
    print(u+f"ERROR{y}➦ERROR")
    print(u+f"ERROR{y}➦ERROR")
    print(u+f"ERROR{y}➦ERROR")
    print(u+f"ERROR{y}➦ERROR")
    print(u+f"ERROR{y}➦ERROR")
    exit(0)
