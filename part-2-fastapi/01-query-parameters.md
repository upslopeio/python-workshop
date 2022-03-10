# FastAPI - Query Parameters

In a URL, the query parameters come after the `?` - for example:

| URL                                                       | Query String                  |
|-----------------------------------------------------------|-------------------------------|
| http://localhost:8000/houses?for_sale=true&zip_code=10012 | ?for_sale=true&zip_code=10012 |

To write an endpoint that can read a querystring variable, 

```py
@app.get("/houses")
def double(for_sale: bool):
    return {"house is for sale?": for_sale}
```

How does it work?

- FastAPI reads your method signature `def double(for_sale: bool):` and sees a parameter named `for_sale`
- FastAPI sees that there's no path parameter named `for_sale`
- FastAPI parses the querystring for a query parameter named `for_sale` and see that it's the string "true"
- FastAPI sees that your parameter is of type `bool` so it converts `"true"` to `True`
- FastAPI calls your method like so `doubld(True)`

## Challenge

Write an endpoint for this url:

http://localhost:8000/issues?open=true&limit=10&label=bug

That returns the following response:

```json
{
    "open": true,
    "limit": 10,
    "label": "bug"
}
```

## Challenge

Write an endpoint for this url:

http://localhost:8000/posts?author=Hank&published=false

That returns the following response:

```json
{
    "author": "Hank",
    "published": false
}
```

## Challenge

Write an HTTP request (that would be valid to run in a `.http` file) for the given code:

```py
@app.get("/to-the-power-of")
def exponentiate(base: int, exponent: int):
    return {"result": base ** exponent}
```

> NOTE: `base` and `exponent` can be any valid values

[Next: Path Parameters](./02-path-parameters.md)