# Python Backend Template

This is a template for writing backends in Python using the following technologies:

- Flask (Routes)
- SQLAlchemy (ORM)

This includes a basic "hello, world!" endpoint along with a user and session model

### virtual env

```python
virtualenv venv
. venv/bin/activate
pip3 install -r requirements.txt
```

### running the server

To run the server, run:

```
python src/run.py
```

The hello world endpoint can be found at http://127.0.0.1:5000/api/
