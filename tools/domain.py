import webbrowser, time
from colorama import Fore

def domain_look():
    domain = input(f"{Fore.GREEN}[?]{Fore.BLUE} input domain:{Fore.RESET} ").lower()
    webbrowser.open(f"https://www.norid.no/?s={domain}")
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # yes this is so funny
    
