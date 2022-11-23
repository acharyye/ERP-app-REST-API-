# Test if API endpoint exists
GET http://localhost:3000/companies

HTTP/* *

[Asserts]
status == 200

# test creation of the company, should fail on empty json
POST http://localhost:3000/companies
{
}

HTTP/* *

[Asserts]
status == 400

# test creation of the company, should fail on wrong payload
POST http://localhost:3000/companies
{
    "debug": true
}

HTTP/* *

[Asserts]
status == 400

# test creation of the company
POST http://localhost:3000/companies
{
    "name": "Some company name"
}

HTTP/* *

[Asserts]
status == 200

[Captures]
company_id: jsonpath "$.result"

# fail with sending empty body
POST http://localhost:3000/companies/{{company_id}}

HTTP/* *

[Asserts]
status == 400

# fail with sending wrong body
POST http://localhost:3000/companies/{{company_id}}
{
    "debug": true
}

HTTP/* *

[Asserts]
status == 400

# fail with sending wrong body
POST http://localhost:3000/companies/{{company_id}}
{
    "name": "Modified company name"
}

HTTP/* *

[Asserts]
status == 200

# verify company record
GET http://localhost:3000/companies/{{company_id}}

HTTP/* *

[Asserts]
jsonpath "$.result.name" == "Modified company name"

# cleanup. deleting created record
DELETE http://localhost:3000/companies/{{company_id}}

HTTP/* *

[Asserts]
status == 200