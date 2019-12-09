from flask import Flask, session, request, redirect
import os, logging


app = Flask(__name__, instance_relative_config=True)
app.secret_key = os.urandom(16)
app.url_map.strict_slashes = False


from app import routes
