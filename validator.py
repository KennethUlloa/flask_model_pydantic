from functools import wraps
from pydantic import BaseModel
from flask import request
import inspect

def create_model(class_: BaseModel):
    content_type = request.headers.get("Content-Type")
    if content_type:
        if "application/json" in content_type:
            return class_(**request.get_json())
        elif "form-data" in content_type:
            return class_(**request.form)


def validate_body(body=None):
    def super_function(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            parameters = inspect.signature(f).parameters
            # Check if body exists
            if "body" in parameters:
                param = parameters["body"]
                # If the parameter is a BaseModel
                if param.annotation == inspect._empty and body != None:
                    model = create_model(body)
                    kwargs["body"] = model
                elif issubclass(param.annotation, BaseModel):
                    model = create_model(param.annotation)
                    kwargs["body"] = model

            return f(*args, **kwargs)
        return decorated_function
    return super_function