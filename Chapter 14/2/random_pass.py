import string
import random
import secrets

length = 16

specialChar = random.choice(string.punctuation)
upperCase = random.choice(string.ascii_uppercase)
digit = random.choice(string.digits)

password = ""
password=password + upperCase
for i in range(13):
    password += random.choice(string.ascii_letters)

password = password + specialChar
password = password + digit
print("Random password: {}".format(password))
