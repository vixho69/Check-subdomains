import socket
import requests
import colorama as color
import sys

print(color.Fore.CYAN + """
 ▄█▀▀▀█▄█           ▄██                    ▀███                                     ██
▄██    ▀█            ██                      ██
▀███▄   ▀███  ▀███   ██▄████▄           ▄█▀▀███   ▄██▀██▄▀████████▄█████▄  ▄█▀██▄ ▀███ ▀████████▄  ▄██▀███
  ▀█████▄ ██    ██   ██    ▀██        ▄██    ██  ██▀   ▀██ ██    ██    ██ ██   ██   ██   ██    ██  ██   ▀▀
▄     ▀██ ██    ██   ██     ██  █████ ███    ██  ██     ██ ██    ██    ██  ▄█████   ██   ██    ██  ▀█████▄
██     ██ ██    ██   ██▄   ▄██        ▀██    ██  ██▄   ▄██ ██    ██    ██ ██   ██   ██   ██    ██  █▄   ██
█▀█████▀  ▀████▀███▄ █▀█████▀          ▀████▀███▄ ▀█████▀▄████  ████  ████▄████▀██▄████▄████  ████▄██████▀

                                By: Little.Kid | Versión: 1.6
""")

print(color.Fore.YELLOW + "Ingresa de un dominio, Ejemplo: google.com")
lw = input(">> ")
if lw == "":
    print(color.Fore.RED + "No haz ingresado ninguno dominio!")
    print(color.Fore.RESET)
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
                    print(color.Fore.GREEN + "Dominio:", enlace)
                elif rev.status_code == 200:
                    print(color.Fore.GREEN + "Dominio:", enlace3)
                else:
                    print(color.Fore.RED + "Dominio:", enlace2)
            except requests.exceptions.ConnectionError:
                print(color.Fore.RED + f"Dominio: {enlace2}")
            try:
                pp = socket.gethostbyname(enlace2)
                print(color.Fore.GREEN + f"IP: {pp}")
            except socket.gaierror:
                print("Fuera de servicio.")
            try:
                tt = requests.get(enlace)
                yy = tt.headers
                if "Server" in yy and "cloudflare" in yy["Server"].lower():
                    print(color.Fore.GREEN + "CloudFlare:",color.Fore.GREEN + "True")
                else:
                    print(color.Fore.GREEN + "CloudFlare:", color.Fore.RED + "False")
            except requests.exceptions.ConnectionError:
                pass
ss()
