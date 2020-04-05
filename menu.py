
from main import app_starter

LOGO = """
██╗  ██╗██╗   ██╗███████╗████████╗██████╗ ██╗██╗  ██╗     ██████╗  ██████╗ ██╗  ██╗
██║  ██║╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔══██╗██║╚██╗██╔╝     ██╔══██╗██╔═══██╗╚██╗██╔╝
███████║ ╚████╔╝ ███████╗   ██║   ██████╔╝██║ ╚███╔╝█████╗██████╔╝██║   ██║ ╚███╔╝ 
██╔══██║  ╚██╔╝  ╚════██║   ██║   ██╔══██╗██║ ██╔██╗╚════╝██╔══██╗██║   ██║ ██╔██╗ 
██║  ██║   ██║   ███████║   ██║   ██║  ██║██║██╔╝ ██╗     ██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝  ╚═╝   ╚═╝   ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝     ╚═════╝  ╚═════╝ ╚═╝  ╚═╝                                                                      
"""


def decrypter():
    print(app_starter('-h'.split()))
    inputText = ''
    while inputText != 'exit':
        inputText = input('>>')
        print(app_starter(inputText.split()))


option = ''
print(LOGO)
print('input exit to exit')
while option != 'exit':
    option = input('Main Menu\n1) Decrypter\n2) Forencisc\n3) Extractor\n>>')
    if option == '1' or option == 'Decrypter' or option == 'decrypter':
        decrypter()


