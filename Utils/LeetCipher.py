def leet_translator(text):
    leet_dict = {"8": "ate",
                 'm8': 'mate',
                 'tht': "that",
                 'j00': "you",
                 '0': 'o',
                 '1': 'i',
                 '3': 'e',
                 '5': 's',
                 '4': 'a',
                 '7': 't', }
    temp_str = text
    for replaced_char in temp_str:
        if replaced_char in leet_dict:
            temp_str = temp_str.replace(replaced_char, leet_dict[replaced_char])
    return temp_str.lower()

# message = input("Please enter a message: ")
# print("Translated Message: ", leet_translator(message))
