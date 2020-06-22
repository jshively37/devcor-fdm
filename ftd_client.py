import requests

from bravado.client import SwaggerClient
from bravado.requests_client import RequestsClient


class FTDClient:

    def __init__(self,
                 address='10.10.20.65',
                 port=443,
                 username="admin",
                 password="Cisco1234",
                 verify=False):
        self.server_address = address
        self.server_port = port
        self.username = username
        self.password = password
        self.verify = verify
        self.access_token = None
        self.bravado_client = None
        self.headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }

        if self.verify is False:
            requests.packages.urllib3.disable_warnings()

    def login(self):
        payload = {
            "grant_type": "password",
            "username": self.username,
            "password": self.password
        }

        print(f'Authentication Headers: {self.headers}')
        print(f'Authentication Payload: {payload}')
        r = requests.post(
            f"https://{self.server_address}:{self.server_port}/api/fdm/v5/fdm/token",
            json=payload,
            verify=self.verify,
            headers=self.headers)

        if r.status_code == 400:
            raise Exception(f"Error logging in: {r.content}")
        try:
            self.access_token = r.json()['access_token']
        except Exception as e:
            raise e

    def logout(self):
        logout_payload = {
            'grant_type': 'revoke_token',
            'access_token': self.access_token,
            'token_to_revoke': self.access_token
            }
        requests.post(
            f"https://{self.server_address}:{self.server_port}/api/fdm/v1/fdm/token",
            json=logout_payload,
            verify=self.verify,
            headers=self.headers
            )

        self.access_token = None

    def get_client(self):
        if self.bravado_client:
            return self.bravado_client

        http_client = RequestsClient()
        http_client.session.verify = False

        self.headers['Authorization'] = f"Bearer {self.access_token}"
        http_client.session.headers = self.headers

        self.bravado_client = SwaggerClient.from_url(
            f'https://{self.server_address}:{self.server_port}/apispec/ngfw.json',
            http_client=http_client,
            config={'validate_responses': False}
            )
        return self.bravado_client
