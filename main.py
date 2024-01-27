morse_code_dict = {
    # Letters
    'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".", 'F': "..-.",
    'G': "--.", 'H': "....", 'I': "..", 'J': ".---", 'K': "-.-", 'L': ".-..",
    'M': "--", 'N': "-.", 'O': "---", 'P': ".--.", 'Q': "--.-", 'R': ".-.",
    'S': "...", 'T': "-", 'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-",
    'Y': "-.--", 'Z': "--..",

    # Numbers
    '0': "-----", '1': ".----", '2': "..---", '3': "...--", '4': "....-",
    '5': ".....", '6': "-....", '7': "--...", '8': "---..", '9': "----.",

    # Space
    ' ': "/"
}

text = input("Original Text:\n ")
morse_code = ""

for char in text:
    if char.upper() in morse_code_dict:
        letter_to_morse = morse_code_dict.get(char.upper())
        morse_code += letter_to_morse + " "
    else:
        morse_code += char
print(f"Morse Code:\n {morse_code}")


