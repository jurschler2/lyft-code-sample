# Lyft Sample Code

This repository is for a small Flask web application consisting of one `POST` request to the route `/test`. This request accepts a JSON object with the key of `'string_to_cut'` with a string value. This request returns a JSON object with the key of `'return_string'` and a new string comprised of every third character of the input string.

#### Example:
```python
{'string_to_cut': 'somestring'} # Input
{'return_string': 'mtn'}        # Output
```

#### Requirements:
- Python 3.7.4

#### Getting Started:

```sh
# install Python dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Running the Flask Server:
```sh
# assuming the venv is active through `source venv/bin/activate`
flask run
```

#### Stopping the Flask Server and Virtual Environment:
```sh
# assuming the venv is active through `source venv/bin/activate`
# assuming flask is running through `flask run`
# Press `control` && `c`
deactivate
```

#### Running Tests:

```sh
# testing the route
source venv/bin/activate
python -m unittest -v
```
```sh
# testing the string cutter
source venv/bin/activate
python -m doctest -v helpers.py
```
