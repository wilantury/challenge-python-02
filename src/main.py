# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
min_size = 8
max_size = 16
char_start = 33
char_end = 126

def getChar(type_char):
    if type_char == 0:
        return string.ascii_lowercase[random.randint(0, len(string.ascii_lowercase)-1)]
    elif type_char == 1:
        return string.ascii_uppercase[random.randint(0, len(string.ascii_uppercase)-1)]
    elif type_char == 2:
        return chr(random.randint(48,57))
    elif type_char == 3:
        return string.punctuation[random.randint(0, len(string.punctuation)-1)]    


def generate_password():
    # Start coding here
    size_password = random.randint(min_size,max_size)
    password = []
    options = random.randint(0,3)
    for idx in range(0,size_password):
        password.insert(0, getChar(options))
        options += 1
        if(options > 3):
            options = 0
    print(password)
    secure_password = ''.join(password)
    return secure_password



def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
