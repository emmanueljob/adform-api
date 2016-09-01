import unittest

from adformclient.service.connection import Connection
from adformclient.models.advertiser import Advertiser
from tests.base import Base


class AdvertiserTest(Base):

    def testGet(self):

        loader = Advertiser(AdvertiserTest.conn)
        Advertiser.connection.get_authorization()
        advs = loader.find("Accuen Demo") 
        
        for adv in advs:
            print "\n"
            print adv
            print adv['Name']
