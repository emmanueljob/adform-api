import json

from rest_base import RestBase


class Deal(RestBase):

    obj_name = "deals"
    profile_obj = None

    def find(self, id=None):
        if id is None:
            url = "{0}/{1}".format("https://api.adform.com/dsp/v1", self.obj_name)
            response = self._execute("GET", url, None)

            rval = []
            if response:
                rval = self._get_response_objects(response)
            return rval
        else:
            url = "{0}/{1}?search={2}".format("https://api.adform.com/dsp/v1", self.obj_name, id)
            response = self._execute("GET", url, None)

            if response:
                deals = self._get_response_objects(response)
                for deal in deals:
                    if deal.get('Id') == id:
                        rval = self.__class__(RestBase.connection)
                        rval.import_props(deal)
                        return rval

                return None
            else:
                return None


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
