import socket
import requests
import colorama as color
import sys

rojo = color.Fore.RED
verde = color.Fore.GREEN
magenta = color.Fore.CYAN
amarillo = color.Fore.YELLOW

print(magenta + """
 ▄█▀▀▀█▄█           ▄██                    ▀███                                     ██                    
▄██    ▀█            ██                      ██                                                           
▀███▄   ▀███  ▀███   ██▄████▄           ▄█▀▀███   ▄██▀██▄▀████████▄█████▄  ▄█▀██▄ ▀███ ▀████████▄  ▄██▀███
  ▀█████▄ ██    ██   ██    ▀██        ▄██    ██  ██▀   ▀██ ██    ██    ██ ██   ██   ██   ██    ██  ██   ▀▀
▄     ▀██ ██    ██   ██     ██  █████ ███    ██  ██     ██ ██    ██    ██  ▄█████   ██   ██    ██  ▀█████▄
██     ██ ██    ██   ██▄   ▄██        ▀██    ██  ██▄   ▄██ ██    ██    ██ ██   ██   ██   ██    ██  █▄   ██
█▀█████▀  ▀████▀███▄ █▀█████▀          ▀████▀███▄ ▀█████▀▄████  ████  ████▄████▀██▄████▄████  ████▄██████▀

                          By:  Little.Kid | Version: 1.5
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
            enlace = f"https://www.{cosa.strip()}.{lw}"
            enlace2 = f"www.{cosa.strip()}.{lw}"
            enlace3 = f"http://www.{cosa.strip()}.{lw}"
            print("")
            try:
                rev = requests.get(enlace3)
                rr = requests.get(enlace)
                if rr.status_code == 200:
                    print(verde + "Dominio:", enlace)
                elif rev.status_code == 200:
                    print(verde + "Dominio:", enlace3)
                else:
                    print(rojo + "Dominio:", enlace2)
            except requests.exceptions.ConnectionError:
                print(rojo + f"Dominio: {enlace2}")
            try:
                pp = socket.gethostbyname(enlace2)
                print(verde + f"IP: {pp}")
            except socket.gaierror:
                print("Fuera de servicio.")
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
