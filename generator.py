import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string
    
def generate_random_email():
    return f"{generate_random_string(6)}@yandex.ru"