from rest_base import RestBase


class RTBActivity(RestBase):

    obj_name = "Activities"
    profile_obj = None

    def set_domains(self, domains):
        pass

    def get_domains(self):
        pass

    def set_deals(self, deals):
        pass

    def get_deals(self):
        pass

    def find(self, campaign_id, line_item_id):
        url = "{0}?campaignId={1}&ActivityId={2}".format(self.get_url(), campaign_id, line_item_id)

        response = self._execute("GET", url, None)

        return self._get_response_object(response)
