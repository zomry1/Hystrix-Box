import shlex
from os import system, name
from consolemenu import *
from consolemenu.items import *
import consolemenu

###########################
from HystrixBox.modules_parser import decrypter_module, extractor_module, file_module, strings_module, zip_extract_module, \
    emailAnalyzer_module

LOGO = """
██╗  ██╗██╗   ██╗███████╗████████╗██████╗ ██╗██╗  ██╗     ██████╗  ██████╗ ██╗  ██╗
██║  ██║╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔══██╗██║╚██╗██╔╝     ██╔══██╗██╔═══██╗╚██╗██╔╝
███████║ ╚████╔╝ ███████╗   ██║   ██████╔╝██║ ╚███╔╝█████╗██████╔╝██║   ██║ ╚███╔╝ 
██╔══██║  ╚██╔╝  ╚════██║   ██║   ██╔══██╗██║ ██╔██╗╚════╝██╔══██╗██║   ██║ ██╔██╗ 
██║  ██║   ██║   ███████║   ██║   ██║  ██║██║██╔╝ ██╗     ██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝  ╚═╝   ╚═╝   ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝     ╚═════╝  ╚═════╝ ╚═╝  ╚═╝                                                                      
"""


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
    # module('-h'.split())
    module(shlex.split('-h'))
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
        result = module(shlex.split(input_txt))
        if result != None:
            print(result + '\n\nIn order to go back to menu , type: back')


###########################
def main():
    # Create style for the menus
    menuStyle = consolemenu.menu_formatter.MenuFormatBuilder()
    menuStyle.set_border_style_type(5)

    menu_main = ConsoleMenu(title='Main Menu', subtitle=LOGO, formatter=menuStyle)

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
    # item_stegoLSB = FunctionItem('StegoLSB decode', module_run, [stegoLSB_module])
    item_emailAnalyzer = FunctionItem('Email analyzer', module_run, [emailAnalyzer_module])

    # Add items to forensics menu
    menu_forensics.append_item(item_file)
    menu_forensics.append_item(item_strings)
    menu_forensics.append_item(item_extract_zip)
    # menu_forensics.append_item(item_stegoLSB)
    menu_forensics.append_item(item_emailAnalyzer)

    # Show the menu
    menu_main.show()

if __name__ == "__main__":
    main()