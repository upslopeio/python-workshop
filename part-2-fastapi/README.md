# FastAPI

> NOTE: you can create a FastAPI app for AA within runway by choosing "Create and App" > "PythonFastAPI"

For this exercise:

1. Fork and clone this empty repository https://github.com/AAInternal/fastapi-sample-application
2. Complete the challenges
3. Commit / Push your changes
4. Open a PR

## Create an empty python project

```
cd ~/fastapi-sample-application

# mac
virtualenv venv
source venv/bin/activate

# windows in Git Bash
python -m virtualenv venv
source venv/Scripts/activate

pip install pipenv
```

## Install FastAPI

```
pipenv install fastapi
pipenv install "uvicorn[standard]"
```

## Add a simple GET endpoint

Create a file named `main.py` with the following contents:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "World"}
```

## Run the app

```
uvicorn main:app --reload
```

Visit http://localhost:8000/ and you should see:

```
{"Hello": "World"}
```

## Hot reloading

Since you specified the `--reload` option when you started the server, any changes you make to your application will be immediately reflected.

Change the app file to return a different result, like so:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "WORLD!!!!"}
```

Go back to your browser and refresh the page. You should see the updated version: `{"Hello": "WORLD!!!!"}`

> NOTE: you do _not_ want to turn this on in production

## Live Documentation

Visit http://localhost:8000/docs - it's like magic! It uses Swagger to auto-generate API documentation for you.

Follow these steps to actually make a request:

![](./images/swagger-1.png)
---
![](./images/swagger-2.png)
---
![](./images/swagger-3.png)
---
![](./images/swagger-4.png)

[Next: Query Parameters](./01-query-parameters.md)