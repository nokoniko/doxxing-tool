import webbrowser,  time
import requests as req
from colorama import Fore

url: str = 'https://checkip.amazonaws.com'
request = req.get(url)
ip: str = request.text

def ip_look():
    stupid = input(f"{Fore.GREEN}[?]{Fore.BLUE} input ip adress:{Fore.RESET} ").lower()
    webbrowser.open(f'https://whatismyipaddress.com/ip/{ip}')
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # yes this is so funny
    
