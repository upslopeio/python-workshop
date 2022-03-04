# Python Introduction

> NOTE: the following assumes you are running on a unix-esque terminal. If you are windows, either use WSL2 Ubuntu, or Git Bash.

## Check Your Version

Which version of Python do you have?

```
python --version
```

Most systems have Python 2 installed by default. You may _also_ have Python 3 installed, but it might be named `python3`:

```
python3 --version
```

**Alternately** you might have Python named `python2`:

```
python2 --version
```

## Download Python 3 (if you need it)

https://www.python.org/downloads/

If you are on a mac, you can also run:

```
brew install python
```

## Virtual Environments

You might have different projects that rely on different Python versions:

![](./diagrams/multiple-projects.drawio.svg)

You can install python packages with a tool called `pip` (which might be `pip3` on your machine).

By default `pip` will install all of your packages into the same directory on your computer, using whatever the current Python version is.

This can, in some cases, cause issues that will slow down your development. So it's customary to create _virtual environments_ using `virtualenv`.

A `virtualenv` is a folder that contains:

- a specific python executable
- all packages you installed with `pip`

### Install Virtualenv

> NOTE: make sure you are in Python 3 for all of these examples.

```
pip3 install virtualenv
# or maybe...
# pip install virtualenv
```

### Create a Project Folder

```
mkdir example
cd example
```

### Create a Virtual Environment

```
virtualenv venv
# or for windows
# python3 -m virtualenv venv
```

This creates a folder named `venv` that has files like this:

```
venv
├── bin
│   ├── activate
│   ├── activate.csh
│   ├── activate.fish
│   ├── activate.nu
│   ├── activate.ps1
│   ├── activate_this.py
│   ├── deactivate.nu
│   ├── pip
│   ├── pip-3.9
│   ├── pip3
│   ├── pip3.9
│   ├── python -> /usr/local/opt/python@3.9/bin/python3.9
│   ├── python3 -> python
│   ├── python3.9 -> python
│   ├── wheel
│   ├── wheel-3.9
│   ├── wheel3
│   └── wheel3.9
├── lib
│   └── python3.9
└── pyvenv.cfg
```

It basically installed a new version of Python inside your project folder.

You'll always want to add `venv` to `.gitignore`, which you can do like this:

```
echo venv >> .gitignore
```

Now that it's installed, how do you use it?

### Activate the environment

You can tell your terminal to use this `venv` version of Python like so:

```
# mac / unix
source venv/bin/activate

# windows bash
./venv/Scripts/activate
```

You'll know that your terminal window is activated when you see `(venv)` in your terminal prompt:

```
(venv) ➜  example git:(main) ✗ 
```

Did it work? Run `which python` and you'll notice that it points to the Python version in your `venv` folder:

```
which python
# /Users/you/example/venv/bin/python
which pip
/Users/you/example/venv/bin/pip
```

### Pythons Everywhere!!

Your computer may have one or more Python versions installed:

1. Python 2 (either `python` or `python2`)
1. Python 3 (either `python` or `python3`)

Your computer also has `pip` installed (for example `pip`, `pip2` or `pip3`).

Once you **activate** a `virtualenv` you get standard naming:

1. `python` always points to the correct python version for the project
1. `pip` always points to the correct python version for the project

![](./diagrams/virtualenv.drawio.svg)

## Hello World

Every time you create a python script, you are creating a `module`.  Let's create one:

```
echo "print('Hello World')" > hello.py
```

And run the file:

```
python -m hello
```

What does the `-m` flag do? According to `python --help` it allows you to:

> run library module as a script

So it:

1. finds the module (aka file) named `hello.py`
1. executes the code from top to bottom

### Add `__pycache__` to gitignore

When you run a python script with `-m` it creates a folder named `__pycache__` so let's add that to `.gitignore`:

```
echo __pycache__ >> .gitignore
```

## Installing Packages

There are a few ways to manage dependencies in your application:

**Manually Install (bad)**

You can manually install packages with `pip install <package>`. 

This is the worst option as it means that every developer has to manually download each package on their own machine and manually ensure the versions are correct.

**Use requirements.txt (better)**

You can list your requirements in a `requirements.txt` file like so:

```
requests==2.26.0
six==1.16.0
urllib3==1.26.7
```

Then you can install all the dependencies at once with a single command:

```
pip install -r requirements.txt
```

This is a little better than manually adding packages, but has a few problems:

- you need to specify your dev and prod dependencies in different files
- you can't lock down the versions of sub-dependencies of packages, so you can still get slightly different results in different environments

**Use pipenv**

The best solution is to use a [`Pipfile`](https://github.com/pypa/pipfile). That's what we'll be doing here.

https://pipenv.pypa.io/en/stable/

### Install `pipenv`

> NOTE: you'll do this from _within_ your activated `virtualenv`

```
pip install pipenv
```

### Install a package with pipenv

You can install packages using `pip`, but if you instead use `pipenv` you get some extra benefits.

To install a library run:

```
pipenv install requests
```

What just happened? `pipenv` did the following:

1. created file named `Pipfile` that has the following contents:

    ```
    [[source]]
    url = "https://pypi.org/simple"
    verify_ssl = true
    name = "pypi"

    [packages]
    requests = "*"

    [dev-packages]

    [requires]
    python_version = "3.9"
    ```

1. Downloaded the `requests` package to your `venv` folder

1. created a file named `Pipfile.lock` which contains a list of all the sub-dependencies of `requests` and their exact versions

## Importing

You can import an entire other package like this:

```
import os
```

You can also import individual parts of a package like so:

```
from os import getenv
```

You can import from the [python standard library](https://docs.python.org/3/library/) or from packages you downloaded with `pipenv`

### Examples

To demonstrate, run the following examples:

First, create a new file called `print-env-1.py` like so:

```
cat <<EOF > print-env-1.py
from os import environ

print(environ)
EOF
```

And run it like so:

```
python -m print-env-1.py
```

You should see your shell's environment variables printed on the screen.

Next, create a file called `print-env-2.py` like so:

```
cat <<EOF > print-env-2.py
import os

print(os.environ)
EOF
```

And run it like so:

```
python -m print-env-2.py
```

## Challenge: Download a Web Page

1. Create a python module named `download-example`
1. Install the requests library with `pipenv` (if you haven't already)
1. Import `requests`
1. Follow the documentation on the [requests site](https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request) and make a request to `http://example.com`
1. Print the HTML of the page (hint, use `r.text`)
1. Run the file

## Next Steps

Go to [LearnPython.org](https://www.learnpython.org/en/Variables_and_Types) and learn more about the Python language!