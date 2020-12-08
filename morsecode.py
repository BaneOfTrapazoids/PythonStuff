from string import ascii_lowercase, digits
#will contain all lowercase letters and all digits
character_list = []

for letter in ascii_lowercase:
    character_list += letter

for number in digits:
    character_list += number

#adds a space so a space can be put in between each word when converting from morse to text
character_list += " "

#list of all morse code codes
morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "/"]

#two dictionaries that contain pairs of letters and their morse codes, and vice versa for the second
letter_to_morse = {}
morse_to_letter = {}

#adds all the letters and morse codes to both dictionaries
for i in range(37):
    letter_to_morse.update({f"{character_list[i]}":f"{morse_code[i]}"})
    morse_to_letter.update({f"{morse_code[i]}":f"{character_list[i]}"})


while True:
    text_to_morse = input("Text to Morse Code (true or false):")
    
    if text_to_morse == "True" or text_to_morse == "true":
        text_to_translate = input("input what you want to translate, only use letters and numbers:")
    elif text_to_morse == "False" or text_to_morse == "false":
        text_to_translate = input("input what you want to translate, separate each character with a space and each word with a /:")

    #if you want to convert text to morse, then it goes through each character in the string of what you want to translate
    #and converts it into it's morse code equivalent by geting each characters value from the letter to morse dictionary
    if text_to_morse == "True" or text_to_morse == "true":
        translated_text = ""
        for character in text_to_translate:
            translated_text += f"{letter_to_morse.get(character)} "

    #Converts the text you put in to morse with a dictionary like text to morse
    elif text_to_morse == "False" or text_to_morse == "false":
        #the text that will be printed once finished
        translated_text = ""

        #an empty list for now that will hold each separate morse code
        characters_to_translate = []

        #splits the morse code to be translated into a list of each code
        characters_to_translate = text_to_translate.split(" ")

        #takes each morse code and adds it's letter equivalent to translated text
        for character in characters_to_translate:
            translated_text += f"{morse_to_letter.get(str(character))}"
    print(translated_text)