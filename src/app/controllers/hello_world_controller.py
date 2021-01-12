from . import *
from flask import request

class HelloWorldController(AppController):
    def get_path(self):
        return "/"
    
    def get_methods(self):
        return ["GET"]
    
    def content(self):
        return {"message": "Hello World :)"}
