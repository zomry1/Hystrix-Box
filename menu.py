from main import app_starter
from os import system, name

LOGO = """
██╗  ██╗██╗   ██╗███████╗████████╗██████╗ ██╗██╗  ██╗     ██████╗  ██████╗ ██╗  ██╗
██║  ██║╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔══██╗██║╚██╗██╔╝     ██╔══██╗██╔═══██╗╚██╗██╔╝
███████║ ╚████╔╝ ███████╗   ██║   ██████╔╝██║ ╚███╔╝█████╗██████╔╝██║   ██║ ╚███╔╝ 
██╔══██║  ╚██╔╝  ╚════██║   ██║   ██╔══██╗██║ ██╔██╗╚════╝██╔══██╗██║   ██║ ██╔██╗ 
██║  ██║   ██║   ███████║   ██║   ██║  ██║██║██╔╝ ██╗     ██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝  ╚═╝   ╚═╝   ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝     ╚═════╝  ╚═════╝ ╚═╝  ╚═╝                                                                      
"""


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def decrypter():
    print(app_starter('-h'.split()))
    while True:
        inputText = input('>>')
        clear()
        if inputText == 'exit':
            return
        print(app_starter(inputText.split()))

clear()
while True:
    print(LOGO)
    print('type exit to exit')
    option = input('Main Menu\n1) Decrypter\n2) Forencisc\n3) Extractor\n>>')
    if option == 'exit':
        exit()
    if option == '1' or option == 'Decrypter' or option == 'decrypter':
        clear()
        decrypter()
