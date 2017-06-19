import requests
from urllib.parse import urljoin
from pprint import pprint
import time

class NoTokenProvided(Exception):
    pass


class droplets:
    endpoint = 'https://api.digitalocean.com/v2/droplets/'
    params = {'name': 'Tempo', 'region': "nyc3", 'size': "512mb", 'image': "centos-7-0-x64"}

    def __init__(self, token=None):
        self.token = token
        self.create_droplet()


    def __authorization(self, headers):
        if not self.token:
            raise NoTokenProvided()
        headers.update({"Content-Type": "application/json", "Authorization": "Bearer {}".format(self.token)})


    def create_droplet(self):
        self.headers = {}
        self.__authorization(self.headers)
        id = requests.post(self.endpoint,
                           headers=self.headers,
                           params=self.params).json()
        self.id = id['droplet']['id']


    def get_IP(self, id):
        ID = urljoin(self.endpoint, str(id))
        temp = requests.get(ID, headers=self.headers).json()
        return temp['droplet']['networks']['v4'][0]['ip_address']

    def destroy_droblet(self, id):
        ID = urljoin(self.endpoint, str(id))
        return requests.delete(ID,
                               headers=self.headers)
