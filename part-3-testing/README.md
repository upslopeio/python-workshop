# Testing FastAPI

## Local Setup

1. Clone this repo
1. `cd python-curriculum/part-3-testing`
1. Run the following commands:

    ```
    virtualenv venv
    source venv/bin/activate
    pip install pipenv
    pipenv install --dev
    ```

1. Check that the app works locally

    ```
    python -m uvicorn app.main:app --reload
    ```

    Open http://localhost:8000/

## Adding Tests

Install the testing library `pytest` using `pipenv`:

```
pipenv install pytest --dev
```

When you run tests, `pytest` will create a `.pytest_cache` folder, so add that to your `.gitignore` file:

```
.pytest_cache
```

## Create the test file

Create a file named `app/main_test.py` (or it could be `app/test_main.py` if you prefer that).

Add the following contents to that file:

```py
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_not_found_404():
    response = client.get("/youcantseeme")
    assert response.status_code == 404
```

What just happened?

- **`from fastapi.testclient import TestClient`** imports a class that allows you to make HTTP requests to your API using the `requests` library
- **`from app.main import app`** imports your application. 
  
  The way to interpret this is `app[./app folder].main[main.py file]:app[variable named app in main.py]`

- **`client = TestClient(app)`** instantiates a new test client, which you'll use in all of your tests

All methods that start with `test_` will be run automatically by `pytest`.


## Run Tests

Run the following command:

```
python -m pytest
```

You should see something like:

```
============================ test session starts ============================
platform darwin -- Python 3.9.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /Users/you/aa/python-curriculum/part-3-testing
plugins: mock-3.6.1, time-machine-2.4.1, anyio-3.4.0
collected 1 item                                                            

app/main_test.py .                                                    [100%]

============================= 1 passed in 0.16s =============================
```

If you want more verbose output, use the `-v` flag:

```
python -m pytest -v
```

Which will show you which individual tests passed / failed:

```
============================ test session starts ============================
platform darwin -- Python 3.9.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /Users/jeff/aa/python-curriculum/part-3-testing/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/jeff/aa/python-curriculum/part-3-testing
plugins: mock-3.6.1, time-machine-2.4.1, anyio-3.4.0
collected 1 item                                                            

app/main_test.py::test_not_found_404 PASSED                           [100%]

============================= 1 passed in 0.16s =============================
```

## Testing Basics

### Testing GET Requests

```py
response = client.get("/path")
```

### Passing headers

You can pass headers by using the `headers` keyword with a dictionary:

```py
response = client.get("/", headers={"X-Forwarded-For": "example.com"})
```

### Passing Query Parameters

Query parameters are whatever come after the `?` in a URL. Take the following URL:

```
http://localhost:8000/items?sort=name&dir=asc
```

There are two query parameters there:
- **sort** => name
- **dir** => asc

Use the `params` keyword argument of the test client to pass query parameters. It will format the URL correctly:

```py
response = client.get("/path", params={"q": "this works"})
```

### Passing Path Parameters

Path parameters include dynamic data in the path itself, for example:

- `http://localhost:8000/items/4`
- `http://localhost:8000/items/5`
- `http://localhost:8000/items/6`

In those examples, the `4`, `5`, and `6` are called Path Parameters.

You don't need anything special to test these:

```py
response = client.get("/items/4")
```

It's common to use string interpolation to generate the path like so:

```py
id = 5
response = client.get(f"/items/{id}")
```

### POSTing JSON Data

The easiest way to post JSON is by using the `json` keyword argument on the test client:

```py
item = {
    "price": "4500",
    "description": "Mic Cable",
}

response = client.post("/items", json=house)
```

### Passing Headers



### Testing Basic Authentication

Basic authentication is a common way of securing endpoints, especially for internal applications or lower environments. You can test basic authentication easily by using the the `auth`:

```py
response = client.get("/admin/items", auth=('some-username', 'some-password'))
```

## Challenges

1. Write 2 tests for the `home` method
   1. Write one test with no `X-Forwarded-For` header
   1. Write one test with an `X-Forwarded-For` header

1. Write 2 tests for the `houses` method
   1. Write one test with no `zip` query parameter
   1. Write one test with a `zip` query parameter

1. Write 2 tests for the `house` method
   1. Write one test with a valid house number and check for a 200 response
   1. Write one test with an invalid house number and check for a 404 response

1. Write a test for the `create_house` method

1. Write 3 tests for the `profile` method
   1. Don't pass any credentials and assert that the response is a 401
   1. Pass incorrect credentials and assert that the response is a 401
   1. Pass correct credentials and assert that the response is a 200
