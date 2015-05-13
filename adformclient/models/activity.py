from adformclient.models.base import Base
from suds.client import Client


class Activity(Base):

    wsdl_url = '/Services/v20130401/RTBActivityService.svc/wsdl'

    def find_by_campaign(self, campaign_id):
        client = Client(Activity.get_wsdl_url())
        header = {'Ticket': Activity.connection.get_authorization()}
        client.set_options(soapheaders=header)
        resp = client.service.GetActivities(CampaignId=campaign_id)

        rval = []
        for obj in resp[0]:
            toAdd = Activity(Activity.connection)
            toAdd.update(obj)
            rval.append(toAdd)

        return rval
