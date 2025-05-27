import webbrowser, socket, time
from colorama import Fore 

hostname = socket.gethostname()

def name_look():
    why = input(f"{Fore.GREEN}[?]{Fore.BLUE} input name:{Fore.RESET} ").lower()
    webbrowser.open(f"https://www.whitepages.com/name/{hostname}?fs=1&q={hostname}")
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # yes this is so funny
    
