from adformclient.models.base import Base
from suds.client import Client


class Placement(Base):

    wsdl_url = '/Services/PlacementService.svc/wsdl'

    def find(self, campaign_id, id):
        client = Client(Placement.get_wsdl_url())
        header = {'Ticket': Placement.connection.get_authorization()}
        client.set_options(soapheaders=header)
        ids = client.factory.create('ns1:ArrayOfint')
        ids.int.append(int(id))
        resp = client.service.GetPlacements(CampaignId=campaign_id, Ids=ids)

        if len(resp) != 1:
            return
            raise Exception("Did not return one result")

        rval = Placement(Placement.connection)
        rval.update(resp[0])

        # get the RTB Attrs.
        loader = RTBActivity(Placement.connection)
        rtb_activity = loader.find(campaign_id, id)
        rval['rtb_activity'] = rtb_activity
        return rval
        

    def find_by_campaign(self, campaign_id):
        
        client = Client(Placement.get_wsdl_url())
        header = {'Ticket': Placement.connection.get_authorization()}
        client.set_options(soapheaders=header)
        resp = client.service.GetPlacements(CampaignId=campaign_id)
        rval = []
        for placement in resp:
            to_add = Placement(Placement.connection)
            to_add.update(placement)
            rval.append(to_add)

        return rval
