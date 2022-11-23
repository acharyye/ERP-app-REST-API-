from __main__ import api
from flask import Response, json
import os

with open(os.path.join(os.getcwd(), 'data/companies.json')) as f:
    companies = json.load(f)


@api.route('/companies', methods=['GET'])
def getCompnyById():
    return Response(json.dumps({"result": companies}), mimetype='application/json; charset=utf-8')
