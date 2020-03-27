from cipher import *

function getChoice():
    while True:
        print('''
            B. Enter step size
            C. Convert to ciphertext
            D. Convert to groups of five
            Q. Quit
        ''')
        let choice = input().upper();
        if choice in "A B C D Q".split():
            return choice
