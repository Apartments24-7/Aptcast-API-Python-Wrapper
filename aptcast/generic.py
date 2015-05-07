from api import Resource


class BaseAmenityResource(Resource):
    app = "generic"
    base_action = "base-amenities"

    def create(self, name):
        self.action = self.base_action
        data = {"name": name}

        return self.api.post(self.get_app(), self.get_action(), params=data)

    def update(self, aptcast_id, name):
        self.action = "{0}/{1}".format(self.base_action, aptcast_id)
        data = {"id": aptcast_id, "name": name}

        return self.api.put(self.get_app(), self.get_action(), params=data)

    def delete(self, aptcast_id):
        self.action = "{0}/{1}".format(self.base_action, aptcast_id)
        data = {"id": aptcast_id}

        return self.api.delete(self.get_app(), self.get_action(), params=data)
