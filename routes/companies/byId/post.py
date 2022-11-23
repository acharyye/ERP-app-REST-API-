import os.path
from __main__ import api

from flask import Response, json, make_response, request


@api.route('/companies/<company_id>', methods=['POST', 'PATCH'])
def updateCompanyById(company_id):
    # load json
    with open(os.path.join(os.getcwd(), 'data/companies.json')) as f:
        companies = json.load(f)
    # jq find company by id
    filtered_comps = [item for item in companies if item["id"] == company_id]
    body = request.get_json()

    if len(filtered_comps) == 0:
        # return with 404 status code
        response404 = json.dumps({"error: ": {"code: ": 404}})
        resp = make_response(response404, 404)
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        return resp

    # check if body has [name] field, otherwise return 400
    if 'name' not in body:
        response400 = json.dumps({"error": {"code": 400, "message": "Payload validation failed"}})
        resp = make_response(response400, 400)
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        return resp

    # update found object with value from the [name]
    # find index of: filtered_comps[0] within companies
    index = companies.index(filtered_comps[0])
    companies[index]['name'] = body['name']

    # store back to file
    with open('data/companies.json', 'w') as r:
        json.dump(companies, r)

    return Response(json.dumps({"result": companies[index]['id']}), mimetype='application/json; charset=utf-8')

    # return response
