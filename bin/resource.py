import json

import falcon


class Resource:

    def on_get(self, req, resp):

        # Create a JSON representation of the resource
        resp.text = json.dumps({"message": "Hello World"}, ensure_ascii=False)

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200
