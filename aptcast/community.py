import json
import requests

from api import Resource
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO

class CommunityResource(Resource):
    app = "community"
    base_action = "communities"

    def create(self, name, lat, lng, address0, address1, city, state, postal_code, email,
               website, phone, pet_policy_details, dogs, cats, senior,
               section8, student, corporate, military, corporation,
               description, location, logo_description, hero_shot_description,
               logo, hero_shot):
        self.action = self.base_action

        data = {
            "description": {"body": description},
            "name": name,
            "location": {
                "lat": lat,
                "lng": lng
            },
            "contact": {
                "email": email,
                "website": website,
                "phone": phone,
                "address": {
                    "address0": address0,
                    "address1": address1,
                    "city": city,
                    "state": state,
                    "postal_code": postal_code,
                }
            },
            "pet_policy": {
                "cats": cats,
                "dogs": dogs,
                "details": pet_policy_details or ""
            }
        }

        files = {}
        if any([logo, hero_shot]):
            if logo:
                files.update({"logo": logo})
            if hero_shot:
                files.update({"hero_shot": hero_shot})

        return self.api.post(
            self.get_app(), self.get_action(), params=data, files=files)

    def update(self, aptcast_id, name, description, lat, lng, address, city,
               state, postal_code, email, website, phone, cats, dogs,
               pet_policy):
        data = {
            "community_id": aptcast_id,
            "description": {"body": description},
            "name": name,
            "location": {
                "lat": lat,
                "lng": lng
            },
            "contact": {
                "email": email,
                "website": website,
                "phone": phone,
                "address": {
                    "address0": address,
                    "city": city,
                    "state": state,
                    "postal_code": postal_code,
                }
            },
            "pet_policy": {
                "cats": cats,
                "dogs": dogs,
                "details": pet_policy or ""
            }
        }

        return self.api.put(self.app, "update", params=json.dumps(data))


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
    base_action = "floor-plans"

    def create(self, community_aptcast_id, beds, baths, name, is_loft,
               is_studio, description, image, image_description, rent_low,
               rent_high, deposit_low, deposit_high, square_feet_low,
               square_feet_high):
        self.action = "{0}/{1}".format(community_aptcast_id, self.base_action)

        description_dict = None
        if description:
            description_dict = {
                "body": description
            }

        data = {
            "name": name,
            "beds": beds,
            "baths": baths,
            "description": description_dict,
            "rent": {
                "low": rent_low,
                "high": rent_high
            },
            "deposit": {
                "low": deposit_low,
                "high": deposit_high
            },
            "square_feet": {
                "low": square_feet_low,
                "high": square_feet_high
            },
            "is_loft": is_loft,
            "is_studio": is_studio
        }

        files = {}
        if image:
            response = requests.get(image)
            files = {"image": BytesIO(response.content)}

        return self.api.post(
            self.get_app(), self.get_action(), params=data, files=files)

    def update(self, community_aptcast_id, aptcast_id, **kwargs):
        self.action = "{0}/{1}/{2}".format(
            community_aptcast_id, self.base_action, aptcast_id)
        files = {}

        if kwargs.get("image"):
            files.update({"image": kwargs.pop("image")})

        return self.api.patch(
            self.get_app(), self.get_action(), params=kwargs, files=files)

    def delete(self, community_aptcast_id, aptcast_id):
        self.action = "{0}/{1}/{2}".format(
            community_aptcast_id, self.base_action, aptcast_id)

        return self.api.delete(self.get_app(), self.get_action())


class UnitResource(Resource):
    app = "community"
    base_action = "units"

    def create(self, floor_plan_aptcast_id, number, building, floor,
               available_date, description, rent_low, rent_high, deposit_low,
               deposit_high, square_feet_low, square_feet_high):
        self.action = "{0}/{1}".format(floor_plan_aptcast_id, self.base_action)

        description_dict = None
        if description:
            description_dict = {
                "body": description
            }

        data = {
            "number": number,
            "building": building,
            "floor": floor,
            "available_date": available_date,
            "description": description_dict,
            "rent": {
                "low": rent_low,
                "high": rent_high
            },
            "deposit": {
                "low": deposit_low,
                "high": deposit_high
            },
            "square_feet": {
                "low": square_feet_low,
                "high": square_feet_high
            }
        }

        return self.api.post(self.get_app(), self.get_action(), params=data)

    def update(self, floor_plan_aptcast_id, aptcast_id, **kwargs):
        self.action = "{0}/{1}/{2}".format(
            floor_plan_aptcast_id, self.base_action, aptcast_id)

        return self.api.patch(self.get_app(), self.get_action(), params=kwargs)

    def delete(self, floor_plan_aptcast_id, aptcast_id):
        self.action = "{0}/{1}/{2}".format(
            floor_plan_aptcast_id, self.base_action, aptcast_id)

        return self.api.delete(self.get_app(), self.get_action())


