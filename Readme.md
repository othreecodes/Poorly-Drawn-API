# Poorly Drawn API

# Installing
```sh
$ git clone git@github.com:othreecodes/Poorly-Drawn-API.git
$ cd Poorly-Drawn-API
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ gunicorn poorlydrawn.config.wsgi:application # run with gunicorn

```