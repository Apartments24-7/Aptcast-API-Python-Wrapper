import requests

from util import join_url


class AptcastApi(object):
    content_type = "application/json"

    def __init__(self, **kwargs):
        self.mode = kwargs.get("mode", "live")
        self.api_host = kwargs.get("api_host", self.default_api_host())
        self.api_key = kwargs.get("api_key")

    def default_api_host(self):
        if self.mode == "live":
            return "https://api.aptcast.com"
        else:
            return "http://localhost:3000"

    def post(self, app, action, params=None, headers=None, refresh_token=None):
        headers = headers or {}
        headers["Content-Type"] = self.content_type
        headers["Authorization"] = self.api_key
        return requests.post(
            join_url(self.api_host, app, action), data=params or {},
            headers=headers).json()

    def put(self, app, action, params=None, headers=None, refresh_token=None):
        headers = headers or {}
        headers["Content-Type"] = self.content_type
        headers["Authorization"] = self.api_key

        return requests.put(
            join_url(self.api_host, app, action), data=params or {},
            headers=headers).json()


class Resource(object):
    app = None

    def __init__(self, api):
        self.api = api
