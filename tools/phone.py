import webbrowser, time
from colorama import Fore

def phone():
    phone = input(f"{Fore.GREEN}[?]{Fore.BLUE} input phone number:{Fore.RESET} ").lower()
    webbrowser.open(f"https://www.whitepages.com/phone/{phone}")
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # yes this is so funny
