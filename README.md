# Contracts Lab

A small Flask API for a company that manages contracts between two parties. It exposes two read-only endpoints: one for contract details (not sensitive) and one that only confirms whether a customer exists, without exposing any of their data.

## Description

This app demonstrates using HTTP status codes to communicate intent, not just success/failure:

- **`GET /contract/<id>`** — looks up a contract by numeric id in an in-memory list.
  - **200 OK** — contract found; response body is the contract's `contract_information` string.
  - **404 Not Found** — no contract with that id.

- **`GET /customer/<customer_name>`** — checks whether a customer name exists in an in-memory list.
  - **204 No Content** — customer found, but since customer data is sensitive, the response body is intentionally empty.
  - **404 Not Found** — no customer with that name.

## Installation

Requirements: Python 3 and [pipenv](https://pipenv.pypa.io/).

```bash
pipenv install
pipenv shell
```

> Note: the `Pipfile` no longer pins exact `flask`/`pytest`/`Werkzeug` versions. The lab was originally written against Python 3.8; on newer Python versions (3.12+) the old pinned versions fail to import (`ast.Str` and `pkgutil.get_loader` were removed from the standard library), so the dependencies are left unpinned to resolve to versions compatible with your interpreter.

## Usage

Run the server from the `server/` directory:

```bash
cd server
python app.py
```

The API is served at `http://localhost:5555`. Example requests:

```bash
curl -i http://localhost:5555/contract/1        # 200, contract text in the body
curl -i http://localhost:5555/contract/100      # 404, empty body
curl -i http://localhost:5555/customer/bob      # 204, empty body
curl -i http://localhost:5555/customer/mario    # 404, empty body
```

## Verification

Test suite (`server/testing/app_test.py`), run with `pytest`:

```
Flask application in app.py has a resource available at "/contract/<id>". PASSED
Flask application in app.py Returns correct contract_information data PASSED
Flask application in app.py '/contract/<is> route is a 404 if contract does not exists PASSED
Flask application in app.py has a resource available at "/customer/<customer_name>". PASSED
Flask application in app.py returns response body of "" for customer PASSED
Flask application in app.py '/customer/<customer_name> route is a 404 if customer does not exists PASSED

======================= 6 passed in 0.31s =======================
```

Live server, hit with `curl -i`:

```
$ curl -i http://localhost:5555/contract/1
HTTP/1.1 200 OK
Content-Length: 45

This contract is for John and building a shed

$ curl -i http://localhost:5555/contract/100
HTTP/1.1 404 NOT FOUND
Content-Length: 0

$ curl -i http://localhost:5555/customer/bob
HTTP/1.1 204 NO CONTENT

$ curl -i http://localhost:5555/customer/mario
HTTP/1.1 404 NOT FOUND
Content-Length: 0
```

## Testing

```bash
pytest server/testing/app_test.py -v
```

## Support

Open an issue on this repository if you run into a problem.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

See [LICENSE.md](LICENSE.md).
