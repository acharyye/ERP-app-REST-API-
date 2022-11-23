import os.path
from __main__ import api

from flask import Response, json, make_response


@api.route('/companies/<company_id>', methods=['GET'])
def getCompanies(company_id):
    # load json
    with open(os.path.join(os.getcwd(), 'data/companies.json')) as f:
        companies = json.load(f)
    # jq find company by id
    filtered_comps = [item for item in companies if item["id"] == company_id]

    if len(filtered_comps) == 0:
        # return with 404 status code
        response404 = json.dumps({"error": {"code": 404}})
        resp = make_response(response404, 404)
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        return resp

    return Response(json.dumps({"result": filtered_comps[0]}), mimetype='application/json; charset=utf-8')
