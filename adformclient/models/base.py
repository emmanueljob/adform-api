
class Base(dict):

    connection = None

    def __init__(self, connection):
        Base.connection = connection
        super(Base, self).__init__()

    @classmethod
    def get_wsdl_url(self):
        return "{0}{1}".format(Base.connection.url, self.wsdl_url)
