import os,sys

import time

import pyshorteners

os.system("pip install pyshorteners")

os.system("clear")

time.sleep(3)

print("""

\033[1;32;40m

 _   _      _       _                _

| | | |_ __| |  ___| |__   ___  _ __| |_ _ __   ___ _ __

| | | | '__| | / __| '_ \ / _ \| '__| __| '_ \ / _ \ '__|

| |_| | |  | | \__ \ | | | (_) | |  | |_| | | |  __/ |

 \___/|_|  |_| |___/_| |_|\___/|_|   \__|_| |_|\___|_|

          

+=========================================+""")


print("[+] Tool Name:URL-Shortner")

print("[+] Author:Yousuf Shafi'i Muhammad. Junior Programmer")

print("[+] Version:1.0")

print("[+] Team:Junior Programmers")

print("[+] Github:https://github.com/Yousuf9963/phone-num-info")

print("[+] Follow me on Github: https://github.com/Yousuf9963")

print("[-] Website: muhammadabdirahman.wixsite.com/yousuf9963blog.")

print("[!] legal disclaimer: Usage of this Program for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.")

print("Motto: [+] I hope for you good future and i am willing that you will come high effort.")

print("")

print("""

 [1] Tinyurl

 [2] Chilp.it

 [3] Clck.ru

 [4] Da.gd

 [5] Exit the program

  """)

web = input(" Choose any of your choice : ")

if web == "1":

	os.system("clear")	
	
	print("""

\033[1;32;40m

 _   _      _       _                _

| | | |_ __| |  ___| |__   ___  _ __| |_ _ __   ___ _ __

| | | | '__| | / __| '_ \ / _ \| '__| __| '_ \ / _ \ '__|

| |_| | |  | | \__ \ | | | (_) | |  | |_| | | |  __/ |

 \___/|_|  |_| |___/_| |_|\___/|_|   \__|_| |_|\___|_|

          

          [+] By Yousuf Shafi'i Muhammad Junior Programmer.

""")

	site = input("Enter the Site Link : ")

	s = pyshorteners.Shortener()

	print("The shortened link :", s.tinyurl.			short(site))

elif web == "2":

	

	os.system("clear")

	print("""

\033[1;32;40m

 _   _      _       _                _

| | | |_ __| |  ___| |__   ___  _ __| |_ _ __   ___ _ __

| | | | '__| | / __| '_ \ / _ \| '__| __| '_ \ / _ \ '__|

| |_| | |  | | \__ \ | | | (_) | |  | |_| | | |  __/ |

 \___/|_|  |_| |___/_| |_|\___/|_|   \__|_| |_|\___|_|

          

          [+] By Yousuf Shafi'i Muhammad Junior Programmer.

""")

	site = input("Enter the Site Link : ")

	s = pyshorteners.Shortener()

	print("The Shortened link : ", s.chilpit.		short(site))

elif web == "3":

	

	os.system("clear")

	print("""

\033[1;32;40m

 _   _      _       _                _

| | | |_ __| |  ___| |__   ___  _ __| |_ _ __   ___ _ __

| | | | '__| | / __| '_ \ / _ \| '__| __| '_ \ / _ \ '__|

| |_| | |  | | \__ \ | | | (_) | |  | |_| | | |  __/ |

 \___/|_|  |_| |___/_| |_|\___/|_|   \__|_| |_|\___|_|

          

          [+] By Yousuf Shafi'i Muhammad Junior Programmer.

""")

	site = input("Enter The Site Link : ")

	s = pyshorteners.Shortener()

	print("The shortened link : ", s.clckru.		short(site))

elif web == "4":

	

	os.system("clear")

	print("""

\033[1;32;40m

 _   _      _       _                _

| | | |_ __| |  ___| |__   ___  _ __| |_ _ __   ___ _ __

| | | | '__| | / __| '_ \ / _ \| '__| __| '_ \ / _ \ '__|

| |_| | |  | | \__ \ | | | (_) | |  | |_| | | |  __/ |

 \___/|_|  |_| |___/_| |_|\___/|_|   \__|_| |_|\___|_|

          

          [+] By Yousuf Shafi'i Muhammad Junior Programmer.

""")

	site = input("Enter the Site Link : ")

	s = pyshorteners.Shortener()

	print("The shortened link : ", s.dagd.		short(site))	
	
	os.system ("xdg-open https://chat.whatsapp.com/IcFWDRiYVBx7nAxc0VIAzl")

elif web == "5":

	sys.exit()

else:

	print("\033[1;31;40mError : Please enter a digit \033")

	
	
