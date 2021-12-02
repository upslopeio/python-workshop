# FastAPI

> NOTE: you can create a FastAPI app for AA within runway by choosing "Create and App" > "PythonFastAPI"

## Create an empty python project

```
mkdir ~/fastapi-basics
cd ~/fastapi-basics
virtualenv venv
echo venv >> .gitignore
echo __pycache__ >> .gitignore
source venv/bin/activate
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

## Specifying Path Parameters

```python
@app.get("/double/{number}")
def double(number):
    return {"number": number, "doubled": number * 2}
```

Now try accessing that endpoint with a few different URLs:

- http://localhost:8000/double/4
- http://localhost:8000/double/5
- http://localhost:8000/double/6

### Adding Types

Hrm... something doesn't look right 🤔

When you request http://localhost:8000/double/6 it returns the following:

```json
{
    "number": "6",
    "doubled": "66"
}
```

Instead of multiplying the number `6` by 2, it just _string concatenates_ the string `"6"`.

The way to fix that is to add type hints:

```python
@app.get("/double/{number}")
def double(number: int):
    return {"number": number, "doubled": number * 2}
```

Now when you make the request, FastAPI knows to convert the `number` variable to an `int` for you, and you get:

```json
{
    "number": 6,
    "doubled": 12
}
```

FastAPI relies heavily on using types, as you'll see.

Try it out from the live docs as well!

http://localhost:8000/docs#/default/double_double__number__get

> NOTE: there's also another set of generated docs at http://127.0.0.1:8000/redoc

## Challenges for GET requests

First, create a new GET endpoint named `shout` that takes a string and returns a JSON object like with the uppercased string and an exclamation point. For example:

If you go to http://localhost:8000/shout/hello you should see:

```json
{
    "word": "hello", 
    "shout": "HELLO!"
}
```

Then, create a new GET endpoint named `opposite` that takes a boolean and returns a JSON object with the opposite of the value. For example:

If you go to http://localhost:8000/opposite/true you should see:

```json
{
    "value": true, 
    "opposite": false
}
```

> NOTE: you may have to Google how to uppercase a string, perform string concatenation, or use Python conditional statements (if statements).

## POST Requests

Imagine you want to allow users to POST a JSON array of numbers, and return the average of the list. For example:

Input:

```json
[1,3,5,7]
```

Output:

```json
{
    "average": 4
}
```

Your first thought might be something like this:

```py
@app.post("/average")
def average(numbers):
    return {"average": round(sum(numbers)/len(numbers), 2)}
```

The problem here is that FastAPI will think that `list` is a query parameter, and furthermore it will think it's a string.

So you could add this:

```py
@app.post("/average")
def average(numbers: list):
    return {"average": round(sum(numbers)/len(numbers), 2)}
```

Better, but now it thinks you'll be posting a list of strings.

So you need to use Generics to tell FastAPI that it's a list of ints:

```py
@app.post("/average")
def average(numbers: list[int]):
    return {"average": round(sum(numbers)/len(numbers), 2)}
```

> TODO: as an extra challenge, take a moment and fix the divide by zero error that occurs when you send in an empty list `[]`

