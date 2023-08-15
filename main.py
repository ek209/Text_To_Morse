#This code translates English strings into morse code.

#Dictionary for morse code translations
#Codes end with space to account for singular 
#Space needed after letters too account for character spacing in morse code
morse_dict = {'a' : '.- ', 'b' : '-... ', 'c' : '-.-. ',
              'd' : '-.. ', 'e' : '. ', 'f' : '..-. ',
              'g' : '--. ', 'h' : '.... ', 'i' : '.. ',
              'j' : '.--- ', 'k' : '-.- ', 'l' : '.-.. ',
              'm' : '-- ', 'n' : '-. ', 'o' : '--- ', 
              'p' : '.--. ', 'q' : '--.- ', 'r' : '.-. ',
              's' : '... ', 't' : '- ', 'u' : '..- ',
              'v' : '...- ', 'w' : '.-- ', 'x' : '-..- ',
              'y' : '-.-- ', 'z' : '--.. ', '0' : '----- ',
              '1' : '.---- ', '2' : '..--- ', '3' : '...-- ',
              '4' : '....- ', '5' : '..... ', '6' : '-.... ',
              '7' : '--... ', '8' : '---.. ', '9' : '----. ',
              '.' : '-.-.-. ', ',' : '--..-- ', '?' : '..--.. ',
              "'" : '.----. ', '!' : '-.-.--', '/' : '-..-. ',
              '(' : '-.--. ', ')' : '-.--.- ', '&' : '.-... ',
              ':' : '---... ', ';' : '-.-.-. ', '=' : '-...- ',
              '+' : '.-.-. ', '-' : '-....- ', '_' : '..--.- ',
              '"' : '.-..-. ', '$' : '...-..- ', '@' : '.--.-. ',
              ' ' : '/ '}

#reverses morse_dict and creates a new reverse_morse_dict sorted by
#key length in order to translate
reverse_morse_list = [[value, key] for key, value in morse_dict.items()]
reverse_morse_list.sort(reverse=True, key = lambda x: len(x[0]))
reverse_morse_dict = { kv_pair[0] : kv_pair[1] for kv_pair in reverse_morse_list}

original_text = str(input('Enter the text you want translated to morse: ').lower())
morse_table = str.maketrans(morse_dict)

translated = original_text.translate(morse_table)
retranslated = translated
for key, value in reverse_morse_dict.items():
    retranslated = retranslated.replace(key, value)
print(translated)
print(retranslated)
