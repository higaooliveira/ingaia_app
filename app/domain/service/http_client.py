import requests


class HttpClient:
    def __init__(self, headers=None):
        self.session = requests.Session()
        self.base_url = ""
        self.__set_hooks(headers)

    def __set_hooks(self, headers):
        self.session.hooks['response'] = self.check_error
        self.session.headers = {'Content-Type': 'application/json', 'Accept': '*/*'}

        if headers:
            self.session.headers.update(headers)

    def set_base_url(self, base_url):
        self.base_url = base_url

    @staticmethod
    def check_error(response, *args, **kwargs):
        response.raise_for_status()

    def get(self, endpoint, **kwargs):
        url = f'{self.base_url}{endpoint}'
        response = self.session.get(url, **kwargs)

        return response.json()
