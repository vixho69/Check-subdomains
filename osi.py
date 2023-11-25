import socket
import requests
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

print(amarillo + "ingresa de un dominio.")
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
                    print(verde + "Dominio:", enlace2)
                elif rr.status_code == 404:
                    print(rojo + "Dominio:", enlace2)
                else:
                    pass
            except requests.exceptions.ConnectionError:
                print(rojo + f"Dominio: {enlace2}")
            try:
                pp = socket.gethostbyname(enlace2)
                print(verde + f"IP: {pp}")
            except socket.gaierror:
                pass
            try:
                tt = requests.get(enlace)
                yy = tt.headers
                if "Server" in yy and "cloudflare" in yy["Server"].lower():
                    print(verde + "CloudFlare:",verde + "True")
                else:
                    print(verde +"CloudFlare:", rojo + "False")
            except requests.exceptions.ConnectionError:
                pass
ss()
