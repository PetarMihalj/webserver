import HTTP_util


@HTTP_util.GET("/")
def indexa(req: HTTP_util.Request, resp: HTTP_util.Response):
    resp.status_code = 200
    resp.headers['Content-type'] = 'text/html'

    resp.message = b"""
    <h1 style="text-align: center;">Hello</h1>
    <p style="text-align: center;">This is a picture of a random cat. Please report bugs if you see some.</p>
    <p style="text-align: center;"><img src="/maca_generator" alt="A maca" /></p>
    """


@HTTP_util.GET("/doggo")
def indexa(req: HTTP_util.Request, resp: HTTP_util.Response):
    resp.status_code = 200
    resp.headers['Content-type'] = 'text/html'

    resp.message = b"""
    <h1 style="text-align: center;">You are such a good hacker!</h1>
    <img src="doggo_generator" alt="Random doggo">"""


@HTTP_util.GET("/maca_generator")
def indexa(req: HTTP_util.Request, resp: HTTP_util.Response):
    resp.status_code = 200
    resp.headers['Content-type'] = 'image/jpeg'
    import random
    with open(f"maca{random.randint(1,4)}.jpg", "rb") as file:
        resp.message = file.read()


@HTTP_util.GET("/doggo_generator")
def indexa(req: HTTP_util.Request, resp: HTTP_util.Response):
    resp.status_code = 200
    resp.headers['Content-type'] = 'image/jpeg'

    with open("doggo.png", "rb") as file:
        resp.message = file.read()
