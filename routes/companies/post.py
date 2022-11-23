from __main__ import api
import random
from flask import Response, request, json, make_response
import os.path


@api.route('/companies', methods=['POST'])
def post_companies():
    with open(os.path.join(os.getcwd(), 'data/companies.json')) as t:
        companies = json.load(t)
    randomIdBetween = random.randint(1000, 10000)

    if not request.data:
        response400 = json.dumps({"error": {"code": 400, "message:": "Payload validation failed. Empty body"}})
        resp = make_response(response400, 400)
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        return resp

    body = request.get_json()

    if 'name' not in body:
        response400 = json.dumps({"error": {"code": 400, "message:": "Payload validation failed"}})
        resp = make_response(response400, 400)
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        return resp

    body['id'] = randomIdBetween.__str__()
    companies.append(body)

    with open('data/companies.json', 'w') as r:
        json.dump(companies, r)

    return Response(json.dumps({"result": randomIdBetween.__str__()}), mimetype='application/json; charset=utf-8')

# make proper format of json with name and id

# insert json in format {id: '123', name:"name from postman"} into companies.json
# save the changes
# return to user all companies (including newly created one)


# return Response(json.dumps({"result: ": {}}), mimetype='application/json; charset=utf-8')
