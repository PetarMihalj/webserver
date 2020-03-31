import HTTP_util


@HTTP_util.GET("/")
def index(req: HTTP_util.Request, resp: HTTP_util.Response):
    resp.status_code = 200
    resp.headers['Content-type'] = 'text/html'

    resp.message = b"""
    <h1 style="text-align: center;">Hello</h1>
    <p style="text-align: center;">This is a picture of a random cat. Please report bugs if you see some.</p>
    <p style="text-align: center;"><img src="/cat_generator" alt="A maca" /></p>
    """


@HTTP_util.GET("/cat_generator")
def maca_gen(req: HTTP_util.Request, resp: HTTP_util.Response):
    resp.status_code = 200
    resp.headers['Content-type'] = 'image/jpeg'
    import random

    if "id" in req.query_dict:
        val = req.query_dict["id"]
        with open(f"maca{val}.jpg", "rb") as file:
            resp.message = file.read()
    else:
        with open(f"maca{random.randint(1,4)}.jpg", "rb") as file:
            resp.message = file.read()
