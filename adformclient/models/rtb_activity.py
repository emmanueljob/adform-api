from rest_base import RestBase

from .deal import Deal

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
        
        ##
        # The documentation for AdForm is not complete and this works. If you change
        # this make sure you know what you're doing. If its not intuitive its because
        # the AdForm API isn't intuitive so be careful.
        #
        # If you want to make changes the best way to do it is to change inventory in the UI
        # and inspect the calls to see how the inventories are passed and specifically what the "states"
        # are set to.
        ##

        # Make sure deals are all ints
        deals = [int(deal) for deal in deals]
        
        inventory_sources_we_have = {}
        # get a list inventory_sources we have already
        inventories = self.get('Inventories', [])
        for inventory in inventories:
            if inventory.get('SourceType') == 1:
                inventory_sources_we_have[inventory.get('InventorySourceId')] = inventory
        
        inventory_sources_we_need = []
        # reset all current deals
        inventories = self.get('Inventories', [])
        for inventory in inventories:
            if int(inventory['SourceId']) in deals:
                # keep deal
                inventory['State'] = 1
                deals.remove(inventory['SourceId'])
                inventory_sources_we_need.append(inventory['InventorySourceId'])
            else:
                # remove deal
                inventory['State'] = 3

        for deal_id in deals:
            # add deal
            deal = Deal(RTBActivity.connection).find(deal_id)
            inventory_sources_we_need.append(deal.get('InventorySourceId'))
            self.get('Inventories').append({'InventorySourceId': deal.get('InventorySourceId'), 'DealId': deal.get('DealId'), 'SourceId': deal_id, 'State': 2, 'SourceType': 3})

        for inventory_source_id in inventory_sources_we_need:
            if inventory_source_id in inventory_sources_we_have:
                for inventory in self.get('Inventories', []):
                    if inventory.get('SourceId') == inventory_source_id:
                        # not documented anywhere in AdForm but for exchanges we should use State: 4 all the time.
                        inventory['State'] = 4
            else:
                self.get('Inventories').append({'SourceId': inventory_source_id, 'InventorySourceId': inventory_source_id, 'SourceType': 1, 'State': 2})
                

    def get_deals(self):
        rval = []
        for inventory in self.get('Inventories', []):
            rval.append(inventory.get('SourceId'))
        return rval

    def find(self, campaign_id, activity_id):
        url = "{0}?campaignId={1}&ActivityId={2}".format(self.get_url(), campaign_id, activity_id)

        response = self._execute("GET", url, None)

        return self._get_response_object(response)
