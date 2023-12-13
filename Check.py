import socket
import requests
import colorama as color
import sys

def logo():
    print(color.Fore.CYAN + """
 ▄█▀▀▀█▄█           ▄██                    ▀███                                     ██
▄██    ▀█            ██                      ██
▀███▄   ▀███  ▀███   ██▄████▄           ▄█▀▀███   ▄██▀██▄▀████████▄█████▄  ▄█▀██▄ ▀███ ▀████████▄  ▄██▀███
  ▀█████▄ ██    ██   ██    ▀██        ▄██    ██  ██▀   ▀██ ██    ██    ██ ██   ██   ██   ██    ██  ██   ▀▀
▄     ▀██ ██    ██   ██     ██  █████ ███    ██  ██     ██ ██    ██    ██  ▄█████   ██   ██    ██  ▀█████▄
██     ██ ██    ██   ██▄   ▄██        ▀██    ██  ██▄   ▄██ ██    ██    ██ ██   ██   ██   ██    ██  █▄   ██
█▀█████▀  ▀████▀███▄ █▀█████▀          ▀████▀███▄ ▀█████▀▄████  ████  ████▄████▀██▄████▄████  ████▄██████▀

                                By: Little.Kid | Versión: 1.8
    """)

def domain():
    print(color.Fore.YELLOW + "Ingresa un dominio, Ejemplo: google.com")
    lw = input(">> ")
    if lw == "":
        print(color.Fore.RED + "No has ingresado ningún dominio!")
        print(color.Fore.RESET)
        sys.exit()
    return lw

def check_domain(lw):
    with open("sub.txt", "r") as osi:
        for cosa in osi:
            enlace = f"https://www.{cosa.strip()}.{lw}"
            enlace2 = f"www.{cosa.strip()}.{lw}"
            print("")
            try:
                rev = requests.get(enlace)
                if rev.status_code == 200:
                    print(color.Fore.GREEN + "Dominio:", enlace)
                else:
                    print(color.Fore.RED + "Dominio:", enlace2, "OFF")
            except requests.exceptions.ConnectionError:
                print(color.Fore.RED + f"Dominio: {enlace2}")
            try:
                pp = socket.gethostbyname(enlace2)
                print(color.Fore.GREEN + f"IP: {pp}")
            except socket.gaierror:
                pass
            try:
                tt = requests.get(enlace)
                yy = tt.headers
                if "Server" in yy and "cloudflare" in yy["Server"].lower():
                    print(color.Fore.GREEN + "CloudFlare:", color.Fore.GREEN + "True")
                else:
                    print(color.Fore.GREEN + "CloudFlare:", color.Fore.RED + "False")
            except requests.exceptions.ConnectionError:
                pass
            try:
                tcode = requests.get(enlace)
                tcode2 = tcode.status_code
                print(color.Fore.GREEN + "Codigo de respuesta:",color.Fore.MAGENTA + f"{tcode2}")
            except requests.exceptions.ConnectionError:
                pass

def main():
    logo()
    lw = domain()
    check_domain(lw)

if __name__ == "__main__":
    main()
