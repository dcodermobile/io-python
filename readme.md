# IO-PYTHON
<p>Python lib for dcoder io</p>

<br />

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python3](https://www.python.org/downloads/) and [PIP](https://pypi.org/project/pip/) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone 

# Go into the repository
$ cd io-python

# Compiling setup file
$ python setup.py sdist bdist_wheel

# Installing the whl
$ pip install dcoderio-<=version-no=>-py3-none-any.whl

# Pushing the code into test.pypi.org
$ python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

# Pushing the code into pypi.org
$ python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```
