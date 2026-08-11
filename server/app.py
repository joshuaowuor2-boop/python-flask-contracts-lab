#!/usr/bin/env python3

from flask import Flask, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)


@app.route('/contract/<int:id>')
def contract(id):
    # Contract data is not sensitive, so it's safe to return in full.
    contract = next((c for c in contracts if c["id"] == id), None)
    if contract is None:
        return make_response("", 404)
    return make_response(contract["contract_information"], 200)


@app.route('/customer/<customer_name>')
def customer(customer_name):
    # Customer data is sensitive: only confirm existence, never return details.
    if customer_name in customers:
        return make_response("", 204)
    return make_response("", 404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
