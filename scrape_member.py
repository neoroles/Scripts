#!/usr/bin/python3
import sys
import csv
import random
import traceback
import time
import os
from time import sleep
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest

api_id = ""
api_hash = "" 
phone = ""
__author__		= "mrblackx"
__version__		= "1.0"
__description__	= "Simple Group Members Scraper"

def clear():
	if sys.platform.startswith('win32'):
		os.system('cls')
	else:
		os.system('clear')
clear()
banner = f"""\033[34m
\033[34m████████╗   \033[31m███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
\033[34m╚══██╔══╝   \033[31m██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
\033[34m   ██║\033[37m█████╗\033[31m███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
\033[34m   ██║\033[37m╚════╝\033[31m╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
\033[34m   ██║      \033[31m███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
\033[34m   ╚═╝      \033[31m╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝

\t\t\033[33mAuthor  	: \033[35m{__author__}
\t\t\033[33mVersion 	: \033[35m{__version__}
\t\t\033[33mDescription 	: \033[35m{__description__}

"""

print(banner)


if not api_id:
	print("\033[34m[\033[31m!\033[34m]\033[31m You need to specify your details! Missing : \033[35mapi_id\n")
	sys.exit(1)
if not api_hash:
	print("\033[34m[\033[31m!\033[34m]\033[31m You need to specify your details! Missing : \033[35mapi_hash\n")
	sys.exit(1)
if not phone:
	print("\033[34m[\033[31m!\033[34m]\033[31m You need to specify your details! Missing : \033[35mphone\n")
	sys.exit(1)

try:
	client = TelegramClient(phone, api_id, api_hash)
	client.connect()
	if not client.is_user_authorized():
		client.send_code_request(phone)
		client.sign_in(phone, input("Enter the code: "))
except:
	print("\033[34m[\033[31m!\033[34m]\033[31m Invalid Authentication, Please Contact : \033[35mhttps://t.me/f4c3r100\n")
	sys.exit(1)

chats = []
last_date = None
chuck_size = 200
groups = []

result = client(GetDialogsRequest(offset_date=last_date, offset_id=0,offset_peer=InputPeerEmpty(), limit=chuck_size, hash=0))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue

i=0
print("\033[34m[\033[33m*\033[34m]\033[37m Choose a group\n")
sleep(1)
for g in groups:
	print('\033[34m' + str(i) + '\033[37m - \033[32m' + g.title)
	i+=1

g_index = input("\n\033[34m[\033[31m?\033[34m] \033[37mEnter a Number\033[34m=> \033[31m")
target_group = groups[int(g_index)]

print("\033[34m[\033[32m*\033[34m] \033[37mFetching Members...")
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)

print("\033[34m[\033[32m*\033[34m] \033[37mSaving to file....")
with open("members.csv", "a+", encoding="UTF-8") as f:
	writer = csv.writer(f,delimiter=",",lineterminator="\n")
	writer.writerow(['username','user_id','name'])
	for user in all_participants:
		if user.username:
			username = user.username
		else:
			username = ""
		if user.first_name:
			first_name = user.first_name
		else:
			first_name = ""
		if user.last_name:
			last_name = user.last_name
		else:
			last_name = ""
		name = (first_name + ' ' + last_name).strip()
		writer.writerow([username,user.id,name])

print("\033[34m[\033[32m*\033[34m] \033[37mMember scraped successfully")

