import socket
import requests
from datetime import datetime
import sys

rojo = "\033[31;1m"
verde = "\033[92m"
magenta = "\033[36m"
amarillo = "\033[33m"

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

print(rojo + "Ingresa un dominio, ejemplo: google.com")
cosa_fea = input(">> ")
print(amarillo + "ingresa de nuevo el dominio.")
cosa_fea2 = input(">> ")
if cosa_fea2 == "":
    print("ingresa algo XDDDDDDDDDDDDDDDDD")
    sys.exit()
else:
    pass
def ss():
    with open("sub.txt","r") as osi:
        for cosa in osi:
            enlace = f"https://{cosa.strip()}.{cosa_fea2}"
            enlace2 = f"www.{cosa.strip()}.{cosa_fea2}"
            print("")
            try:
                rr = requests.get(enlace)
                if rr.status_code == 200:
                    print(verde + "Dominio:", enlace2)
                else:
                    print(rojo + "Dominio:", enlace2)
            except:
                print(rojo + f"Dominio: {enlace2}")
            try:
                pp = socket.gethostbyname(enlace2)
                print(verde + f"IP: {pp}")
            except:
                pass
            try:
                tt = requests.get(enlace)
                yy = tt.headers
                if "Server" in yy and "cloudflare" in yy["Server"].lower():
                    print("CloudFlare:",verde + "True")
                    h = datetime.now().strftime("%H:%M, %d-%m-%Y")
                    print(verde + "Hora de revisión:", h)
                else:
                    print("CloudFlare:", rojo + "False")
                    qw = datetime.now().strftime("%H:%M, %d-%m-%Y")
                    print(verde + "Hora de revisión:", qw)
            except:
                pass

ss()
