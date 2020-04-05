from modules_parser import decrypter_module, forensics_module, extractor_module
from os import system, name

###########################

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
In order to exit , type: exit\n
'''


###########################

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def module_run(module):
    print(module('-h'.split()))
    while True:
        input_txt = input('>>')
        clear()
        if input_txt == 'exit':
            exit()
        if input_txt == 'back':
            return
        print(module(input_txt.split()) + '\n\nIn order to go back to menu , type: back')


###########################

def menu_run():
    clear()
    while True:
        print(LOGO)
        print(menu_txt)
        option = input('>>')
        if option == 'exit':
            exit()
        # menu options
        if option == '1' or option == 'Decrypter' or option == 'decrypter':
            clear()
            module_run(decrypter_module)
        elif option == '2' or option == 'Forensics' or option == 'forensics':
            clear()
            module_run(forensics_module)
        elif option == '3' or option == 'Extractor' or option == 'extractor':
            clear()
            module_run(extractor_module)


menu_run()
