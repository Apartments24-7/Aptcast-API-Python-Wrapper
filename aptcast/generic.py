import json

from api import Resource


class GenericResource(Resource):
    app = "generic"


class BaseAmenityResource(GenericResource):
    base_action = "base-amenities"

    def create(self, name):
        self.action = self.base_action
        data = {"name": name}

        return self.api.post(
            self.get_app(), self.get_action(), params=json.dumps(data))

    def update(self, amenity_id, name):
        self.action = "{0}/{1}".format(self.base_action, amenity_id)
        data = {"id": amenity_id, "name": name}

        return self.api.put(
            self.get_app(), self.get_action(), params=json.dumps(data))

    def delete(self, amenity_id):
        self.action = "{0}/{1}".format(self.base_action, amenity_id)
        data = {"id": amenity_id}

        return self.api.delete(
            self.get_app(), self.get_action(), params=json.dumps(data))
