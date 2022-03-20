## FastAPI - POSTing JSON Objects

In real life, you'll need need to parse more complex objects. The way to do that in FastAPI is via [Pydantic Models](https://pydantic-docs.helpmanual.io/).

For example, let's say we wanted to POST this object to our API:

```json
{
    "firstName": "Some",
    "lastName": "User",
    "address": {
        "city": "New York",
        "state": "NY"
    }
}
```

First, import `BaseModel` from `pydantic`:

```py
from pydantic import BaseModel
```

Next, declare your types:

```py
class Address(BaseModel):
    city: str
    state: str


class Person(BaseModel):
    firstName: str
    lastName: str
    address: Address
```

Finally, build your endpoint:

```py
@app.post("/welcome")
def average(person: Person):
    return {"greeting": f"Hello {person.firstName} {person.lastName}! How's {person.address.city}?"}
```

The API docs now give great documentation:

![](./images/welcome-1.png)

And if you post this JSON body:

```json
{
  "firstName": "Example",
  "lastName": "User",
  "address": {
    "city": "New York",
    "state": "NY"
  }
}
```

Then you should see:

```json
{
  "greeting": "Hello Example User! How's New York?"
}
```

FastAPI parses the JSON, and creates python objects for you that match the schema you defined in the Pydantic model!

## What's happening under the hood?

Imagine you have the following app:

```py
class VoterData(BaseModel):
    firstName: Optional[str]
    lastName: str
    age: int
    voted: bool


class VoterResponse(BaseModel):
    fullName: str
    eligible: bool
    data: VoterData


@app.post("/voter-data", response_model=VoterResponse)
def voter_data(data: VoterData):
    return {
        "fullName": data.firstName + " " + data.lastName,
        "eligible": not data.voted,
        "data": data
    }
```

What does FastAPI do when you make a POST request to `/voter-data`?

- parses the HTTP request
- looks at the VERB of the HTTP request (`POST`)
- looks at the path (liek `/voter-data`)
- looks at the decorators to see if there is a mapping for `@app.[VERB](PATH)`
- sees that there is one, and it points to the `voter_data` function
- looks at `voter_data` parameters
  - sees 1 parameter named `data`
  - there's no `{data}` in the path - so it's not a path parameter
  - it sees that data is a non-scalar type, so it guesses it's a body and parses the body
- parsed the JSON from the post request
- instantiated a `VoterData` class
- mapped the values of the JSON payload to the properties of the class
- called the `voter_data` method and passed the instance of the `VoterData` class to the method


## Camel vs Snake Case

Camel case has no spaces, and capitalizes the first letter of every word, like `firstName`.

Snake case separates words by underscores, and does not capitalize anything, like `first_name`.

Python uses snake case. JSON typically uses camel case. So... how do you choose?

You don't have to! Here's an excellent article on how to get the best of both worlds:

https://medium.com/analytics-vidhya/camel-case-models-with-fast-api-and-pydantic-5a8acb6c0eee

## Full Example App

Here's a full example application:

```py
from fastapi import FastAPI
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str


class Person(BaseModel):
    firstName: str
    lastName: str
    address: Address


app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "WORLD!!"}


@app.get("/double/{number}")
def double(number: int):
    return {"number": number, "doubled": number * 2}


@app.post("/average")
def average(numbers: list[int]):
    return {"average": round(sum(numbers)/len(numbers), 2)}


@app.post("/welcome")
def average(person: Person):
    return {"greeting": f"Hello {person.firstName} {person.lastName}! How's {person.address.city}?"}
```

## Summary

To define what type of data a user should send to your app:

1. define a class that inherits from pydantic BaseModel
2. define your json properties as fields
3. pass that type into your FastAPI endpoint

To define what type of data your app will return to a user

1. define a class that inherits from pydantic BaseModel
2. define your fields
3. pass that type into the `response_model` argument of the decorator (`@app.get` etc...)

## Challenge

In your FastAPI application create an endpoint that responds
to a POST to /address that takes this JSON object:

```json
{
    "city": "New York",
    "state": "NY",
    "zip": "12345"
}
```

and returns `{"formatted": "New York, NY 12345"}`

## Challenge

In your FastAPI application create an endpoint that responds
to a POST to /personal-address that takes this JSON object:

```json
{
    "firstName": "Tom",
    "active": true,
    "address": {
        "city": "New York",
        "state": "NY",
        "zip": "12345"
    }
}
```

and returns 

```json
{"formatted": "Tom (active) - New York, NY 12345"}
```

OR if it's inactive:

```json
{"formatted": "Tom (inactive) - New York, NY 12345"}
```

## Pydantic Schema Challenge

From https://docs.github.com/en/rest/reference/codes-of-conduct

Write a pydantic model that would parse this JSON:

```json
 {
  "key": "contributor_covenant",
  "name": "Contributor Covenant",
  "url": "https://api.github.com/codes_of_conduct/contributor_covenant",
  "body": "some long text here",
  "html_url": "http://contributor-covenant.org/version/1/4/"
}
```

## Pydantic Shchema Challenge

From https://docs.github.com/en/rest/reference/codes-of-conduct

Write a pydantic modelt hat would parse this JSON:

```json
[
  {
    "key": "citizen_code_of_conduct",
    "name": "Citizen Code of Conduct",
    "url": "https://api.github.com/codes_of_conduct/citizen_code_of_conduct",
    "html_url": "http://citizencodeofconduct.org/"
  },
  {
    "key": "contributor_covenant",
    "name": "Contributor Covenant",
    "url": "https://api.github.com/codes_of_conduct/contributor_covenant",
    "html_url": "https://www.contributor-covenant.org/version/2/0/code_of_conduct/"
  }
]
```

