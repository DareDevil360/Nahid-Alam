version="2.1.9"
#IMPORT
import getpass,time,os
import signal

if os.path.isdir("/sdcard/ROC-X")!=True and os.path.isdir("$HOME/Desktop/ROC-X")!=True :
	try:
		os.mkdir("/sdcard/ROC-X")
	except:
		os.mkdir("$HOME/Desktop/ROC-X")

#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
line=yellow+"======================================================================================================================"
space=" "
logo=red+str("""
⠀⠀⢀⢀⡀⢀⣠⣄⣦⣶⣶⣿⣿⣿⣿⣿⣿⣿⣶⡀
⠀⣤⣿⣾⣷⣿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣧⡀
⢸⣿⣿⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⣿⣿⣿⣄
⢹⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡿
⠈⢿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⢻⣿⡇
⠀⢸⣿⠀⠀⠀⢻⣿⣿⣶⣀⣀⣠⣾⣿⣿⣟⡉⠃⢸⣿
⠀⠈⢿⠀⠀⠼⠒⠿⣟⠟⠃⠀⠙⠿⣿⣿⣻⠿⠃⢸⡇
⠀⠀⢈⠀⠀⠀⠀⢉⣡⣤⣶⣶⣶⣤⣀⡉⠁⠀⠀⢸
⠀⠀⠘⢶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⡿
⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁
⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧
⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏
⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟
⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⠟  """)



os.system("clear || cls")

notice=green+""

# Definition

def header():
	print(logo+cyan+"\n\n\n\t\tTOOL BY : NAHID ALAM\n\n"+green+"\t\t     Version : "+str(version)+" \n\n"+end+line+"\n"+end)

def clear():
	os.system("clear || cls")

count=1
about=7
e_count=1
ddos_count=1
kali_count=1
ms_count=1
sms_count=1
t_count=1

os.system("clear")
header()
print(cyan+"\n\t\t[•] Checking For Updates")
time.sleep(0.7)


try:
	import requests
except:
	os.system("pip install requests")
import requests
r=requests.get('https://pastebin.com/raw/0e7CzUNG')
upchck=r.text
if upchck==version:
	pass
elif upchck!=version:
	os.system("clear")
	header()
	print(cyan+"\n  [°] Installing The Updated Tools. Allow Up to 10 minutes ")
	time.sleep(2)
	os.system("clear")
	notice=cyan+"\t\t[°] Installing Updated Tools.. \n"
	header()
	notice=""
	print("\n")
	clear()
	notice=cyan+"\t\t[•] Backing up the Tool...."
	header()
	os.system("mkdir $HOME/roc-x_updater")
	os.system("cp -rf $HOME/roc-x $HOME/roc-x_updater")
	try:
		clear()
		notice=cyan+"\t\t[•] Updating the Tools...."
		header()
		os.system("cd $HOME")
		os.system("cd $HOME && rm -rf roc-x")
		print(green)
		os.system("cd $HOME && git clone https://github.com/DareDevil360/Nahid-Alam")
		clear()
		notice=green+"\t\t[√] Update Successful!"
		header()
		print(cyan+"\n [•••] TerMux Restart is Required for The Update. Please Restart Termux For The Tool Updated Version")
		#os.kill(os.getppid(), signal.SIGHUP)
		os.system("rm -rf $HOME/roc-x_updater")
		for i in range(99999999999):
			os.system("clear")
			a=input(cyan+"\n"*10+" [>] Please Exit Termux from Notification Bar. Then Again Open Tool By :\n\n "+yellow+"\t [1] Exit Termux\n\t [2] Open Termux"+"\n\t [3] cd $HOME/roc-x"+yellow+"\n\t [4] "+yellow+"python3 main.py\n\n")

	except:
		clear()
		notice=red+"\t\t[×] Update Failed!"
		header()
		sjsjstshsb=input(cyan+"\n\n\t     Press Enter to Restore Tool")
		os.system("cd $HOME")
		os.system("cd $HOME && mkdir roc-x")
		os.system("cd $HOME && cp -rf $HOME/roc-x_updater/roc-x $HOME")
		os.system("rm -rf $HOME/roc-x_updater")
		os.system("python3 $HOME/roc-x/main.py")
		for i in range(99999999999):
			os.system("clear")
			a=input(cyan+"\n"*10+" [>] Please Exit Termux from Notification Bar. Then Again Open Tool By :\n\n "+yellow+"\t [1] Exit Termux\n\t [2] Open Termux"+"\n\t [3] cd $HOME/roc-x"+yellow+"\n\t [4] "+yellow+"python3 main.py\n\n")

