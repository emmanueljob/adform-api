import unittest
import json

from adformclient.models.tag import Tag
from tests.base import Base


class TagTest(Base):

    def testGetByCampaign(self):
        loader = Tag(TagTest.conn)
        tags = loader.find_by_campaign(676348)

        for tag in tags:
            assert tag.get('Id') is not None

    def testFind(self):
        loader = Tag(TagTest.conn)
        tag = loader.find(13800107)

        assert tag.get('Id') is not None
        
