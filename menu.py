from modules_parser import decrypter_module, forensics_module, extractor_module, file_module, strings_module, \
    zip_extract_module
from os import system, name
from consolemenu import *
from consolemenu.items import *
import consolemenu

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
    module('-h'.split())
    while True:
        input_txt = input('>>')
        clear()
        if input_txt == 'exit':
            exit()
        if input_txt == 'back':
            return
        if input_txt == 'clear':
            clear()
            continue
        result = module(input_txt.split())
        if result != None:
            print(result + '\n\nIn order to go back to menu , type: back')


###########################
'''
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
'''
# Create style for the menus
menuStyle = consolemenu.menu_formatter.MenuFormatBuilder()
menuStyle.set_border_style_type(5)

menu_main = ConsoleMenu(title=LOGO, formatter=menuStyle)

# Create 2 tools selection
item_decrypter = FunctionItem('Ultimate Decrypter', module_run, [decrypter_module])
item_extractor = FunctionItem('Ultimate Extractor', module_run, [extractor_module])

# Create sub-menu for forensics
menu_forensics = ConsoleMenu('Ultimate Forensics', formatter=menuStyle)
item_forensics = SubmenuItem('Ultimate Forensics', menu_forensics, menu_main)


# Add items to main menu
menu_main.append_item(item_decrypter)
menu_main.append_item(item_extractor)
menu_main.append_item(item_forensics)

# Create tools for forensics menu
item_file = FunctionItem('Detect file type', module_run, [file_module])
item_strings = FunctionItem('Find printable strings in files', module_run, [strings_module])
item_extract_zip = FunctionItem('Extract recursive zip file', module_run, [zip_extract_module])

# Add items to forensics menu
menu_forensics.append_item(item_file)
menu_forensics.append_item(item_strings)
menu_forensics.append_item(item_extract_zip)

# Show the menu
menu_main.show()
