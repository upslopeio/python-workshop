# Python Data Types and Standard Library

## Strings

**get the length**
```py
sentence = "the brown fox jumped over the fence"
print( len(sentence) )
```

**split a string into a list**
```py
print( sentence.split(" ") )
```

**concatenate two strings together**
```py
result = ""
result = result + "hello"
result += " world"
print(result)
```

**join the elements of a list by a string**
```py
items = ["1", "2", "3"]
result = "_".join(items)
print(result)
```

**substrings**
```py
chars = "hElLo World"
print(chars[0]) # "chars sub zero" or "chars at zero"
print(chars[1:4]) # substring
```

**upper / lower**
```py
print(chars.upper())
print(chars.lower())
```

**for loop**
```py
for char in chars:
    print(char)
```

**does a string contain another string?**
```py
print( "World" in chars )
print( "world" in chars )
```

## Lists

Docs:

- https://www.w3schools.com/python/python_lists.asp
- https://docs.python.org/3/library/functions.html
