# Variables
login = False
attempts = 5

# Password authenticator
while not login and attempts != 0:
    password = input()
    if password == "FLDSMDFR21":
        login = True
    else:
        attempts -= 1

# Case no more attempts
if attempts == 0:
    print("FLDSMDFR bloqueada!")

# Make it rain
if login == True:
    water_ml = int(input())
    hamburgers = int(water_ml / 3)
    i = 1
    while i <= hamburgers:
        print("* " * i)
        i += 1
