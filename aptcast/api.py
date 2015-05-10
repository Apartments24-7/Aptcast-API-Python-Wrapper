import json

import requests

from util import join_url


class AptcastApi(object):
    def __init__(self, **kwargs):
        self.mode = kwargs.get("mode", "live")
        self.api_host = kwargs.get("api_host", self.default_api_host())
        self.api_base_path = kwargs.get("api_base_path", "/api/v1/")
        self.api_key = kwargs.get("api_key")
        self.corporation_id = None

    def default_api_host(self):
        if self.mode == "live":
            return "https://api.aptcast.com"
        else:
            return "http://localhost:8080"

    def _set_headers(self, headers=None, files=None):
        headers = headers or {}
        headers["Authorization"] = self.api_key

        if self.corporation_id is not None:
            headers["X-Corporation-Id"] = self.corporation_id

        return headers

    def set_corporation_id_header(self, corporation_id):
        """
        Main purpose is to set this id when using the super duper
        API key to act on behalf of a corporation.
        """
        self.corporation_id = corporation_id

    def post(self, app, action, params=None, files=None, headers=None,
             refresh_token=None):
        headers = self._set_headers(headers, files)
        headers["Content-Type"] = "application/json"

        response = requests.post(
            join_url(self.api_host, self.api_base_path, app, action),
            data=json.dumps(params) or {}, files=files or {},
            headers=headers)

        return response.json()

    def post_multipart(self, app, action, params=None, files=None,
                       headers=None, refresh_token=None):
        headers = self._set_headers(headers, files)

        response = requests.post(
            join_url(self.api_host, self.api_base_path, app, action),
            data=params or {}, files=files or {},
            headers=headers)
        return response.json()

    def put(self, app, action, params=None, headers=None, refresh_token=None):
        headers = self._set_headers(headers)

        return requests.put(join_url(
            self.api_host, self.api_base_path, app,
            action), data=params or {}, headers=headers).json()

    def patch(self, app, action, params=None, files=None, headers=None,
              refresh_token=None):
        headers = self._set_headers(headers)

        return requests.patch(join_url(
            self.api_host, self.api_base_path, app,
            action), data=params or {}, files=files or {},
            headers=headers).json()

    def delete(self, app, action, params=None, headers=None,
               refresh_token=None):
        headers = self._set_headers(headers)

        response = requests.delete(join_url(
            self.api_host, self.api_base_path, app,
            action), data=params or {}, headers=headers)

        return json.dumps({"status_code": response.status_code})


class Resource(object):
    app = None
    action = None

    def __init__(self, api):
        self.api = api

    def get_app(self):
        if self.app is None:
            raise AttributeError(
                '{0} is missing the "app" property. Define {0}.app.'.format(
                    self.__class__.__name__))

        return self.app

    def get_action(self):
        if self.action is None:
            raise AttributeError(
                '{0} is missing the "action" property. '
                'Define {0}.action.'.format(self.__class__.__name__))

        return self.action
