from adformclient.models.base import Base
from suds.client import Client


class Placement(Base):

    wsdl_url = '/Services/PlacementService.svc/wsdl'

    def find(self, campaign_id, id):
        client = Client(Placement.get_wsdl_url())
        print client
        header = {'Ticket': Placement.connection.get_authorization()}
        client.set_options(soapheaders=header)
        ids = client.factory.create('ns1:ArrayOfint')
        ids.int.append(int(id))
        resp = client.service.GetPlacements(CampaignId=campaign_id, Ids=ids)

        print resp

        if len(resp) != 1:
            print "LEN: {0}".format(str(len(resp)))
            return
            raise Exception("Did not return one result")

        rval = Placement(Placement.connection)
        rval.update(resp[0])

        return rval
        

    def find_by_campaign(self, campaign_id):
        
        client = Client(Placement.get_wsdl_url())
        header = {'Ticket': Placement.connection.get_authorization()}
        client.set_options(soapheaders=header)
        resp = client.service.GetPlacements(CampaignId=campaign_id)
        print resp
        rval = []
        for placement in resp:
            to_add = Placement(Placement.connection)
            to_add.update(placement)
            rval.append(to_add)

        return rval
