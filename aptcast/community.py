import requests

from api import Resource
from io import BytesIO


class CommunityResource(Resource):
    app = "community"
    base_action = "communities"

    def build_address(self, address0, city, state, postal_code, address1=""):
        address = {
            "address0": address0,
            "city": city,
            "state": state,
            "postal_code": postal_code
        }
        if address1:
            address["address1"] = address1
        return address

    def build_contact(self, phone, email="", website="", **kwargs):
        contact = {
            "phone": phone,
            "address": self.build_address(**kwargs)
        }
        if email:
            contact["email"] = email
        if website:
            contact["website"] = website
        return contact

    def build_community(self, name, lat, lng, phone, address0, city, state,
                        postal_code, description="", address1="", email="",
                        website="", **kwargs):
        """
        Create Aptcast Community Dict

        Required arguments include:
            name: <string>,
            lat: <float>,
            lng: <float>,
            phone: <string>,
            address0: <string>,
            city: <string>,
            state: <string>,
            postal_code: <string|integer>
        Optional arguments include:
            description: <string>,
            address1: <string>,
            email: <string>,
            website: <string>,
            pet_policy_details: <string>,
            dogs: <boolean>,
            cats: <boolean>,
            senior: <boolean>,
            section8: <boolean>,
            student: <boolean>,
            corporate: <boolean>,
            military: <boolean>
        """
        data = {
            "name": name,
            "location": {
                "lat": lat,
                "lng": lng
            },
            "contact": self.build_contact(
                phone, email, website, address0=address0, address1=address1,
                city=city, state=state, postal_code=postal_code
            )
        }

        if description == "":
            description = None
        data["description"] = description

        for key, value in kwargs.items():
            data[key] = value

        return data

    def create(self, *args, **kwargs):
        self.action = self.base_action
        data = self.build_community(*args, **kwargs)
        return self.api.post(
            self.get_app(), self.get_action(), params=data)

    def update(self, aptcast_id, *args, **kwargs):
        self.action = "{0}/{1}".format(self.base_action, aptcast_id)
        data = self.build_community(*args, **kwargs)
        return self.api.put(self.get_app(), self.get_action(), params=data)

    def delete(self, aptcast_id):
        self.action = "{0}/{1}".format(self.base_action, aptcast_id)
        return self.api.delete(self.get_app(), self.get_action())


class CommunityAmenityResource(Resource):
    app = "community"
    base_action = "amenities"

    def create(self, community_aptcast_id, name, order, base):
        self.action = self.base_action
        data = {
            "name": name or None,
            "order": order,
            "base": base,
            "community": community_aptcast_id
        }

        return self.api.post(self.get_app(), self.get_action(), params=data)

    def update(self, aptcast_id, **kwargs):
        self.action = "{0}/{1}".format(self.base_action, aptcast_id)
        return self.api.patch(self.get_app(), self.get_action(), params=kwargs)

    def delete(self, aptcast_id):
        self.action = "{0}/{1}".format(self.base_action, aptcast_id)
        return self.api.delete(self.get_app(), self.get_action())


class FloorPlanResource(Resource):
    app = "community"
    base_action = "floor-plan"

    def build_low_high(self, low, high=None):
        return {
            "low": low,
            "high": high
        }

    def build_floor_plan(self, beds, baths, name, rent_low, deposit_low,
                         square_feet_low, is_loft=False, is_studio=False,
                         rent_high=None, deposit_high=None,
                         square_feet_high=None, description=None):
        data = {
            "name": name,
            "beds": beds,
            "baths": baths,
            "rent": self.build_low_high(rent_low, rent_high),
            "deposit": self.build_low_high(deposit_low, deposit_high),
            "square_feet": self.build_low_high(
                square_feet_low,
                square_feet_high
            ),
            "is_loft": is_loft,
            "is_studio": is_studio
        }

        if description == "":
            description = None
        data["description"] = description

        return data

    def create(self, community_aptcast_id, *args, **kwargs):
        self.action = "{0}/{1}".format(community_aptcast_id, self.base_action)

        data = self.build_floor_plan(*args, **kwargs)

        return self.api.post(
            self.get_app(), self.get_action(), params=data)

    def update(self, community_aptcast_id, aptcast_id, *args, **kwargs):
        self.action = "{0}/{1}/{2}".format(
            community_aptcast_id, self.base_action, aptcast_id)

        data = self.build_floor_plan(*args, **kwargs)

        return self.api.put(
            self.get_app(), self.get_action(), params=data)

    def delete(self, community_aptcast_id, aptcast_id):
        self.action = "{0}/{1}/{2}".format(
            community_aptcast_id, self.base_action, aptcast_id)

        return self.api.delete(self.get_app(), self.get_action())


class FloorPlanImageResource(Resource):
    app = "community"
    base_action = "floor-plan"

    def create(self, floorplan_aptcast_id, image_url, width=None, height=None):
        self.action = "{0}/{1}".format(self.base_action, floorplan_aptcast_id)
        if image_url:
            response = requests.get(image_url, timeout=10)
            files = {
                "image": (
                    image_url.split("/")[-1],
                    BytesIO(response.content),
                    response.headers.get("content-type", "")
                )
            }
        else:
            return {}

        return self.api.post_multipart(self.app, "{0}/image".format(
            self.action), files=files)

    def delete(self, floorplan_aptcast_id):
        self.action = "{0}/{1}".format(self.base_action, floorplan_aptcast_id)

        return self.api.delete(
            self.app, "{0}/image".format(self.action))


