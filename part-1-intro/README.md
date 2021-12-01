# Python Introduction

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
source venv/bin/activate
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

## Pythons Everywhere!!

Your computer may have or more Python versions installed:

1. Python 2 (either `python` or `python2`)
1. Python 3 (either `python` or `python3`)

Your computer also has `pip` installed (for example `pip`, `pip2` or `pip3`).

Once you **activate** a `virtualenv` you get standard naming:

1. `python` always points to the correct python version for the project
1. `pip` always points to the correct python version for the project

![](./diagrams/virtualenv.drawio.svg)
