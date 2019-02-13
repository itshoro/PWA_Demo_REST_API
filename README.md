# PWA Demo REST API
This REST API is used to serve base64 encoded image files.
It is used for demo purposes during my talk on Progressive Web Applications to simulate a real world use case of them.

## Requirements
- Python 3

```
pip install flask
pip install flask-restful
```

## Usage

Create an `imgs` folder  and add `.jpg` files that are to be served via this API.

```
python app.py
```

You can use GET, PUT, PUSH and DELETE Methods on `127.0.0.1:5000/api/` to get, add, change or remove entries.
Responses are in a JSON format.

The `setup.sh` script adds all `.jpg` files from the `imgs` folder via a PUT Method.
