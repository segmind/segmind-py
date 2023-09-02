import requests
from PIL import Image
from io import BytesIO


class BackgroundRemoval:
    """
    This API allows you to remove the background from an image. It is available at https://api.segmind.com/v1/bg-removal.
    The API accepts a URL of the image to be processed and returns the image with the background removed.

    The API accepts the following parameters:
        imageUrl = str
            the link to the image

    The API returns the following:
        PIL Image with the background removed.

    It also prints the the number of credits remaining in your account.
    """

    def __init__(self, api_key=None):
        self.url = "https://api.segmind.com/v1/bg-removal"
        self.headers = {"x-api-key": f"{api_key}"}
        if api_key is None:
            raise Exception("API Key is required")

    def generate(self, imageUrl):
        data = {"method": "object", "imageUrl": imageUrl}
        response = requests.post(self.url, json=data, headers=self.headers)
        if response.status_code == 200:
            print(
                f"Success! You have {response.headers['X-remaining-credits']} credits remaining"
            )
            return Image.open(BytesIO(response.content))
        else:
            raise Exception(f"Error: {response.status_code}")
