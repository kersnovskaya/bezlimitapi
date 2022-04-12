import requests
import json

from api.configuration.config import DOMAIN_PROD


class Response:

    __headers = None
    __status_code = None
    __reason = None
    __ok = None
    __content = None

    def __init__(self, headers: dict, status_code: int, reason: str, ok: bool, content: dict):
        self.__headers = headers
        self.__status_code = status_code
        self.__reason = reason
        self.__ok = ok
        self.__content = content

    def get_headers(self):
        return self.__headers

    def get_status_code(self):
        return self.__status_code

    def get_reason(self):
        return self.__reason

    def get_ok(self):
        return self.__ok

    def get_content(self):
        return self.__content


class Request:

    def __init__(self, method: str, endpoint: str, headers={}, data={}, params={}):
        self.method = method
        self.base_url = DOMAIN_PROD
        self.endpoint = endpoint
        self.headers = headers
        self.data = data
        self.params = params

    def make_request_to_endpoint(self):
        url = self.base_url + self.endpoint

        if self.method == 'POST':
            response = requests.post(url=url, headers=self.headers, data=self.data)
        elif self.method == 'PUT':
            response = requests.put(url=url, headers=self.headers, data=self.data)
        elif self.method == 'GET':
            response = requests.get(url=url, headers=self.headers, params=self.params)

        try:
            res_headers = response.headers
            status_code = response.status_code
            reason = response.reason
            ok = response.ok
            content = json.loads(response.content.decode('utf-8'))
        except Exception:
            return ValueError

        return Response(headers=res_headers,
                        status_code=status_code,
                        reason=reason,
                        ok=ok,
                        content=content)

    def make_url(self):
        return self.base_url + self.endpoint
