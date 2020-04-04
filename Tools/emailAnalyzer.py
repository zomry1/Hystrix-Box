import email
#from email.parser import HeaderParser
# https://github.com/SpamScope/mail-parser/blob/develop/mailparser/mailparser.py

wantedFields = ['Subject', 'Date', 'From', 'To', 'Message-ID', 'List-Unsubscribe', 'Return-Path', 'Content-Type', 'Received']

with open('emailCheck/Netflix.eml') as file:
    msg = email.message_from_file(file)


    #parser = HeaderParser()
    #msgparser = parser.parse(msg)
    for field in wantedFields:
        for value in (msg.get_all(field) or []):
            print(field + ": " + value)