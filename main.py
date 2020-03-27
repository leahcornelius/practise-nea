from cipher import *

def getChoice():
    while True:
        print('''
            B. Enter step size
            C. Convert to ciphertext
            D. Convert to groups of five
            Q. Quit
        ''')
        choice = input().upper();
        if choice in "A B C D Q".split():
            return choice
        else:
            print("That is not a valid input, please try again")
        
def getPlaintext():
    print("Please enter the text you wish to encode")
    return input.strip()

def getCiphertext():
    print("Please enter the text you wish to decode")
    return input.strip()

def getStep():
    while True:
        print("Please enter the amount of steps to encode with")
        in = int(input)
        if in < 1 or in > 25:
            print(in + " is out of range: 1-25. Please enter a diffrent number")
        else:
            return in

def quit():
    print("Goodbye")
    raise SystemExit

def toGroupsOfFive(text):
    res = ""
    for i < len(text):
        if i % 5 == 0: # This tells us if we are at a multiple of five
            res = res + " "
        else:
            res = res + test[i]
    return res

def main():
    while True:
        print("Welcome to SUCOCI - The SUper-COol-CIeser-cipher")
        mode = getChoice()
        if mode == "Q":
            quit()
        else if mode == "A":
            plaintext = getPlaintext()
            step = getStep()
            encrypted = toGroupsOfFive(encrypt(plaintext, step))
            print("Ciphertext for plaintext:" + plaintext + " with step: " + step + " is: " + encrypted)
        
