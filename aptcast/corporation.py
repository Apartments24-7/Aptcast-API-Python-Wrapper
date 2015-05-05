import json

from api import Resource


class Corporation(Resource):
    base_action = "corp"
    app = "corporation"

    def __init__(self, api):
        self.api = api

    def create(self, name, address0, address1, city, state, postal_code,
               email, website, phone, parent):
        self.action = self.base_action
        data = {
            "name": name,
            "parent": parent,
            "contact": {
                "email": email,
                "website": website,
                "phone": phone,
                "address": {
                    "address0": address0,
                    "address1": address1,
                    "city": city,
                    "state": state,
                    "postal_code": postal_code
                }
            }
        }

        return self.api.post(
            self.get_app(), self.get_action(), params=json.dumps(data))