class HeroShot(CommunityResource):
    app = "community"

    def create(self, community_id, url, width=None, height=None):
        data = {
            "community_id": community_id,
            "url": url,
            "width": width,
            "height": height
        }

        return self.api.post(
            self.app, "{0}/hero_shot".format(
                community_id), params=json.dumps(data))

    def update(self, community_id, url, width=None, height=None):
        data = {
            "community_id": community_id,
            "url": url,
            "width": width,
            "height": height
        }

        return self.api.put(
            self.app, "update/hero_shot", params=json.dumps(data))

    def delete(self, community_id):
        data = {"community_id": community_id}

        return self.api.delete(
            self.app, "delete/hero_shot", params=json.dumps(data))


class LogoImage(CommunityResource):
    def create(self, community_id, url, width=None, height=None):
        data = {
            "community_id": community_id,
            "url": url,
            "width": width,
            "height": height
        }

        return self.api.post(
            self.app, "create/logo", params=json.dumps(data))

    def update(self, community_id, url, width=None, height=None):
        data = {
            "community_id": community_id,
            "url": url,
            "width": width,
            "height": height
        }

        return self.api.put(
            self.app, "update/logo", params=json.dumps(data))

    def delete(self, community_id):
        data = {"community_id": community_id}

        return self.api.delete(
            self.app, "delete/logo", params=json.dumps(data))


class FloorPlan(CommunityResource):
    def create(self, community_id, name, beds, baths, description, image_url,
               price_low, price_high, deposit_low, deposit_high, sqft_low, sqft_high,
               image_height=None, image_width=None):

        data = {
            "community_id": community_id,
            "name": name,
            "beds": beds,
            "baths": baths,
            "description": description,
            "image": {
                "url": image_url,
                "height": image_height,
                "width": image_width,
            },
            "rent": {
                "low": price_low,
                "high": price_high
            },
            "deposit": {
                "low": deposit_low,
                "high": deposit_high
            },
            "square_feet": {
                "low": sqft_low,
                "high": sqft_high
            }
        }

        return self.api.post(
            self.app, "create/floorplan", params=json.dumps(data))

    def update(self, floorplan_id, name, beds, baths, description, image_url,
               price_low, price_high, deposit_low, deposit_high, sqft_low, sqft_high,
               image_height=None, image_width=None):

        data = {
            "floorplan_id": floorplan_id,
            "name": name,
            "beds": beds,
            "baths": baths,
            "description": description,
            "image": {
                "url": image_url,
                "height": image_height,
                "width": image_width,
            },
            "rent": {
                "low": price_low,
                "high": price_high
            },
            "deposit": {
                "low": deposit_low,
                "high": deposit_high
            },
            "square_feet": {
                "low": sqft_low,
                "high": sqft_high
            }
        }

        return self.api.put(
            self.app, "update/floorplan", params=json.dumps(data))

    def delete(self, floorplan_id):
        data = {"floorplan_id": floorplan_id}

        return self.api.delete(
            self.app, "delete/floorplan", params=json.dumps(data))


class Unit(CommunityResource):
    def build(self, community_id, floorplan_id, number, price_low, price_high,
              deposit_low, deposit_high, description="", building="",
              floor="", available_date=None):

        return {
            "community_id": community_id,
            "floorplan_id": floorplan_id,
            "number": number,
            "building": building,
            "floor": floor,
            "available_date": available_date,
            "description": description,
            "price": {
                "low": price_low,
                "high": price_high
            },
            "deposit": {
                "low": deposit_low,
                "high": deposit_high
            }
        }

    def create(self, community_id, floorplan_id, number, price_low, price_high,
               deposit_low, deposit_high, description="", building="",
               floor="", available_date=None):

        data = self.build(
            community_id, floorplan_id, number, price_low, price_high,
            deposit_low, deposit_high, description, building, floor,
            available_date)

        return self.api.post(self.app, "create/unit", params=json.dumps(data))

    def update(self, community_id, floorplan_id, number, price_low, price_high,
               deposit_low, deposit_high, description="", building="",
               floor="", available_date=None):

        data = self.build(
            community_id, floorplan_id, number, price_low, price_high,
            deposit_low, deposit_high, description, building, floor,
            available_date)

        return self.api.put(self.app, "update/unit", params=json.dumps(data))

    def bulk_create(self, units):
        return self.api.post(
            self.app,
            "bulk-create/unit",
            params=json.dumps(units))

    def delete(self, unit_id):
        data = {"unit_id": unit_id}

        return self.api.delete(
            self.app, "delete/unit", params=json.dumps(data))


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

    def create(self, slideshow_aptcast_id, name, description, image):
        self.action = "{0}/{1}/{2}".format(
            self.base_action, slideshow_aptcast_id, self.extra_action)

        data = {
            "name": name or None,
            "description": description or None
        }

        response = requests.get(image)
        import pdb;pdb.set_trace()
        files = {"image": response.content}
        return self.api.post(
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