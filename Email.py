from hashlib import md5
import requests
from random import choice
import time

#http://api.temp-mail.ru/request/domains/

class Email:
    '''a simple wrapper for  api.temp-mail.ru.
    I'll use this Emails in the singing in process'''


    def __init__(self, login):
        self.login = login

    def get_hash(self, intity):
        ''' get the hashes of the emails'''
        return md5(intity.encode('utf-8')).hexdigest()

    def __get_Domains(self):
        '''ge the availabe domains and choose one randomly'''

        domains = requests.get('http://api.temp-mail.ru/request/domains/format/json').json()
        return choice(domains)

    def new_email(self):

        setattr(self,'email',self.login + self.__get_Domains())
        return self.email

    def get_messages(self):
        return requests.get('http://api.temp-mail.ru/request/mail/id/{}/format/json/'
                            .format(self.get_hash(self.email))).json()