class UnitResource(Resource):
    app = "community"
    base_action = "units"

    def build_low_high(self, low, high=None):
        return {
            "low": low,
            "high": high
        }

    def build_unit(self, rent_low, deposit_low, square_feet_low,
                   rent_high=None, deposit_high=None, square_feet_high=None,
                   number="", building="", floor="", available_date=None,
                   description=None):
        data = {
            "number": number,
            "building": building,
            "floor": floor,
            "available_date": available_date,
            "rent": self.build_low_high(rent_low, rent_high),
            "deposit": self.build_low_high(deposit_low, deposit_high),
            "square_feet": self.build_low_high(
                square_feet_low,
                square_feet_high
            ),
        }

        if description == "":
            description = None
        data["description"] = description

        return data

    def create(self, floor_plan_aptcast_id, *args, **kwargs):
        self.action = "{0}/{1}".format(floor_plan_aptcast_id, self.base_action)

        data = self.build_unit(*args, **kwargs)

        return self.api.post(self.get_app(), self.get_action(), params=data)

    def update(self, floor_plan_aptcast_id, unit_aptcast_id, *args, **kwargs):
        self.action = "{0}/{1}/{2}".format(
            floor_plan_aptcast_id, self.base_action, unit_aptcast_id)

        data = self.build_unit(*args, **kwargs)

        return self.api.put(self.get_app(), self.get_action(), params=data)

    def delete(self, floor_plan_aptcast_id, aptcast_id):
        self.action = "{0}/{1}/{2}".format(
            floor_plan_aptcast_id, self.base_action, aptcast_id)

        return self.api.delete(self.get_app(), self.get_action())


class HeroShotResource(Resource):
    app = "community"

    def create(self, community_id, image_url, width=None, height=None):

        if image_url:
            response = requests.get(image_url, timeout=10)
            files = {
                "image": (
                    image_url.split("/")[-1],
                    BytesIO(response.content),
                    response.headers.get("content-type", "")
                )
            }
        else:
            return {}

        return self.api.post_multipart(
            self.app, "{0}/hero-shot".format(
                community_id), files=files)

    def delete(self, community_id):
        return self.api.delete(
            self.app, "{0}/hero-shot".format(community_id))


class LogoImageResource(Resource):
    app = "community"

    def create(self, community_id, image_url, width=None, height=None):

        if image_url:
            response = requests.get(image_url, timeout=10)
            files = {
                "image": (
                    image_url.split("/")[-1],
                    BytesIO(response.content),
                    response.headers.get("content-type", "")
                )
            }
        else:
            return {}

        return self.api.post_multipart(self.app, "{0}/logo".format(
            community_id), files=files)

    def delete(self, community_id):
        return self.api.delete(
            self.app, "{0}/logo".format(community_id))


class SlideshowResource(Resource):
    app = "community"
    base_action = "slideshow"

    def create(self, community_aptcast_id, name):
        self.action = "{0}/{1}".format(community_aptcast_id, self.base_action)
        data = {"name": name}

        return self.api.post(self.get_app(), self.get_action(), params=data)

    def update(self, community_aptcast_id, aptcast_id, **kwargs):
        self.action = "{0}/{1}/{2}".format(
            community_aptcast_id, self.base_action, aptcast_id)

        return self.api.patch(
            self.get_app(), self.get_action(), params=kwargs)

    def delete(self, community_aptcast_id, aptcast_id):
        self.action = "{0}/{1}/{2}".format(
            community_aptcast_id, self.base_action, aptcast_id)

        return self.api.delete(self.get_app(), self.get_action())


class SlideshowImageResource(Resource):
    app = "community"
    base_action = "slideshow"
    extra_action = "images"

    def create(self, slideshow_aptcast_id, name, description, image_url):
        self.action = "{0}/{1}/{2}".format(
            self.base_action, slideshow_aptcast_id, self.extra_action)

        data = {
            "name": name or None,
            "description": description or None
        }

        response = requests.get(image_url, timeout=10)

        files = {
            "image": (
                image_url.split("/")[-1],
                BytesIO(response.content),
                response.headers.get("content-type", "")
            )
        }

        return self.api.post_multipart(
            self.get_app(), self.get_action(), params=data, files=files)

    def update(self, slideshow_aptcast_id, aptcast_id, **kwargs):
        self.action = "{0}/{1}/{2}/{3}".format(
            self.base_action, slideshow_aptcast_id, self.extra_action,
            aptcast_id)

        files = {}
        if kwargs.get("image"):
            files.update({"image": kwargs.pop("image")})

        return self.api.patch(
            self.get_app(), self.get_action(), params=kwargs, files=files)

    def delete(self, slideshow_aptcast_id, aptcast_id):
        self.action = "{0}/{1}/{2}/{3}".format(
            self.base_action, slideshow_aptcast_id, self.extra_action,
            aptcast_id)

        return self.api.delete(self.get_app(), self.get_action())
