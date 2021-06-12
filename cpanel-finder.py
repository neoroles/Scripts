#!/usr/bin/python3

import requests
import os
import sys
import time
import threading
import queue


def clear():
	if sys.platform.startswith('win32'):
		os.system('cls')
	else:
		os.system('clear')

clear()

banner= """\033[34;1m╔═╗╔═╗╔═╗╔╗╔╔═╗╦  \033[32m ╦  ╦╔═╗╦  ╦╔╦╗
\033[34m║  ╠═╝╠═╣║║║║╣ ║  \033[32m ╚╗╔╝╠═╣║  ║ ║║
\033[34m╚═╝╩  ╩ ╩╝╚╝╚═╝╩═╝\033[32m  ╚╝ ╩ ╩╩═╝╩═╩╝
\033[33m╦  ╔═╗╔═╗╦╔╗╔\033[31m ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗   
\033[33m║  ║ ║║ ╦║║║║\033[31m ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝  
\033[33m╩═╝╚═╝╚═╝╩╝╚╝\033[31m ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═\033[0m

\033[32;1mWritten by @MrBlackX\033[0m
"""
print(banner)
class Main:
	inputQueue = queue.Queue()

	def __init__(self):
		self.urls = input("\033[34m[\033[33m*\033[34m]\033[37m Input your url list:\033[32m ")
		self.thread = input("\033[34m[\033[33m*\033[34m]\033[37m Input threads:\033[32m ")
		self.countList = len(list(open(self.urls)))
		print('')

	def save_to_file(self, nameFile, x):
		kl = open(nameFile, "a+")
		kl.write(x)
		kl.close()

	def post_req(self, url):
		url2 = url+":2083/"
		try:
			t = requests.get(url2, timeout=5)
			if t.status_code == 200:
				return 'live'
			else:
				return 'die'
		except Exception as e:
			#print(e)
			return 'error'
	def chk(self):
		while 1:
			url = self.inputQueue.get()
			rez = self.post_req(url)
			if rez == 'die':
				print(f"\033[34m[\033[31m!\033[34m]\033[37m BAD \033[31m{url}:2083/ \033[37m| \033[34m[\033[31mCPANEL VALID LOGIN CHECKER - 1.0\033[34m]")
			elif rez == 'live':
				print(f"\033[34m[\033[32m*\033[34m]\033[37m LIVE \033[32m{url}:2083/ \033[37m| \033[34m[\033[32mCPANEL VALID LOGIN CHECKER - 1.0\033[34m]")
				self.save_to_file("live.txt", url+":2083/login/?login_only=1\n")
			elif rez == 'error':
				print(f"\033[34m[\033[31m!\033[34m]\033[37m ERROR \033[31m{url}:2083/ \033[37m| \033[34m[\033[31mCPANEL VALID LOGIN CHECKER - 1.0\033[34m]")

	def run_thread(self):
		for x in range(int(self.thread)):
			t = threading.Thread(target=self.chk)
			t.setDaemon(True)
			t.start()
		for y in open(self.urls, 'r').readlines():
			self.inputQueue.put(y.strip())
		self.inputQueue.join()


heh = Main()
heh.run_thread()