from suds.client import Client


class Connection:

    authorization_token = None

    def __init__(self, username=None, password=None, url=None):
        Connection.username = username
        Connection.password = password
        Connection.url = url

    def connect(self):
        Connection.get_authorization()

    def get_authorization(self):
        #if Connection.authorization_token is None:
        Connection.authorization_token = self.authorize()

        return Connection.authorization_token

    def authorize(self):

        login_service = 'http://api.adform.com/Services/SecurityService.svc/wsdl'

        client = Client(login_service)
        ticket = client.service.Login(UserName=Connection.username, Password=Connection.password)
        Connection.authorization_token = ticket

        return Connection.authorization_token
