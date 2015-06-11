import unittest
import json

from adformclient.models.activity import Activity
from adformclient.models.rtb_activity import RTBActivity
from tests.base import Base


class RTBActivityTest(Base):

    def testGetByCampaign(self):
        loader = Activity(RTBActivityTest.conn)
        activities = loader.find_by_campaign(362140)

        for activity in activities:
            assert activity.get('Id') is not None

    def testFind(self):
        loader = RTBActivity(RTBActivityTest.conn)
        rtb_activity = loader.find(362140, 159383)

        assert rtb_activity.get('Id') is not None

    def testUpdate(self):
        loader = RTBActivity(RTBActivityTest.conn)
        rtb_activity = loader.find(362140, 159383)
        # {"SourceType": 1, "SourceName": "_PRM ExDealAppNexus", "DealId": null, "SourceId": 653, "State": 3, "InventorySourceId": 653, "Id": 10572292}
        # rtb_activity['Inventories'].append({"State": 2, "InventorySourceId": 653, "SourceType": 1, "Id": 10572292})
        rtb_activity.set_deals([653])
        rtb_activity.save()
