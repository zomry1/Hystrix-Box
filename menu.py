from Decryptor import decryptor_module
from os import system, name

LOGO = """
██╗  ██╗██╗   ██╗███████╗████████╗██████╗ ██╗██╗  ██╗     ██████╗  ██████╗ ██╗  ██╗
██║  ██║╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔══██╗██║╚██╗██╔╝     ██╔══██╗██╔═══██╗╚██╗██╔╝
███████║ ╚████╔╝ ███████╗   ██║   ██████╔╝██║ ╚███╔╝█████╗██████╔╝██║   ██║ ╚███╔╝ 
██╔══██║  ╚██╔╝  ╚════██║   ██║   ██╔══██╗██║ ██╔██╗╚════╝██╔══██╗██║   ██║ ██╔██╗ 
██║  ██║   ██║   ███████║   ██║   ██║  ██║██║██╔╝ ██╗     ██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝  ╚═╝   ╚═╝   ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝     ╚═════╝  ╚═════╝ ╚═╝  ╚═╝                                                                      
"""

menu_txt = '''
Main Menu\n
  1) Decrypter\n
  2) Forensics\n
  3) Extractor\n
In order to exit , type: exit

>>
'''


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def decrypter():
    print(decryptor_module('-h'.split()))
    while True:
        input_txt = input('>>')
        clear()
        if input_txt == 'exit':
            exit()
        if input_txt == 'back':
            return
        print(decryptor_module(input_txt.split()))


def menu_run():
    clear()
    while True:
        print(LOGO)
        print(menu_txt)
        option = input()
        if option == 'exit':
            exit()
        if option == '1' or option == 'Decrypter' or option == 'decrypter':
            clear()
            decrypter()


menu_run()
