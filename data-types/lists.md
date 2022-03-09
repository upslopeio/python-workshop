# Lists

**turn a string into a list**
```py
sentence = "the brown fox jumped over the fence"
words = sentence.split(" ")
```

**access the element of a list**
```py
print(words[1])
```

**sublist**
```py
a = [1,2,3,4,5]
print(a[2:4])
```

**add to a list**
```py
a = []
a.append(4)
a.append(5)
print(a)
```

**concatenate two lists**
```py
a = [1,2]
b = [3,4]
print(a + b)
print(a)
print(b)
```

**extend**
```py
a = [1,2]
b = [3,4]
a.extend(b)
print(a)
print(b)
```

**get the index of something in the list**
```py
groceries = ["milk", "eggs", "cheese"]
print( groceries.index("eggs") )
```

**sort / sorted**
```py
groceries = ["milk", "eggs", "cheese"]
groceries.sort()
print ( groceries )
```

**TIP: prefer sorted over .sort() in most cases**
```py
groceries = ["milk", "eggs", "cheese"]
result = sorted(groceries)
print ( result )
print ( groceries )
```

**reverse / reversed**
```py
a = [1,2,3]
print(reversed(a))
print(list(reversed(a)))
```

**for loops**
```py
for word in words:
    print( word )
```

**for loop with the index**
```py
for i, word in enumerate(words):
    print( f"{word} at index {i}" )
```

**for loop just the number**
```py
for index in range(len(words)):
    print( index )
```

**comprehension**
```py
lengths = [len(word) for word in words]
print("lengths")
print(lengths)
```

# Performance vs Readability

```py
# slower / uses more memory
def difference_in_ages(ages):
    sorted_ages = sorted(ages)
    oldest = sorted_ages[-1]
    youngest = sorted_ages[0]
    return youngest, oldest, oldest - youngest

# faster / uses less memory
def difference_in_ages(ages):
    oldest = max(ages)
    youngest = min(ages)
    return youngest, oldest, oldest - youngest

# fastest / lowest memory / hardest to read    
def difference_in_ages(ages):
    max = None
    min = None
    for num in ages:
        if max is None or num > max:
            max = num
        if min is None or num < min:
            min = num
    
    return min, max, max - min
```
