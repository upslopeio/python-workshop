## FastAPI - Specifying Path Parameters

In a URL, path starts with `/` and goes until the `?` or `#`

| URL                                                       | Query String    |
|-----------------------------------------------------------|-----------------|
| http://localhost:8000/houses?for_sale=true&zip_code=10012 | `/houses`       |
| http://localhost:8000/                                    | `/`             |
| http://localhost:8000/customers/12                        | `/customers/12` |

Some parts of a path are _dynamic_ - for example:

- http://localhost:8000/double/4
- http://localhost:8000/double/5
- http://localhost:8000/double/6

In this case, the path is `/double/` followed by some number.

In FastAPI you can handle all of those different paths with a single python function:

```python
@app.get("/double/{number}")
def double(number):
    return {"number": number, "doubled": number * 2}
```

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

## Challenge

First, create a new GET endpoint named `shout` that takes a string and returns a JSON object like with the uppercased string and an exclamation point. For example:

If you go to http://localhost:8000/shout/hello you should see:

```json
{
    "word": "hello",
    "shout": "HELLO!"
}
```

## Challenge

Then, create a new GET endpoint named `opposite` that takes a boolean and returns a JSON object with the opposite of the value. For example:

If you go to http://localhost:8000/opposite/true you should see:

```json
{
    "value": true,
    "opposite": false
}
```

> NOTE: you may have to Google how to uppercase a string, perform string concatenation, or use Python conditional statements (if statements).

## Challenge

Write an endpoint for this url:

http://localhost:8000/houses/ny/10012?under=40000

That returns the following response:

```json
{
    "zip": "10012",
    "under": 40000,
    "state": "NY"
}
```

## Challenge

Write an endpoint for this URL:

http://localhost:8000/customers/123/orders/765?show_details=true&limit=7

That returns the following response:

```
{
    "customer_id": 123,
    "order_id": "765",
    "show_details": true,
    "limit": 7
}
```

## Challenge

Write a URL that would invoke this python method:

```py
@app.get("/users/{user_id}/subscriptions/{subscription_id}/status")
def subscription_status(user_id: int, subscription_id: str):
    return {"ok": True}
```

[Next: Posting JSON Lists](./03-posting-json-lists.md)