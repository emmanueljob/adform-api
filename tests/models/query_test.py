import unittest
import json

from dbmclient.models.query import Query
from tests.base import Base


class QueryTest(Base):

    test_query = """{
 "kind": "doubleclickbidmanager#query",
 "metadata": {
  "title": "API test",
  "dataRange": "PREVIOUS_WEEK",
  "format": "CSV"
 },
 "params": {
  "type": "TYPE_CROSS_PARTNER",
  "groupBys": [
   "FILTER_DATE",
   "FILTER_INSERTION_ORDER"
  ],
  "filters": [
   {
    "type": "FILTER_PARTNER",
    "value": "191"
   }
  ],
  "metrics": [
   "METRIC_IMPRESSIONS",
   "METRIC_CLICKS",
   "METRIC_TOTAL_CONVERSIONS",
   "METRIC_LAST_CLICKS",
   "METRIC_LAST_IMPRESSIONS",
   "METRIC_REVENUE_ADVERTISER",
   "METRIC_MEDIA_COST_ADVERTISER",
   "METRIC_CTR"
  ],
  "includeInviteData": false
 },
 "schedule": {
  "frequency": "ONE_TIME",
  "endTimeMs": "0",
  "nextRunTimezoneCode": "America/New_York"
 }
}"""

    def testGetAll(self):
        loader = Query(QueryTest.conn)
        queries = loader.find_all()
        for query in queries:
            assert query['queryId'] is not None

    def testCreate(self):
        loader = Query(QueryTest.conn)
        query = loader.create(self.test_query)
        
        assert int(query['queryId']) > 0

        body = {"dataRange": "PREVIOUS_WEEK"}
        # loader.run(query['queryId'], body)

        # just make sure we get here
        assert 1 == 1
