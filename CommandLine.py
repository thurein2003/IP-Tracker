# need to install packages -> pip install ip2geotools
import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance
from colorama import Fore 
import pyfiglet
from colorama import init, Fore, Style

# Initialize colorama
init()

# Spider ASCII art
spider = """
    ╭━━━━╮
   ╭┃⛧⛧┃╮╭┳━━━┳╮
   ┃┃⛧⛧┃┃┃╭━╮┣╋╮┃
   ╰┫⛧⛧┃╯╰┫╭╯┃┃╰╯
   ╱┃⛧⛧┃╭╮┃┃╰┫┃╭╮
   ╱╰━━╯╰╯╰┻━━┻╯╰╯
"""


print(f"{Fore.YELLOW}{spider}")
print(f"{Fore.GREEN}[*] {Style.RESET_ALL}Running your Python...

def printDis(ip):
    ans = DbIpCity.get(ip, api_key="free")
    print(f"IP address : {ans.ip_address}")
    print(f"Location : {ans.city}, {ans.country}")
    print(f"Coordinates : {ans.longitude}, {ans.latitude}")

name = "EchTit"
font = pyfiglet.figlet_format(name)
print(Fore.RED + font)


Number1 = ("Go with IP address : 1\n")
Number2 = ("Go with Url address : 2\n")
print(Number1)
print(Number2)
inputans = int(input("Enter Your choice : "))

if inputans == 1 :
    ip_address = input("Enter target IP : ")
    printDis(ip_address)
elif input == 2:
    url_address = input("Enter Your URL : ")
    ip_address = socket.gethostbyname(url_address)
    printDis(ip_address)
else :
    print("Try again!")