import random, secrets, hashlib

def finRand():
    lines = open("words_alpha.txt").readlines()
    return str(lines[random.randint(0, len(lines))])

def genFromWord():
    password = ""
    for i in range(random.randint(2,4)):
        toAdd1 = finRand()
        toAdd2 = ""
        for i in range(len(toAdd1) - 2):
            toAdd2 = toAdd2 + toAdd1[i]
        toAdd1 = toAdd2
        password = password + toAdd1
    return password

s = int(input("Select Mode:\n[1] Random Words\n[2] Random Words With Number\n[3] Random String Of Characters\n"))

if s == 1:
    print(genFromWord())
if s == 2:
    print(genFromWord() + str(random.randint(1, int(input("Give range between 1 and: ")))))
if s == 3:
    print(secrets.token_hex(int(input("Input desired length: "))))
