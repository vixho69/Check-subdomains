import socket
import requests
import colorama

red = colorama.Fore.RED
green = colorama.Fore.GREEN
magenta = colorama.Fore.MAGENTA
yellow = colorama.Fore.YELLOW
reset = colorama.Fore.RESET

print(
    magenta
    + """
 ▄█▀▀▀█▄█           ▄██                    ▀███                                     ██                    
▄██    ▀█            ██                      ██                                                           
▀███▄   ▀███  ▀███   ██▄████▄           ▄█▀▀███   ▄██▀██▄▀████████▄█████▄  ▄█▀██▄ ▀███ ▀████████▄  ▄██▀███
  ▀█████▄ ██    ██   ██    ▀██        ▄██    ██  ██▀   ▀██ ██    ██    ██ ██   ██   ██   ██    ██  ██   ▀▀
▄     ▀██ ██    ██   ██     ██  █████ ███    ██  ██     ██ ██    ██    ██  ▄█████   ██   ██    ██  ▀█████▄
██     ██ ██    ██   ██▄   ▄██        ▀██    ██  ██▄   ▄██ ██    ██    ██ ██   ██   ██   ██    ██  █▄   ██
█▀█████▀  ▀████▀███▄ █▀█████▀          ▀████▀███▄ ▀█████▀▄████  ████  ████▄████▀██▄████▄████  ████▄██████▀

                                        By: Little.Kid
"""
)


def domain_exists(domain: str):
    try:
        request = requests.get(f"https://{domain}", timeout=10)
    except ConnectionError:
        print(f"[{red}ERROR{reset}] Domain does NOT exist")
        return False
    else:
        return True


domain = input(f"{yellow} Domain >>")

while not domain_exists(domain):
    print(f"[{red}ERROR]{reset}] You have to write a valid domain")
    domain = input(f"{yellow} Domain >>")


with open("sub.txt", "r") as osi:
    if not osi:
        print(f"[{red}ERROR{reset}] No subdomains on list! check your sub.txt")
        exit()
    for con in osi:
        link_1 = f"http://{con.strip()}.{domain}"
        link_2 = f"www.{con.strip()}.{domain}"
        try:
            req = requests.get(link_1)
            print(green + f"Domain: {link_2} {reset}[{green}{req.status_code}{reset}]")
        except ConnectionError:
            print(red + f"Domain: {link_2}")
            continue
        try:
            pp = socket.gethostbyname(link_2)
            print(green + f"IP: {pp}")
        except socket.gaierror:
            print(f"[{red}ERROR{reset}] No address assosiated: {link_2}")
            continue
        req = requests.get(link_1)
        headers = req.headers
        if "Server" in headers.keys() and "cloudflare" in headers["Server"].lower():
            print(green + "CloudFlare: True")
        else:
            print(green + "CloudFlare:", red + "False")
