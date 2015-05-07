from api import Resource


class CommunityResource(Resource):
    app = "community"
    base_action = "communities"

    def create(self, name, address0, address1, city, state, postal_code, email,
               website, phone, pet_policy_details, dogs, cats, senior,
               section8, student, corporate, military, corporation,
               description, location, logo_description, hero_shot_description,
               logo, hero_shot):
        self.action = self.base_action

        data = {
            "name": name,
            "address0": address0,
            "address1": address1 or None,
            "city": city,
            "state": state,
            "postal_code": postal_code,
            "email": email or None,
            "website": website or None,
            "phone": phone,
            "pet_policy_details": pet_policy_details or None,
            "dogs": dogs or False,
            "cats": cats or False,
            "senior": senior or False,
            "section8": section8 or False,
            "student": student or False,
            "corporate": corporate or False,
            "military": military or False,
            "corporation": corporation,
            "description": description or None,
            "location": location,
            "logo_description": logo_description or None,
            "hero_shot_description": hero_shot_description or None
        }

        files = {}
        if any([logo, hero_shot]):
            if logo:
                files.update({"logo": logo})
            if hero_shot:
                files.update({"hero_shot": hero_shot})

        return self.api.post(
            self.get_app(), self.get_action(), params=data, files=files)

    def update(self, aptcast_id, **kwargs):
        self.action = "{0}/{1}".format(self.base_action, aptcast_id)
        files = {}

        if kwargs.get("logo"):
            files.update({"logo": kwargs.pop("logo")})
        if kwargs.get("hero_shot"):
            files.update({"hero_shot": kwargs.pop("hero_shot")})

        return self.api.patch(
            self.get_app(), self.get_action(), params=kwargs, files=files)


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
               square_feet_hight):
        self.action = "{0}/{1}".format(community_aptcast_id, self.base_action)

        data = {
            "beds": beds,
            "baths": baths,
            "name": name,
            "is_loft": is_loft or False,
            "is_studio": is_studio or False,
            "description": description or None,
            "image_description": image_description or None,
            "rent_low": rent_low,
            "rent_high": rent_high or None,
            "deposit_low": deposit_low,
            "deposit_high": deposit_high or None,
            "square_feet_low": square_feet_low,
            "square_feet_hight": square_feet_hight or None
        }

        files = {}
        if image:
            files.update({"image": image})

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
               deposit_high, square_feet_low, square_feet_hight):
        self.action = "{0}/{1}".format(floor_plan_aptcast_id, self.base_action)

        data = {
            "number": number or None,
            "building": building or None,
            "floor": floor or None,
            "available_date": available_date or None,
            "description": description or None,
            "rent_low": rent_low,
            "rent_high": rent_high or None,
            "deposit_low": deposit_low or None,
            "deposit_high": deposit_high or None,
            "square_feet_low": square_feet_low,
            "square_feet_hight": square_feet_hight or None
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


# class SlideShowImage(Resource):
#     def create(self, slideshow_id, name, url, height, width, description):
#         data = {
#             "slideshow_id": slideshow_id,
#             "name": name,
#             "url": url,
#             "height": height or None,
#             "width": width or None,
#             "description": description or ''
#         }
#
#         return self.api.post(
#             self.app, "create/slideshow/image", params=json.dumps(data))
#
#     def update(self, slideshow_image_id, name, url, height, width,
#                description):
#         data = {
#             "slideshow_image_id": slideshow_image_id,
#             "name": name,
#             "url": url,
#             "height": height,
#             "width": width,
#             "description": description
#         }
#
#         return self.api.put(
#             self.app, "update/slideshow/image", params=json.dumps(data))
#
#     def delete(self, slideshow_image_id):
#         data = {"slideshow_image_id": slideshow_image_id}
#
#         return self.api.delete(
#             self.app, "delete/slideshow/image", params=json.dumps(data))
