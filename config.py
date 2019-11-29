import base64

class config():
    def __init__(self):
        self.client_id = "CLIENT_ID_HERE"
        self.client_secret = "CLIENT_SECRET_HERE"
        self.token = base64.b64encode(str.encode(f"{self.client_id}:{self.client_secret}", 'utf-8')).decode('utf-8')

    def getToken(self):
        return self.token