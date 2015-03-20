import json

from api import Resource


class Community(Resource):

    app = "community"

    def create(self, name, description, lat, lng, address, city, state,
               postal_code, email, website, phone):
        data = {
            "community": {
                "description": description,
                "name": name,
                "location": {
                    "lat": lat,
                    "long": lng,
                    "address": {
                        "address0": address,
                        "city": city,
                        "state": state,
                        "postal_code": postal_code,
                    }
                },
                "contact": {
                    "email": email,
                    "website": website,
                    "phone": phone
                }
            }
        }
        return self.api.post("community", "create",
                             params=json.dumps(data))
