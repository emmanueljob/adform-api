from rest_base import RestBase


class RTBActivity(RestBase):

    obj_name = "Activities"
    profile_obj = None

    def set_domains(self, domains):
        if domains and len(domains) > 0:
            if "DomainPatterns" not in self:
                self['DomainPatterns'] = {}
            if "IncludedDomains" not in self["DomainPatterns"]:
                self["DomainPatterns"]["IncludedDomains"] = {}
            self["DomainPatterns"]["IncludedDomains"] = "\n".join(domains)
            self["DomainPatterns"]["DomainFilterMethod"] = 2
            self["DomainPatterns"]["IsInDomainsEditMode"] = True

    def get_domains(self):
        domain_string = self.get("DomainPatterns", {}).get('IncludedDomains')
        if len(domain_string) > 1:
            return self.get("DomainPatterns", {}).get('IncludedDomains').split("\n")
        else:
            return []

    def set_deals(self, deals):

        # reset all current deals
        inventories = self.get('Inventories', [])
        for inventory in inventories:
            if inventory['SourceId'] in deals:
                inventory['State'] = 1
                deals.remove(inventory['SourceId'])
            else:
                inventory['State'] = 3

        for deal in deals:
            self.get('Inventories').append({'InventorySourceId': deal, 'SourceId': deal, 'SourceType': 1})

    def get_deals(self):
        rval = []
        for inventory in self.get('Inventories', []):
            rval.append(inventory.get('SourceId'))
        return rval

    def find(self, campaign_id, activity_id):
        url = "{0}?campaignId={1}&ActivityId={2}".format(self.get_url(), campaign_id, activity_id)

        response = self._execute("GET", url, None)

        return self._get_response_object(response)
