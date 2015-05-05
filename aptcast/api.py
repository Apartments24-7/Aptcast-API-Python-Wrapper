import requests

from util import join_url


class AptcastApi(object):
    content_type = "application/json"

    def __init__(self, **kwargs):
        self.mode = kwargs.get("mode", "live")
        self.api_host = kwargs.get("api_host", self.default_api_host())
        self.api_base_path = kwargs.get("api_base_path", "/api/v1/")
        self.api_key = kwargs.get("api_key")

    def default_api_host(self):
        if self.mode == "live":
            return "https://api.aptcast.com"
        else:
            return "http://localhost:8080"

    def _set_headers(self, headers=None):
        headers = headers or {}
        headers["Content-Type"] = self.content_type
        headers["Authorization"] = self.api_key
        return headers

    def post(self, app, action, params=None, headers=None, refresh_token=None):
        headers = self._set_headers(headers)

        return requests.post(
            join_url(self.api_host, app, action), data=params or {},
            headers=headers).json()

    def put(self, app, action, params=None, headers=None, refresh_token=None):
        headers = self._set_headers(headers)

        return requests.put(
            join_url(self.api_host, app, action), data=params or {},
            headers=headers).json()

    def delete(self, app, action, params=None, headers=None,
               refresh_token=None):
        headers = self._set_headers(headers)

        return requests.delete(
            join_url(self.api_host, app, action), data=params or {},
            headers=headers).json()


class Resource(object):
    app = None

    def __init__(self, api):
        self.api = api
