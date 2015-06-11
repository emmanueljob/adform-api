import json
import requests


class RestBase(dict):

    connection = None

    # Needs to be defined in the subclass
    obj_name = None

    def __init__(self, connection):
        RestBase.connection = connection
        super(RestBase, self).__init__()

    def get_url(self):
        return "{0}/{1}".format("https://api.adform.com/Services/RTBActivity/v20141111", self.obj_name)
        # return "{0}/{1}".format(RestBase.connection.url, self.obj_name)

    def get_create_url(self):
        return self.get_url()

    def get_find_url(self, id):
        return "{0}/{1}".format(self.get_url(), id)

    def find(self, id=None):
        if id is None:
            response = self._execute("GET", self.get_url(), None)

            rval = []
            if response:
                rval = self._get_response_objects(response)
            return rval
        else:
            response = self._execute("GET", self.get_find_url(id), None)

            if response:
                return self._get_response_object(response)
            else:
                return None

    def create(self):
        if id in self:
            del self['id']

        response = self._execute("POST", self.get_create_url(), json.dumps(self.export_props()))
        obj = self._get_response_object(response)
        self.import_props(obj)

        return self.getId()

    def getId(self):
        return self.get('Id')

    def save(self):
        if self.getId() is None or self.getId() == 0:
            raise Exception("cant update an object with no id")

        response = self._execute("PUT", self.get_url(), json.dumps(self.export_props()))
        obj = self._get_response_object(response)
        self.import_props(obj)

        return self.getId()

    def _execute(self, method, url, payload):
        return self._execute_no_reauth(method, url, payload)

    def _execute_no_reauth(self, method, url, payload):
        headers = {'Ticket': RestBase.connection.get_authorization()}

        headers['Content-Type'] = 'application/json'

        if method == "GET":
            print "curl -H 'Content-Type: application/json' -H 'Ticket: {0}' -d '{1}' '{2}'".format(headers['Ticket'], payload, url)
            return requests.get(url, headers=headers, data=payload)
        elif method == "POST":
            print "curl -XPOST -H 'Content-Type: application/json' -H 'Ticket: {0}' -d '{1}' '{2}'".format(headers['Ticket'], payload, url)
            return requests.post(url, headers=headers, data=payload)
        elif method == "PUT":
            print "curl -XPUT -H 'Content-Type: application/json' -H 'Ticket: {0}' -d '{1}' '{2}'".format(headers['Ticket'], payload, url)
            return requests.put(url, headers=headers, data=payload)
        elif method == "DELETE":
            return requests.delete(url, headers=headers)
        else:
            raise Exception("Unknown method")

    def _get_response_objects(self, response):
        rval = []
        obj = json.loads(response.text)
        if obj and 'Result' in obj:
            results = obj.get('Result')
            for result in results:
                new_obj = self.__class__(RestBase.connection)
                new_obj.import_props(result)
                rval.append(new_obj)
        else:
            raise Exception("Bad response code")

        return rval

    def _get_response_object(self, response):
        obj = json.loads(response.text)
        new_obj = None
        if obj and response.status_code == 200:
            new_obj = self.__class__(RestBase.connection)
            new_obj.import_props(obj)
        else:
            raise Exception("Bad response code")

        return new_obj

    def import_props(self, props):
        for key, value in props.iteritems():
            self[key] = value

    def export_props(self):
        rval = {}
        # do this an obvious way because using __dict__ gives us params we dont need.
        for key, value in self.iteritems():
            rval[key] = value

        return rval
