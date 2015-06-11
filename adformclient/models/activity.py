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

    def find_by_id(self, activity_id):
        client = Client(Activity.get_wsdl_url())
        header = {'Ticket': Activity.connection.get_authorization()}
        client.set_options(soapheaders=header)
        resp = client.service.GetActivities(ActivityId=activity_id)
        rval = []
        if len(resp[0]) != 1:
            raise Exception("Should only find one obj for activity_id {0} found: {1}".format(str(activity_id), str(len(resp[0]))))
        for obj in resp[0]:
            toAdd = Activity(Activity.connection)
            toAdd.update(obj)
            return toAdd

        return None
