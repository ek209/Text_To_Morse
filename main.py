#This code translates English strings into morse code.

#Dictionary for morse code translations
#Codes end with space to account for singular 
#space needed after letters
morse_dict = {'a' : '.- ', 'b' : '-... ', 'c' : '-.-. ',
              'd' : '-.. ', 'e' : '. ', 'f' : '..-. ',
              'g' : '--. ', 'h' : '.... ', 'i' : '.. ',
              'j' : '.--- ', 'k' : '-.- ', 'l' : '.-.. ',
              'm' : '-- ', 'n' : '-. ', 'o' : '--- ', 
              'p' : '.--. ', 'q' : '--.- ', 'r' : '.-. ',
              's' : '...', 't' : '- ', 'u' : '..- ',
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
original_text = str(input('Enter the text you want translated to morse: ').lower())
morse_table = str.maketrans(morse_dict)

print(original_text.translate(morse_table))