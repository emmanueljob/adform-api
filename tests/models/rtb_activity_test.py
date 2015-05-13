import unittest
import json

from adformclient.models.activity import Activity
from adformclient.models.rtb_activity import RTBActivity
from tests.base import Base


class RTBActivityTest(Base):

    def testGetByCampaign(self):
        loader = Activity(RTBActivityTest.conn)
        rtb_activities = loader.find_by_campaign(362140)

        for rtb_activity in rtb_activities:
            print rtb_activity.get('Id')
            assert rtb_activity.get('Id') is not None
        print "DONE"

    def testFind(self):
        loader = RTBActivity(RTBActivityTest.conn)
        rtb_activity = loader.find(362140, 159383)
        assert rtb_activity.get('Id') is not None
        
