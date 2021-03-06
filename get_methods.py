import HTTP_util

"""
This module contains all bindings to specific paths.
You can specify multiple modules of this sort in order to better modularize your project.

All such module names should be given as arguments on server startup. 
"""


@HTTP_util.GET("/")
def index(req: HTTP_util.Request, resp: HTTP_util.Response):
    resp.status_code = 200
    resp.headers['Content-type'] = 'text/html'

    resp.message = b"""
    <h1 style="text-align: center;">Hello</h1>
    <p style="text-align: center;">This is a picture of a random cat. Please report bugs if you see some.</p>
    <p style="text-align: center;">Reload the page to see more</p>
    <p style="text-align: center;"><img src="/cat_generator" alt="A cat" /></p>
    """


@HTTP_util.GET("/cat_generator")
def maca_gen(req: HTTP_util.Request, resp: HTTP_util.Response):
    """
    Used to generate a random cat picture.
    Can be used in the form: http://127.0.0.1:8080/cat_generator?id=3 to generate a specific cat.
    """
    resp.status_code = 200
    resp.headers['Content-type'] = 'image/jpeg'
    import random

    if "id" in req.query_dict:
        val = req.query_dict["id"]
        with open(f"pictures/cat{val}.jpg", "rb") as file:
            resp.message = file.read()
    else:
        with open(f"pictures/cat{random.randint(1,4)}.jpg", "rb") as file:
            resp.message = file.read()
