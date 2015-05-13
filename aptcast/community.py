import json
import requests

from api import Resource
from io import BytesIO


class CommunityResource(Resource):
    app = "community"
    base_action = "communities"

    def create(self, name, lat, lng, address0, address1, city, state,
               postal_code, email, website, phone, pet_policy_details, dogs,
               cats, senior, section8, student, corporate, military,
               corporation, description, location, logo_description,
               hero_shot_description):
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

        return self.api.post(
            self.get_app(), self.get_action(), params=data)

    def update(self, aptcast_id, name, lat, lng, address0, address1, city,
               state, postal_code, email, website, phone, pet_policy_details,
               dogs, cats, senior, section8, student, corporate, military,
               corporation, description, location, logo_description,
               hero_shot_description):
        self.action = "{0}/{1}".format(self.base_action, aptcast_id)

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
        return self.api.put(
            self.get_app(), self.get_action(), params=data)

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

    def create(self, community_aptcast_id, beds, baths, name, is_loft,
               is_studio, description, rent_low,
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

        return self.api.post(
            self.get_app(), self.get_action(), params=data)

    def update(self, community_aptcast_id, aptcast_id, **kwargs):
        self.action = "{0}/{1}/{2}".format(
            community_aptcast_id, self.base_action, aptcast_id)
        files = {}

        return self.api.patch(
            self.get_app(), self.get_action(), params=kwargs, files=files)

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
                    response.headers.get('content-type', "")
                )
            }
        else:
            return {}

        return self.api.post_multipart(self.app, "{0}/image".format(
            self.action), files=files)

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


class HeroShotResource(Resource):
    app = "community"

    def create(self, community_id, image_url, width=None, height=None):

        if image_url:
            response = requests.get(image_url, timeout=10)
            files = {
                "image": (
                    image_url.split("/")[-1],
                    BytesIO(response.content),
                    response.headers.get('content-type', "")
                )
            }
        else:
            return {}

        return self.api.post_multipart(
            self.app, "{0}/hero-shot".format(
                community_id), files=files)

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


class LogoImageResource(Resource):
    app = "community"

    def create(self, community_id, image_url, width=None, height=None):

        if image_url:
            response = requests.get(image_url, timeout=10)
            files = {
                "image": (
                    image_url.split("/")[-1],
                    BytesIO(response.content),
                    response.headers.get('content-type', "")
                )
            }
        else:
            return {}

        return self.api.post_multipart(self.app, "{0}/logo".format(
            community_id), files=files)

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
                response.headers.get('content-type', "")
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
