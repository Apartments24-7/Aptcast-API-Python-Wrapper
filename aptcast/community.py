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
        }
        return self.api.post(self.app, "create",
                             params=json.dumps(data))

    def update(self, name, description, lat, lng, address, city, state,
               postal_code, email, website, phone):

        data = {
            "community": {

            }
        }


class HeroShot(Resource):

    app = "community"

    def create(self, community_id, url):

        data = {
            "community_id": community_id,
            "hero_image": {
                "url": url
            }
        }

        return self.api.post(self.app, "create/hero_shot",
                             params=json.dumps(data))


class BaseAmenity(Resource):

    app = "community"

    def create(self, name):

        data = {
            "name": name
        }

        return self.api.post(self.app, "create/base_amenity",
                             params=json.dumps(data))


class Amenity(Resource):

    app = "community"

    def create(self, community_id, name, base_amenity, order):

        data = {
            "community_id": community_id,
            "amenity": {
                "name": name,
                "base_amenity": base_amenity,
                "order": order
            }
        }

        return self.api.post(self.app, "create/amenity",
                             params=json.dumps(data))


class FloorPlan(Resource):

    app = "community"

    def create(self, community_id, name, beds, baths, description, image_url,
               price_low, price_high, deposit_low, deposit_high,
               image_height=None, image_width=None):

        data = {
            "community_id": community_id,
            "floorplan": {
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
                },
            }
        }
        return self.api.post(self.app, "create/floorplan",
                             params=json.dumps(data))


class SlideShow(Resource):

    app = "community"

    def create(self, community_id, name):

        data = {
            "community_id": community_id,
            "slideshow": {
                "name": name
            }
        }

