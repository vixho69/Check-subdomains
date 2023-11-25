import socket
import requests
import colorama
import sys

red = colorama.Fore.RED
green = colorama.Fore.GREEN
magenta = colorama.Fore.MAGENTA
yellow = colorama.Fore.YELLOW

print(magenta + """
 ▄█▀▀▀█▄█           ▄██                    ▀███                                     ██                    
▄██    ▀█            ██                      ██                                                           
▀███▄   ▀███  ▀███   ██▄████▄           ▄█▀▀███   ▄██▀██▄▀████████▄█████▄  ▄█▀██▄ ▀███ ▀████████▄  ▄██▀███
  ▀█████▄ ██    ██   ██    ▀██        ▄██    ██  ██▀   ▀██ ██    ██    ██ ██   ██   ██   ██    ██  ██   ▀▀
▄     ▀██ ██    ██   ██     ██  █████ ███    ██  ██     ██ ██    ██    ██  ▄█████   ██   ██    ██  ▀█████▄
██     ██ ██    ██   ██▄   ▄██        ▀██    ██  ██▄   ▄██ ██    ██    ██ ██   ██   ██   ██    ██  █▄   ██
█▀█████▀  ▀████▀███▄ █▀█████▀          ▀████▀███▄ ▀█████▀▄████  ████  ████▄████▀██▄████▄████  ████▄██████▀

                                        By: Little.Kid
""")

print(yellow + "ingresa de un dominio.")
lw = input(">> ")
if lw == "":
    print("ingresa algo XDDDDDDDDDDDDDDDDD")
    sys.exit()
else:
    pass
def ss():
    with open("sub.txt","r") as osi:
        for cosa in osi:
            enlace = f"http://{cosa.strip()}.{lw}"
            enlace2 = f"www.{cosa.strip()}.{lw}"
            print("")
            try:
                rr = requests.get(enlace)
                if rr.status_code == 200:
                    print(green + "Dominio:", enlace2)
                elif rr.status_code == 404:
                    print(red + "Dominio:", enlace2)
                else:
                    pass
            except requests.exceptions.ConnectionError:
                print(red + f"Dominio: {enlace2}")
            try:
                pp = socket.gethostbyname(enlace2)
                print(green + f"IP: {pp}")
            except socket.gaierror:
                pass
            try:
                tt = requests.get(enlace)
                yy = tt.headers
                if "Server" in yy and "cloudflare" in yy["Server"].lower():
                    print(green + "CloudFlare:",green + "True")
                else:
                    print(green +"CloudFlare:", red + "False")
            except requests.exceptions.ConnectionError:
                pass
ss()
