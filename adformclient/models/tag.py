from adformclient.models.base import Base
from suds.client import Client


class Tag(Base):

    wsdl_url = '/Services/TagService.svc/wsdl'

    def find_by_campaign(self, campaign_id):
        client = Client(Tag.get_wsdl_url())
        header = {'Ticket': Tag.connection.get_authorization()}
        client.set_options(soapheaders=header)
        
        resp = client.service.GetTags(CampaignId=campaign_id)
        rval = []
        for tag in resp:
            to_add = Tag(Tag.connection)
            to_add.update(tag)
            rval.append(to_add)

        return rval

    def find_by_placement(self, campaign_id, placement_id):
        tags = self.find_by_campaign(campaign_id)
        rval = []
        for tag in tags:
            if tag.get('PlacementId') == placement_id:
                rval.append(tag)
        return rval

    def find(self, id):
        client = Client(Tag.get_wsdl_url())
        header = {'Ticket': Tag.connection.get_authorization()}
        client.set_options(soapheaders=header)

        ids = client.factory.create('s1:ArrayOfint')
        ids.int.append(id)
        resp = client.service.GetTags(Ids=ids)

        rval = Tag(Tag.connection)
        rval.update(resp[0])
        return rval
