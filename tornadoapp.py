# -*- coding: utf-8 -
# tornadoapp.py
# This file is part of gunicorn released under the MIT license.
# See the NOTICE for more information.
#
# Run with:
#
#   $ gunicorn -k tornado tornadoapp:app
#
from tornado import web
import os

class IndexHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, world")
 
settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug" : True
}
 
application = web.Application([
    (r'/', IndexHandler),
    (r'/index', IndexHandler),
],**settings)
