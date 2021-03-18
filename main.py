##################################
 # I'm no expert at coding.     #
 # I made an server launcher    #
 # Its basic.                   #
##################################
 # Creator: pepsi man           # 	
 # osu!usernames:               #
 # Ripple: - Windows -          #
 # Akatsuki: - Windows -        #
 # Bancho (banned): - Windows - #
 # Bancho (banned): lynnntn     #
##################################
 # Imports:                     #
import time                 	#
import os                   	#
from configparser import ConfigParser
import sys
def ts(a):
	time.sleep(a)
##################################
 # Use special character        #
sp = r"\\"						#
sp2 = r"\ "						#
sp3 = '"'						#
##################################
 # Configparser:                #
cfgp = ConfigParser()           #
cfgp.read('cfg.ini')        	#
 #								#
##################################
 # Detect neccesary files:      #
def ifexists(a):               	#
	if a == "cfg.ini":          #
		if str(os.path.exists(a)) == "False":
			open('cfg.ini','w+')
			f = open("cfg.ini", "w")
			f.write("""[main]
//osudir : Your osu! directory. Add """ + sp + """ instead of """ + sp2 + """ for the program to understand.
osudir = Unset
//defaultServer : Your default osu server. For example, you can set ripple.moe / akatsuki.pw or leave empty for bancho.
defaultServer = Unset""")
			f.close()			#
	else:                   	#
		pass                	#
	if str(os.path.exists(a)) == "True":
		pass                    	#
	else:                       	#
		print(a + " doesn't exist, redownload the files.")
		time.sleep(1)
 #                              #
##################################
 # Check files.                 #
print("Always check your .INI file!")
ifexists('cfg.ini')				#
ifexists('osu.exe')				#
ifexists('osuold.exe')			#
								#
 #                              #
##################################
 # Read config.
b = cfgp.get('main','osudir')
def cfgRead():
	if b == "Unset":
		print("osu! Directory is not set. Please set it in cfg.ini")
		time.sleep(5)
		quit()
	else:
		if os.path.exists(str(cfgp.get('main','osudir'))) == "False":
			print("osu! directory either doesn't work or doesn't exist.")
			time.sleep(5)
			quit()
		else:
			pass
	b = cfgp.get('main','defaultServer')
	if b == "Unset":
		print("Default Server is not set. Please set it in cfg.ini")
		time.sleep(5)
		quit()
	else:
		pass 
##################################
 # No more beautiful formatting ;-;
 # You can add some yourself!

def main():
	print("  ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ")
	time.sleep(0.2)
	print(" |______|______|______|______|______|______|______|______|______|______|______|______|______|______|")
	ts(0.2)
	print(" | | by Windows      | |                              | |                      | |               | |")
	ts(0.2)
	print(" | |   ___  ___ _   _| |  ___  ___ _ ____   _____ _ __| | __ _ _   _ _ __   ___| |__   ___ _ __  | |")
	ts(0.2)
	print(" | |  / _ \/ __| | | | | / __|/ _ \ '__\ \ / / _ \ '__| |/ _` | | | | '_ \ / __| '_ \ / _ \ '__| | |")
	ts(0.2)
	print(" | | | (_) \__ \ |_| |_| \__ \  __/ |   \ V /  __/ |  | | (_| | |_| | | | | (__| | | |  __/ |    | |")
	ts(0.2)
	print(" | |  \___/|___/\__,_(_) |___/\___|_|    \_/ \___|_|  |_|\__,_|\__,_|_| |_|\___|_| |_|\___|_|    | |")
	ts(0.2)
	print(" | |                                                                                             | |")
	ts(0.2)
	print(""" |_|____ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ____|_|
 |______|______|______|______|______|______|______|______|______|______|______|______|______|______|""")
main()

def selServer():
	print("# | Please select a server from this list. \n# | You can suggest more servers at https://discord.gg/QxyRDVkMkf")
	print("Enter | Default Server\n1 | osu!bancho \n2 | ripple.moe\n3 | Akatsuki.pw\n4 | ainu.pw ")
selServer()
def selServer2(a):
	if a == "1":
		os.system(str(cfgp.get('main','osudir')) + "osu!.exe")
	elif a == "2":
		os.system(str(cfgp.get('main','osudir')) + "osu!.exe -devserver ripple.moe")
	elif a == "3":
		os.system(str(cfgp.get('main','osudir')) + "osu!.exe -devserver akatsuki.pw")
	elif a == "4":
		os.system(sp3 + str(cfgp.get('main','osudir')) + "osu!.exe" + sp3 + " -devserver ainu.pw")
	elif a == "":
		os.system(sp3 + str(cfgp.get('main','osudir')) + "osu!.exe" + sp3 + " -devserver " + cfgp.get('main','defaultServer'))

selServer2(input("# | Please select one. Use only numbers: "))

quit()
