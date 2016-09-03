import unittest
import json

from adformclient.models.activity import Activity
from adformclient.models.rtb_activity import RTBActivity
from tests.base import Base


class RTBActivityTest(Base):

    def testGetByCampaign(self):
        loader = Activity(RTBActivityTest.conn)
        activities = loader.find_by_campaign(676348)

        for activity in activities:
            assert activity.get('Id') is not None

    def testFind(self):
        loader = RTBActivity(RTBActivityTest.conn)
        rtb_activity = loader.find(676348, 408079)
        assert rtb_activity.get('Id') is not None

    def testUpdate(self):
        loader = RTBActivity(RTBActivityTest.conn)
        rtb_activity = loader.find(676348, 408079)
        rtb_activity.set_deals([2641])
        rtb_activity.save()
