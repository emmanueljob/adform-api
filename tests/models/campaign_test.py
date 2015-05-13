import unittest
import json

from adformclient.models.campaign import Campaign
from tests.base import Base


class CampaignTest(Base):

    def testGetByAdvertiser(self):
        loader = Campaign(CampaignTest.conn)
        campaigns = loader.find_by_advertiser('31647')

        for campaign in campaigns:
            assert campaign.get('Id') is not None

    def testFind(self):
        loader = Campaign(CampaignTest.conn)
        campaign = loader.find(362140)

        assert campaign.get('Id') is not None
        
