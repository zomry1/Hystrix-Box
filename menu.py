from consolemenu import *
from consolemenu.items import *

LOGO = """
██╗  ██╗██╗   ██╗███████╗████████╗██████╗ ██╗██╗  ██╗     ██████╗  ██████╗ ██╗  ██╗
██║  ██║╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔══██╗██║╚██╗██╔╝     ██╔══██╗██╔═══██╗╚██╗██╔╝
███████║ ╚████╔╝ ███████╗   ██║   ██████╔╝██║ ╚███╔╝█████╗██████╔╝██║   ██║ ╚███╔╝ 
██╔══██║  ╚██╔╝  ╚════██║   ██║   ██╔══██╗██║ ██╔██╗╚════╝██╔══██╗██║   ██║ ██╔██╗ 
██║  ██║   ██║   ███████║   ██║   ██║  ██║██║██╔╝ ██╗     ██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝  ╚═╝   ╚═╝   ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝     ╚═════╝  ╚═════╝ ╚═╝  ╚═╝                                                                      
"""
print(LOGO)
menu = ConsoleMenu('Main Menu')

decoderMenu = ConsoleMenu('Ultimate Decrypter')
decoderFileMenu = ConsoleMenu('Ultimate Decrypter', 'Read from file')
decoderStringMenu = ConsoleMenu('Ultimate Decrypter', 'Read from string')

decoderItem = SubmenuItem('Ultimate Decrypter', decoderMenu, menu)
decoderFile = SubmenuItem('file', decoderFileMenu, decoderMenu)
decoderText = SubmenuItem('text', decoderStringMenu, decoderMenu)

ForensicsMenu = MenuItem('Ultimate Forensics')
ExtractorMenu = MenuItem('Ultimate Extractor')

menu.append_item(decoderItem)
menu.append_item(ForensicsMenu)
menu.append_item(ExtractorMenu)

decoderMenu.append_item(decoderFile)
decoderMenu.append_item(decoderText)

menu.show()