#!/usr/bin/python3

#################
#               #
# Only for test #
#               #
#################

import hashlib, time, os, sys

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

print(color.BOLD)
os.system('clear')
print(color.RED + """
██╗  ██╗██╗  ██╗███████╗██╗  ██╗ ██████╗ ███╗   ██╗████████╗██████╗ ██████╗ 
██║  ██║██║  ██║██╔════╝██║  ██║██╔═████╗████╗  ██║╚══██╔══╝╚════██╗██╔══██╗
███████║███████║███████╗███████║██║██╔██║██╔██╗ ██║   ██║    █████╔╝██████╔╝
██╔══██║╚════██║╚════██║██╔══██║████╔╝██║██║╚██╗██║   ██║    ╚═══██╗██╔══██╗
██║  ██║     ██║███████║██║  ██║╚██████╔╝██║ ╚████║   ██║   ██████╔╝██║  ██║
╚═╝  ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝
                                                              by TheMasterCH

""")
print(color.CYAN + "Telegram : " + color.GREEN + "t.me/rebl0x3r")
flag = 0
hash = input(color.BLUE + "[*] Enter MD5 hash: " + color.PURPLE + "")
wordlist = input(color.YELLOW + "[*] Enter Wordlist: " + color.PURPLE + "")
os.system('clear')
time.sleep(1)
status = 'Cracking'

try:
    file = open(wordlist, "r")
except:
    print("[!] No File Found!")
    quit()

print('[*] Cracking...')
print(color.BOLD)
print('')
print('')
print(color.RED + "Status : " + color.BLUE + status)
time.sleep(2)

for word in file:
    encode = word.encode('utf-8')
    digest = hashlib.md5(encode.strip()).hexdigest()
    

    if digest == hash:
        #os.system('clear')
        print('[+] Password Found.')
        print('[*] Password is: ' + color.GREEN + word)
        flag = 1
        status = "Cracked"
        print(color.BOLD)
        print(color.RED + "Status : " + color.BLUE + status)        
        break
    
if flag == 0:
    #os.system('clear')
    print("[!] Password is not in the list.")
    status = "Not Cracked"
    print(color.BOLD)
    print(color.RED + "Status : " + color.BLUE + status)     
    quit()
