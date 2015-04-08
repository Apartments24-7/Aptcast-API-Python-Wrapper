import json

from api import Resource


class CommunityResource(Resource):
    app = "community"


class Community(CommunityResource):
    def create(self, name, description, lat, lng, address, city, state,
               postal_code, email, website, phone):
        data = {
            "description": description,
            "name": name,
            "location": {
                "lat": lat,
                "lng": lng,
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
        return self.api.post(self.app, "create", params=json.dumps(data))

    # def update(self, name, description, lat, lng, address, city, state,
    #            postal_code, email, website, phone):
    #
    #     data = {
    #         "community": {
    #
    #         }
    #     }


class HeroShot(CommunityResource):
    def create(self, community_id, url, width=None, height=None):
        data = {
            "community_id": community_id,
            "url": url,
            "width": width,
            "height": height
        }

        return self.api.post(
            self.app, "create/hero_shot", params=json.dumps(data))

    def update(self, community_id, url, width=None, height=None):
        data = {
            "community_id": community_id,
            "url": url,
            "width": width,
            "height": height
        }

        return self.api.put(
            self.app, "update/hero_shot", params=json.dumps(data))


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


class BaseAmenity(CommunityResource):
    def create(self, name):
        data = {
            "name": name
        }

        return self.api.post(
            self.app, "create/base_amenity", params=json.dumps(data))

    def update(self, amenity_id, name):
        data = {
            'amenity_id': amenity_id,
            'name': name
        }

        return self.api.put(
            self.app, "update/base_amenity", params=json.dumps(data))


class Amenity(CommunityResource):
    def create(self, community_id, name, base_amenity, order):
        data = {
            "community_id": community_id,
            "name": name,
            "base_amenity": base_amenity,
            "order": order
        }

        return self.api.post(
            self.app, "create/amenity", params=json.dumps(data))

    def update(self, community_id, name, base_amenity, order):
        data = {
            "community_id": community_id,
            "name": name,
            "base_amenity": base_amenity,
            "order": order
        }

        return self.api.put(
            self.app, "update/amenity", params=json.dumps(data))


class FloorPlan(CommunityResource):
    def create(self, community_id, name, beds, baths, description, image_url,
               price_low, price_high, deposit_low, deposit_high,
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
            "price": {
                "low": price_low,
                "high": price_high
            },
            "deposit": {
                "low": deposit_low,
                "high": deposit_high
            }
        }

        return self.api.post(
            self.app, "create/floorplan", params=json.dumps(data))

    def update(self, floorplan_id, name, beds, baths, description, image_url,
               price_low, price_high, deposit_low, deposit_high,
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
            "price": {
                "low": price_low,
                "high": price_high
            },
            "deposit": {
                "low": deposit_low,
                "high": deposit_high
            }
        }

        return self.api.put(
            self.app, "update/floorplan", params=json.dumps(data))


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


class SlideShow(CommunityResource):
    def create(self, community_id, name):
        data = {"community_id": community_id, "name": name}

        return self.api.post(
            self.app, "create/slideshow", params=json.dumps(data))

    def update(self, slideshow_id, name):
        data = {"slideshow_id": slideshow_id, "name": name}

        return self.api.put(
            self.app, "update/slideshow", params=json.dumps(data))


class SlideShowImage(CommunityResource):
    def create(self, slideshow_id, name, url, height, width, description):
        data = {
            "slideshow_id": slideshow_id,
            "name": name,
            "url": url,
            "height": height or None,
            "width": width or None,
            "description": description or ''
        }

        return self.api.post(
            self.app, "create/slideshow/image", params=json.dumps(data))

    def update(self, slideshow_image_id, name, url, height, width,
               description):
        data = {
            "slideshow_image_id": slideshow_image_id,
            "name": name,
            "url": url,
            "height": height,
            "width": width,
            "description": description
        }

        return self.api.put(
            self.app, "update/slideshow/image", params=json.dumps(data))
