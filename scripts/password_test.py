import random

def password_check(password):
    
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    
    return True
    
def random_password():
    password = ''
    for i in range(random.randint(7,11)):
        password += chr(random.randint(33,126))
    return password

if __name__ == '__main__':
    
    attempts = 0
    while(True):
        password = random_password()
        print('Your generated password is: ',password)
        attempts += 1
    
        if password_check(password):
            print('Password is good: ', password)
            print('Attempts taken: ', attempts)
            break
