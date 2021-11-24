import requests
import time

TOKEN = "dynv6 token/username"
DOMAINS = ["example.com", "example2.com"]

current_pip = ""

def get_ip():
    return requests.get('https://api.ipify.org').text

def update(new_ip):
    for domain in DOMAINS:
        link = f"http://dynv6.com/api/update?hostname={domain}&token={TOKEN}&ipv4={new_ip}"
        requests.get(link)
        return f"changed ip to {new_ip}"

while True:
    new_pip = get_ip()
    if current_pip != new_pip:
        display_new_ip = update(new_pip)
        current_pip = get_ip()
        print(display_new_ip)
    time.sleep(10)