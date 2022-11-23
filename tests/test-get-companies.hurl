GET http://localhost:3000/companies

HTTP/* *

[Asserts]
status == 200
jsonpath "$.result" count > 0