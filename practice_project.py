import random
from string import punctuation, ascii_uppercase, ascii_lowercase, digits

def generator(length = 10):
    string =  punctuation + ascii_uppercase + ascii_lowercase + digits
    
    password = ''.join(random.choice(string) for _ in range(length))
    return password

p = generator(20)
print(f"Here is your new password: {p}")