import requests
import json

from auth import auth

class main():
    
    def __init__(self):
        self.AUTHENTICATION_STRING = "YzRhNWI4NzhlMmI3NGNmODg1YjI4NDNhMTQyODFkYmM6YjE2YzgwZGM1M2MzNDE5NDg3ZGE3MWUxYmU0ZmEyY2E="
        self.authenticator = auth(AUTHENTICATION_STRING)
        self.access_token = authenticator.authenticate() 
