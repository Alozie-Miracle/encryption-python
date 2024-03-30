import random
from alphabets import data


class Encryption:
    def __init__(self):
        self.password = ''
        self.location = ''
        self.encryption = {}

    def encrypt(self, user_input):
        """ Accepts a user input to encrypt password"""
        if user_input:
            for _ in range(0, 33):
                choice = random.randint(0, len(user_input))
                word = data[choice]
                self.password += word
            self.location = user_input

            self.encryption = {self.password: self.location}
            return self.encryption

    def decrypt(self, user_input):
        """ Accepts users encrypted password and returns the unencrypted version """
        info = self.encryption[user_input]
        return info

