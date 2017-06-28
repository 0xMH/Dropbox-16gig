from hashlib import md5
import requests
import string
from random import choice


class Emails:
    '''a simple wrapper for  api.temp-mail.ru.
    I'll use this Emails in the singing in process'''


    def __init__(self, login=None):
        if login:
            self.login = login
        else:
            self.login = self.__name_gen()

    def get_hash(self, intity):
        """get the hashes of the emails"""
        return md5(intity.encode('utf-8')).hexdigest()

    def __get_domains(self):
        """ge the availabe domains and choose one randomly"""

        domains = requests.get('http://api.temp-mail.ru/request/domains/format/json').json()
        return choice(domains)

    def new_email(self):
        """make a new Email"""

        setattr(self,'email',self.login + self.__get_domains())
        return self.email

    def get_messages(self):
        """get the mail box"""

        return requests.get('http://api.temp-mail.ru/request/mail/id/{}/format/json/'
                            .format(self.get_hash(self.email))).json()

    def __password_gen(self):
        pass

    def __name_gen(self):
        """generate random names for Emails"""

        chars = string.ascii_letters + string.digits
        return ''.join(choice(chars) for _ in range(8))

