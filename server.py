import argparse

from flask import Flask

parser = argparse.ArgumentParser(description="An additional program")

parser.add_argument("--port", nargs='*', metavar="num", type=int,
                    help="Server port", default=3000)

parser.add_argument("--host", nargs='*',
                    help="Server port", default='0.0.0.0')

args = parser.parse_args()

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

# GET /companies
import routes.companies.get

# GET /companies/{ID}
import routes.companies.byId.get

# POST /companies (create)
import routes.companies.post

# POSt /companies/{ID} update
import routes.companies.byId.post

# DELETE /companies/{ID}
import routes.companies.byId.delete

if __name__ == '__main__':
    api.run(host=args.host, port=args.port)
