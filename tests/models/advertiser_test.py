import unittest

from adformclient.models.advertiser import Advertiser
from tests.base import Base


class AdvertiserTest(Base):

    def testGet(self):

        loader = Advertiser(AdvertiserTest.conn)
        Advertiser.connection.get_authorization()
        advs = loader.find() 
        
        for adv in advs:
            print adv['Name']
