from adformclient.models.base import Base
from suds.client import Client


class Campaign(Base):

    wsdl_url = '/Services/v20131225/CampaignService.svc/wsdl'

    def find(self, id):
        client = Client(Campaign.get_wsdl_url())
        header = {'Ticket': Campaign.connection.get_authorization()}
        client.set_options(soapheaders=header)
        ids = client.factory.create('ns1:IdCollection')
        ids.Id.append(id)
        resp = client.service.GetCampaigns(Ids=ids)

        if len(resp) != 1:
            raise Exception("Did not return one result")

        rval = Campaign(Campaign.connection)
        rval.update(resp[0])

        return rval
        

    def find_by_advertiser(self, advertiser_id):
        
        client = Client(Campaign.get_wsdl_url())
        header = {'Ticket': Campaign.connection.get_authorization()}
        client.set_options(soapheaders=header)
        resp = client.service.GetCampaigns(AdvertiserId=advertiser_id)

        rval = []
        for campaign in resp:
            to_add = Campaign(Campaign.connection)
            to_add.update(campaign)
            rval.append(to_add)

        return rval
