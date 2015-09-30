from api import Resource


class CorporationResource(Resource):
    app = "corporation"
    base_action = "corp"

    def create(self, name, address0, address1, city, state, postal_code,
               email, website, phone):
        self.action = self.base_action
        data = {
            "name": name,
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
        return self.api.post(self.get_app(), self.get_action(), params=data)

    def update(self, aptcast_id, name, address0, address1, city, state,
               postal_code, email, website, phone):

        data = {
            "name": name,
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

        self.action = "{0}/{1}".format(self.base_action, aptcast_id)
        return self.api.put(self.get_app(), self.get_action(), params=data)
