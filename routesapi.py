#routesapi.py

import falcon
import json

from db_client import * 

class routesResource(object):
    def on_get(self, req, resp):
        dbo = r.db(PROJECT_DB).table(PROJECT_TABLE)
        if req.get_param("id"):
            result = {'route': dbo.get(req.get_param("id")).run(db_connection)}
        else:
            routes = dbo.run(db_connection)
            result = {'routes': [i for i in routes]}
        resp.body = json.dumps(result)
        resp.status = falcon.HTTP_200

api = falcon.API()
api.add_route("/routes", routesResource())