#Main Page

while count<2:
	clear()
	header()
	notice=""
	print(cyan+"\n==> Select the number of the option that you want to start from below : ")
	print(yellow+"\n  [1] BD SMS Bomber\n\n  [2] Nahid Alam Phishing\n\n  [3] DDoS Attacker\n\n  [4] Kali NetHunter\n\n  [5] MetaSploit FrameWork\n\n  [6] E-Mail Bomber\n\n  ["+str(about)+"] Contact Us"+end)
	main_opt=str(input(blue+"\n[>] Select Your Option : "+yellow))
	
	if main_opt=="1":
		if sms_count==1:
			import bdsms
			sms_count=2
		else:
			try:
				reload(bdsms)
			except:
				try:
					import imp
					imp.reload(bdsms)
				except:
					import importlib
					importlib.reload(bdsms)
	elif main_opt=="2":
		if t_count==1:
			import t
			t_count=2
		else:
			try:
				reload(t)
			except:
				try:
					import imp
					imp.reload(t)
				except:
					import importlib
					importlib.reload(t)
	
	elif main_opt=="6":
		if e_count==1:
			import emailtool
			e_count=2
		else:
			try:
				reload(emailtool)
			except:
				try:
					import imp
					imp.reload(emailtool)
				except:
					import importlib
					importlib.reload(emailtool)
					
		notice=""
		count=1
	elif main_opt=="3":
		if ddos_count==1:
			import ddos_opt
			ddos_count=2
		else:
			try:
				reload(ddos_opt)
			except:
				try:
					import imp
					imp.reload(ddos_opt)
				except:
					import importlib
					importlib.reload(ddos_opt)
	elif main_opt=="4":
		if kali_count==1:
			import kali
			kali_count=2
		else:
			try:
				reload(kali)
			except:
				try:
					import imp
					imp.reload(kali)
				except:
					import importlib
					importlib.reload(kali)
		
	elif main_opt=="5":
		if ms_count==1:
			import ms_opt
			ms_count=2
		else:
			try:
				reload(ms_opt)
			except:
				try:
					import imp
					imp.reload(ms_opt)
				except:
					import importlib
					importlib.reload(ms_opt)
		
	elif main_opt==str(about):
		notice=""
		print(cyan+"\n\n\tYoutube:"+yellow+"\n\n\thttps://www.youtube.com/channel/UCvVqA5t8XNCc5UeeC9c__VQ"+cyan+"\n\n\tFacebook Page:"+yellow+"\n\n\thttps://m.facebook.com/I.am.a.devil.of.my.world.d4r3d3v1l"+cyan+"\n\n\tWhat\s app':"+yellow+"\n\n\thttps://chat.whatsapp.com/JPTOWlsJhhgEVtzht4tAlr"+cyan+"\n\n\tTelegram:\n"+yellow+"https://t.me/joinchat/RScE4xF8TiQIOs2Z"+cyan+"\n\n\n\n\tContact Us:"+yellow+"\n\n\tnahidalam20052019@gmail.com"+cyan+"\n\n\n\tTool By "+yellow+"Nahid Alam"+cyan+"\n\tFB Group:"+yellow+"https://m.facebook.com/groups/423523842196228")
		a=input(cyan+"\n\n\t\t[>] Press "+yellow+"Enter"+cyan+" to Continue")
		count=1
	else:
		clear()
		notice=red+"\t\t[×] Wrong Option Entered!"
		count=1
