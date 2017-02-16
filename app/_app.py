# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)
app.config.from_object('app.default_config')
app.config.from_envvar('APP_CONFIG', silent=True)
