from colorama import Fore
from pystyle import Colorate, Colors
from tools.ip import *
from tools.name import *
from tools.phone import *
from tools.domain import *

logo = r"""

            ____                           __                           
            /\  _`\                        /\ \__                        
            \ \ \/\_\  _ __   __  __  _____\ \ ,_\  __  __  _ __    __   
            \ \ \/_/_/\`'__\/\ \/\ \/\ '__`\ \ \/ /\ \/\ \/\`'__\/'__`\ 
            \ \ \L\ \ \ \/ \ \ \_\ \ \ \L\ \ \ \_\ \ \_\ \ \ \//\  __/ 
            \ \____/\ \_\  \/`____ \ \ ,__/\ \__\\ \____/\ \_\\ \____\
                \/___/  \/_/   `/___/> \ \ \/  \/__/ \/___/  \/_/ \/____/
                                /\___/\ \_\                            
                                \/__/  \/_/                            

"""
options = r"""
            ╭───────────────────────────────────────────────────╮
            │ 1. name       {looks up a persnons name}          │
            │ 2. phone      {looks up a persons phone number}   │
            │ 3. ip         {looks up a persons ip adress}      │
            │ 4. domain     {looks up a persons ip adress}      │
            ╰───────────────────────────────────────────────────╯
"""
print(Colorate.Vertical(Colors.blue_to_white, logo))
print(Colorate.Horizontal(Colors.blue_to_white, options))
print()

pick = input(f"{Fore.GREEN}[?]{Fore.BLUE} what tool you wane use?{Fore.RESET} ")

if pick == "1":
    name_look()
elif pick == "2":
    ip = input(f"{Fore.GREEN}[?]{Fore.BLUE} input ip adress:{Fore.RESET} ").lower()
    phone()
elif pick == "3":
    ip = input(f"{Fore.GREEN}[?]{Fore.BLUE} input ip adress:{Fore.RESET} ").lower()
    ip_look()
elif pick == "4":
    domain_look()