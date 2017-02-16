# Notes Application
This is an insecure demo application for a web security workshop. It's vulnerable to SQL injection, XSS, CSRF, and insecure password storage (plain text).

Meant for educational purposes only, be cautious reusing code in other applications.

## Setup

- Get the code

```
$ git clone https://github.com/bgirardeau/web-security-workshop
$ cd web-security-workshop
```

- (Optional) Create a Python virtualenv

```
$ virtualenv venv
$ source venv/bin/activate
 ```

- Install Python requirements

``` 
$ pip install -r requirements.txt
```

- Create the database

```
$ FLASK_APP=app/app.py flask initdb
```

## Running

    $ python run.py

  Acccess at http://127.0.0.1:8080/

  
