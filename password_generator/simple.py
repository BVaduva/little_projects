import string
import random

pw_len = 14
pw_done = ""

for sign in range(pw_len):
    pw_done += random.choice(string.printable)
    #decider = random.randint(1, 3)
    #if decider == 1:  
        #pw_done += random.choice(string.ascii_letters)
    #elif decider == 2:
        #pw_done += random.choice(string.digits)
    #elif decider == 3:
        #pw_done += random.choice(string.punctuation)
print(pw_done)