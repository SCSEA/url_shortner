import os

os.system("clear")

print("[+] Tool Name:URL-Shortner")

print("[+] Author:Yousuf Shafi'i Muhammad. Junior Programmer")

print("[+] Version:1.0")

print("[+] Team:Junior Programmers")

print("[+] Github:https://github.com/Yousuf9963/phone-num-info")

print("[+] Follow me on Github: https://github.com/Yousuf9963")

print("[-] Website: muhammadabdirahman.wixsite.com/yousuf9963blog.")

print("[!] legal disclaimer: Usage of this Program for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.")

print("[+] Motto: I hope for you good future and i am willing that you will come high effort.")

print("")

os.system("pip install pyshorteners")

os.system("pip install requests")

print("[+] Tool Name:URL-Shortner")

print("[+] Author:Yousuf Shafi'i Muhammad. Junior Programmer")

print("[+] Version:1.0")

print("[+] Team:Junior Programmers")

print("[+] Github:https://github.com/Yousuf9963/phone-num-info")

print("[+] Follow me on Github: https://github.com/Yousuf9963")

print("[-] Website: muhammadabdirahman.wixsite.com/yousuf9963blog.")

print("[!] legal disclaimer: Usage of this Program for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.")

print("[+] Motto: I hope for you good future and i am willing that you will come high effort.")

print("")

import requests

long_url = input("Enter Union Resource Locator.URL: ")

url = 'http://tinyurl.com/api-create.php?'

params = {'url':long_url}

r = requests.get(url, params=params)

print("The shortened URL is:", r.text)

os.system ("xdg-open https://chat.whatsapp.com/IcFWDRiYVBx7nAxc0VIAzl")



