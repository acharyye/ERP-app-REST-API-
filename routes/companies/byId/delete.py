from __main__ import api

from flask import Response, json, make_response
import os.path


@api.route('/companies/<company_id>', methods=['DELETE'])
def deleteCompanyById(company_id):
    # load json
    with open(os.path.join(os.getcwd(), 'data/companies.json')) as t:
        companies = json.load(t)

    filtered_comps = [item for item in companies if item["id"] == company_id]

    if len(filtered_comps) == 0:
        # return with 404 status code
        response404 = json.dumps({"error": {"code": 404}})
        resp = make_response(response404, 404)
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        return resp

    # find index of: filtered_comps[0] within companies
    index = companies.index(filtered_comps[0])

    del companies[index]

    # save back to file
    with open('data/companies.json', 'w') as f:
        json.dump(companies, f)

    return Response(json.dumps({"result": {}}), mimetype='application/json; charset=utf-8')
