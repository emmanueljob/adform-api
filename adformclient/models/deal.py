import json

from rest_base import RestBase


class Deal(RestBase):

    obj_name = "deals"
    profile_obj = None

    def get_url(self):
        return "{0}/{1}".format("https://api.adform.com/dsp/v1", self.obj_name)

    def _get_response_objects(self, response):
        rval = []

        if response.status_code != 200:
            raise Exception("Bad response code")

        results = json.loads(response.text)
        for result in results:
            new_obj = self.__class__(RestBase.connection)
            new_obj.import_props(result)
            rval.append(new_obj)

        return rval
