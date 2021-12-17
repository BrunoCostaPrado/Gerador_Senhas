import string
import random
ay = 0
password = ""
for ay in range(15):
    i = random.choice(string.ascii_lowercase)
    password += i
for ay in range(10):
    o = random.choice(string.digits)
    password += o
for ay in range(4):
    u = random.choice(string.ascii_lowercase)
    password += u
print(password)