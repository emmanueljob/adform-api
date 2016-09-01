import unittest

from adformclient.models.deal import Deal
from tests.base import Base


class DealTest(Base):

    def testFind(self):
        loader = Deal(DealTest.conn)
        deals = loader.find()

        for deal in deals:
            print deal
            assert deal.get('Id') is not None
