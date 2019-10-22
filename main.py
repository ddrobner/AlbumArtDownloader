import requests
import json

class main(self):

    token = requests.post("https://accounts.spotify.com/api/token", 
                                headers={'Authorization': 'Basic YzRhNWI4NzhlMmI3NGNmODg1YjI4NDNhMTQyODFkYmM6YjE2YzgwZGM1M2MzNDE5NDg3ZGE3MWUxYmU0ZmEyY2E='},
                                data={'grant_type': 'client_credentials'})

    json.loads(access_token.content)['access_token']
