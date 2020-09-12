from colorama import init, Fore

init()

List = {
    'BLACK' : Fore.BLACK,
    'BLUE' : Fore.BLUE,
    'CYAN' : Fore.CYAN,
    'GREEN' : Fore.GREEN,
    'MAGENTA' : Fore.MAGENTA,
    'RED' : Fore.RED,
    'WHITE' : Fore.WHITE,
    'YELLOW' : Fore.YELLOW,
    'RESET' : Fore.RESET
}

def ctext(text , text_color='RESET', after_color='RESET'):
    return List[text_color] + text + List[after_color]