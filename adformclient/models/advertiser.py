from adformclient.models.base import Base
from suds.client import Client


class Advertiser(Base):

    wsdl_url = '/Services/AdvertiserService.svc/wsdl'

    def find(self):
        
        client = Client(Advertiser.get_wsdl_url())
        header = {'Ticket': Advertiser.connection.get_authorization()}
        client.set_options(soapheaders=header)
        resp = client.service.GetAdvertisers()

        rval = []
        for adv in resp:
            to_add = Advertiser(Advertiser.connection)
            to_add.update(adv)
            rval.append(to_add)

        return rval
