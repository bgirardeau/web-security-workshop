# Notes Application
This is an insecure demo application for the web security workshop.

You can try it out at http://45.55.21.119:8080/. Don't use any sensitive information or passwords!

## Setup

 1. Get the code

```
$ git clone https://github.com/bgirardeau/web-security-workshop
$ cd web-security-workshop
```

2. (Optional) Create a Python virtualenv

```
$ virtualenv venv
$ source venv/bin/activate
 ```

3. Install Python requirements

``` 
$ pip install -r requirements.txt
```

4. Create the database

```
$ FLASK_APP=app/app.py flask initdb
```

## Running

    $ python run.py

  Acccess at http://127.0.0.1:8080/

  
