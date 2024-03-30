from encryption import Encryption

encryption = Encryption()
should_continue = True
is_logged_in = False
password_trial = 0


def ask_mode(purpose):
    """ This function accepts a value which sets the mode of the app, either quit,  encrypt, or decrypt mode"""
    if purpose == 'mode':
        return input('Please select a mode: quit, encrypt or decrypt: ').lower()
    elif purpose == 'password':
        return input('Please enter your password: ')


def authenticate(purpose, password):
    """ Accepts authentication mode either encrypt or decrypt mode
     Also accepts user input password to encrypt or decrypt based on mode """
    if purpose == 'encrypt':
        return encryption.encrypt(password)
    elif purpose == 'decrypt':
        return encryption.decrypt(password)


while should_continue:
    username = ''
    user_input = ''
    mode = ask_mode('mode')

    if mode == 'quit':
        should_continue = False
    else:
        user_input = ask_mode('password')

    feedback = ''
    if mode == 'encrypt':
        feedback = next(iter(authenticate('encrypt', user_input).keys()))

    elif mode == 'decrypt':
        feedback = authenticate('decrypt', user_input)

    print(feedback)


print('Thank you for using Zypher-ix encrypt......bye')
