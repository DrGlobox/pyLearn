#! /usr/bin/python
# -*- coding: utf-8 -*-

import random

import signal
import sys
def signal_handler(signal, frame):
	 print "\n\nGood Bye"
	 sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

FILES = [
		  #"verbe",
		  "LE03",
		  #"LE02",
		  ]
DATA = []
FAIL = []

def loadFILE():
	global DATA
	for FILE in FILES:
		f = open(FILE, 'r')
		f_data = f.read().split("\n")
		for data in f_data:
			 if data and len(data.split("@@")) == 2 :
				  DATA += [data.split("@@")]

def loadLastTest():
	LST = []
	f = open("save", 'r')
	f_data = f.read().split("\n")
	for data in f_data:
		 if data and len(data.split("@@")) == 2 :
			  LST += [data.split("@@")]
	return LST

def save(LST):
	 f = open("save",'w')
	 for lst in LST :
		  f.write(lst[0]+"@@"+lst[1]+"\n")

def question(ask, answer):
	user_say = raw_input(ask+ ":\t")
	return user_say == answer

def startTest(datas):
	global FAIL
	print "\033[H\033[2J"
	print "\n\n\033[33m START new test\033[0m"
	FAIL = []
	for data in datas:
		print str(datas.index(data)+1) +"/"+str(len(datas))+" :",
		if question(data[0],data[1]):
			print "\033[32m right : ",
		else:
			print "\033[31m wrong : ",
			FAIL += [data]
		print data[1] +"\033[0m"
	total = len(DATA)	
	result = total - len(FAIL)
	print "\n\n\033[33m End of test your result : "
	print "\t\t "+ str(result) +" / "+ str(total)
	print "press 's' to save and quit"
	print "\033[0m"
	res = raw_input("Press :")
	if res == "s" :
		save(FAIL)		
		print "\n\nGood Bye"
		sys.exit(0)
	else :
		 startTest(FAIL)

def choice_traitement(choice):
	if choice == "q" :  
		print "\n\nGood Bye"
		sys.exit(0)
	elif choice == "1":
		startTest(DATA)
	elif choice == "2":
		COPY_DATA = DATA[:]
		RANDOM_DATA = []
		index = 0
		while(len(COPY_DATA) != 0):
			index = random.randint(0, len(COPY_DATA)-1)
			RANDOM_DATA += [COPY_DATA.pop(index)]
		startTest(RANDOM_DATA)
	elif choice == "3":
		LAST_TEST = loadLastTest()
		startTest(LAST_TEST)
	elif choice != "" :
		print "\033[31m error : invalid code \033[0m ",
		raw_input("press any key to return to the menu")

def menu():
	choice = ""
	while(1):
		choice_traitement(choice)
		print "\033[H\033[2J"
		print "\n\n\033[33m Welcome to pyLearn"
		print "\t 1 - Start test"
		print "\t 2 - Start Random test"
		print "\t 3 - Restart last test"
		print "\t q - exit"
		print "\033[0m"
		choice = raw_input("\033[33m What is your choice ? : \033[0m")

loadFILE()
menu()

