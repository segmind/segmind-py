import requests
from base64 import b64encode


def toB64(imgUrl):
    return str(b64encode(requests.get(imgUrl).content))[2:-1]
