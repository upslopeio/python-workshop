# Environment Variables

## Setting

There are several ways you can set env variables:

1. At the machine level
    - in a `.bashrc` file or `.zshrc` file
    - by using the Windows `Environment Variables` dialog
1. For one terminal session
    - `export FOO=bar`
1. For one command
    - `FOO=bar uvicorn main:app --reload`

## Reading from the terminal

There are two ways you can see environment variables from your terminal:

1. By running the `env` command, which will list them all
1. By echoing the variable with a dollar sign: `echo $FOO`

## Reading from Python

```py
import os

os.environ          # <= returns a dictionary of all environment variables
os.environ["FOO"]   # <= gets the value of the FOO variable. Raises a key error if FOO is not defined

os.getenv("FOO")        # <= gets the value of the FOO variable. Returns None if FOO is not defined
os.getenv("FOO")        # <= gets the value of the FOO variable. Returns None if FOO is not defined
os.getenv("FOO", "2")   # <= gets the value of the FOO variable. Returns "2" if FOO is not defined
```

Since `os.environ` is just a dictionary, you can also set properties in python:

```py
import os

os.environ["FOO"] = "bar"
```

## Dealing with environment variables in your app

When you write code on multiple applications on your machine it can be annoying to manage them. Some options are:

- You can add them at the machine level:
    - Not ideal because what if two different apps have the same variable names (like `HTTP_PASSWORD`) but different values?
- You can write a shell script that sets environment variables and then `source` that script in every tab
    - This is kind of annoying because you have to remember to `source` the file in every tab you open
- You can type out the environment variables whenever you start a command
    - This is kind of awful because it's a ton of typing once you have multiple environment variables

The solution? `dotenv`

https://pypi.org/project/python-dotenv/

Install the `dotenv` package (ideally you'd be using `pipenv`):

```
pipenv install dotenv
```

If you are not using `pipenv` then put `dotenv` in your `requirements.txt` file and then run:

```
pip install -r requirements.txt
```

Then write a file named `.env` and put environments variables in (see docs for examples).

## Using dotenv with uvicorn

If you have `dotenv` installed, then you can tell `uvicorn` to use it:

```
uvicorn main:app --reload --env-file=.env
```
