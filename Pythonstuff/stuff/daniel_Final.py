#Daniel Kolodziej
#ITMD 413 final
#pass gen
import random


totalOptions="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()"
letters="abcdefghijklmnopqrstuvwxyz"
lettersUP="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="~!@#$%^&*()"
password1=""
length1 = random.randint(8,10)
length2 = random.randint(8,10)
length3 = random.randint(8,10)
length4 = random.randint(8,10)
for val in range(length1):
    password1 += random.choice(letters)
for val in range(length2):
    password1 += random.choice(lettersUP)
for val in range(length3):
    password1 += random.choice(numbers)
for val in range(length4):
    password1 += random.choice(symbols)
print("lower/Upper/nums/syms options:   " + password1)

scramble =""
scrambled=""
scramble = password1
passLen = len(scramble)
for val in range(passLen):
    scrambled += random.choice(scramble)
print("new pass:   " + scrambled)





