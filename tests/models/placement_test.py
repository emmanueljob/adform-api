import unittest
import json

from adformclient.models.placement import Placement
from tests.base import Base


class PlacementTest(Base):

    def testGetByCampaign(self):
        loader = Placement(PlacementTest.conn)
        placements = loader.find_by_campaign(362140)

        for placement in placements:
            assert placement.get('Id') is not None

    def testFind(self):
        loader = Placement(PlacementTest.conn)
        placement = loader.find(362140, 159383)
        assert placement.get('Id') is not None
        
