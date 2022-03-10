# Dictionary

Key / value pairs.

- key can be anything

## What's the purpose of dictionaries

Dictionaries allow you to associate names with pieces of data, and look up those pieces of data by name.

Dictionary lookup is very fast (Constant Time).

```py
person = {
    "first_name": "Jeff"
}

person["first_name"] # <= super fast lookup, 
                     # doesn't get slower as the dict gets bigger
```

https://www.youtube.com/watch?v=shs0KM3wKv8

## Common dictionary operations

Creating `dict`:

```py
foo = {
    "key": "value"
}
```

## Getting things out of a dictionary

If we know the key is there:

```py
foo["key"] # => returns the value
```

If we think the key might not be there, use `get`:

```py
print(  person.get("last_name")  )
print(  person.get("last_name", "<enter last name>")  )
```

## Putting things in a dict

```py
person = {}

person["first_name"] = "some value"
```

## See if a dict has a key

```py
if "last_name" in person:
    print(person["last_name"])
```

## Loop over all key/value pairs

```py
person = {
    "first_name": "Jeff",
    "last_name": "Dean"
}

for key, value in person.items():
    print(key)
    print(value)
```

## Getting keys/values

```py
person = {
    "first_name": "Jeff",
    "last_name": "Dean"
}

print(person.keys())
print(person.values())
```

## Dictionaries in memory

Assume you had the following dictionary:

```py
{
    "name": "Charles",
    "age": 27,
    "employed": True
}
```

You could represent that as a table, like so:

![](https://www.plantuml.com/plantuml/png/SoWkIImgoIhEp-Egvb800gMynDnK9Ii59UUCnAASr68b7OXmOZf8rCWSoatDBSZ9hqnD0OgL59McSjLoEQJcfO3C0G00)

### Dictionaries with lists

If a dictionary property points to a list, the list is a separate item in memory:

```py
{
    "name": "Charles",
    "age": 27,
    "employed": true,
    "jobs": [
        "carpenter", 
        "plumber"
    ]
}
```

![](https://www.plantuml.com/plantuml/png/SoWkIImgoIhEp-Egvb800gMynDnK9Ii59UUCnAASr68b7OXmOZf8rCWSoatDBSZ9hqnD0OgL59McGaMpyfEAWIBHIic9HGMfUIMfHKew2ae5EQMvIK1cB5SjbqDgNWh8DW00)

### Dictionaries with lists

If a dictionary property points to another dictionary, it would look like this:

```py
{
    "name": "Charles",
    "age": 27,
    "employed": true,
    "address": {
        "city": "New York",
        "state": "NY",
        "zip": "10012"
    }
}
```

![](https://www.plantuml.com/plantuml/png/SoWkIImgoIhEp-Egvb800gMynDnK9Ii59UUCnAASr68b7OXmOZf8rCWSoatDBSZ9hqnD0OgL59McmXIbf1Ib5XS31I66WGMJCqigGGRwfPOhHEONPIlf8EI0jfUaWYKZaOMhCWj0WeO61eP6Ic3XMgvQBYw7rBmKa5C1)

## Turtles all the way down

```py
{
    "name": "Charles",
    "age": 27,
    "employed": true,
    "jobs": [
        {
            "title": "carpenter",
            "address": {
                "city": "New York",
                "state": "NY",
                "zip": "10012"
            }
        },
        {
            "title": "plumber",
            "address": {
                "city": "Bronx",
                "state": "NY",
                "zip": "10038"
            }
        }
    ]
}
```

![](https://www.plantuml.com/plantuml/png/fL5DQuGm4BtdLyYSSr1xQEb9sdllKdg8PcYrCGcJaTOM__kQh0YokopilbFUnpmUf0giYFlWhFWNsGAmQa1upk3rIv710F8egy-ebeyhnS4RDw5UDAOHLxLtJLYKzyWIKkS6u8vDAcyLURIC17AVK5eJXbYoFqrcs_4Khz_m9wiTVOCypGHMZ2bKdxF_EX_D8i-B4dRslB5PNjtlpJWqDwv_8MT_xvh-y7HnUdfzY5bKQ7NyrWC0)