import json

from api import Resource


class Corporation(Resource):
    app = "corporation"

    def __init__(self, api):
        self.api = api

    def create(self, name, email, website, phone, address, city, state,
               postal_code):

        data = {
            "corporation": {
                "name": name,
                "contact": {
                    "email": email,
                    "website": website,
                    "phone": phone
                },
                "address": {
                    "address0": address,
                    "city": city,
                    "state": state,
                    "postal_code": postal_code
                }
            }
        }

        return self.api.post("corporation", "create", params=json.dumps(data))
