import base64

class config():
    def __init__(self):
        self.directory = "/home/david/test"
        self.client_id = "c4a5b878e2b74cf885b2843a14281dbc"
        self.client_secret = "b16c80dc53c3419487da71e1be4fa2ca"
        self.token = base64.b64encode(str.encode(f"{self.client_id}:{self.client_secret}", 'utf-8')).decode('utf-8')

    def getDirectory(self):
        return self.directory

    def getToken(self):
        return self.token