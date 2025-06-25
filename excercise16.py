'''
Excercise 16 off of practicepython.org

Maksym Pronin, June 25, 2025
'''
import random
def generatepassword(strength, length):
    password = ''
    lowerletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upperletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
               '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"',
               ',', '<', '.', '>', '/', '?', '`', '~']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    words = ["cloud", "butter", "tiger", "skate", "apple", "zebra", "melon", "laser", "storm", "blanket"]
    looplength = int(length / 4)
    if strength == "s":
        for i in range(looplength):
            password = password + random.choice(lowerletters)
            password = password + random.choice(upperletters)
            password = password + random.choice(symbols)
            password = password + random.choice(digits)
        leftover = length - (looplength * 4)
        all_chars = lowerletters + upperletters + symbols + digits
        for i in range(leftover):
            password = password + random.choice(all_chars)
    elif strength == "w":
        password = random.choice(words) + random.choice(words)
    return password
strength = input("Strong (s) or weak (w) password?")
if strength =="s":
    length = int(input("How many characters would you like the password?"))
    finalpass = generatepassword(strength, length)
elif strength == "w":
    length = 0
    finalpass = generatepassword(strength, length)
print(finalpass)

