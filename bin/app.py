import falcon
from resource import Resource

app = application = falcon.App()

x = Resource()
app.add_route('/', x)
