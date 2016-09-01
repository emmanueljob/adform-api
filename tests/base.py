import unittest
import logging

from adformclient.conf.properties import Properties
from adformclient.service.connection import Connection


class Base(unittest.TestCase):

    conn = None

    def __init__(self, *args, **kwargs):

        props = Properties("test")
        self.username = props.username
        self.password = props.password
        self.url = props.url
        logger = logging.getLogger('suds')
        logger.propagate = False
        Base.conn = Connection(username=self.username,
                               password=self.password,
                               url=self.url)

        super(Base, self).__init__(*args, **kwargs)
