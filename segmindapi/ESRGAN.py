import requests
from PIL import Image
from io import BytesIO

class ESRGAN:
    """
        This API allows you to enhance and upscale images using the ESRGAN (Enhanced Super-Resolution Generative Adversarial Network) algorithm. It is available at https://api.segmind.com/v1/esrgan.
        The API accepts a URL of the image to be enhanced and returns the enhanced image.
        
        The API accepts the following parameters:

            imageUrl: str
                the link to the image

            scale: int
                factor to scale the image 
                values: 2,4,8 , Default: 2
        
        The API returns the following:
            The enhanced image in PIL.Image Format.
        
        It also prints the the number of credits remaining in your account.
    """

    def __init__(self, api_key : str = None):
        self.url = "https://api.segmind.com/v1/esrgan"
        self.headers = {"x-api-key": f"{api_key}"}
        if api_key is None:
            raise Exception("API Key is required")

    def generate(self, imageUrl, scale = 2):
        data = {
        "scale": scale,
        "imageUrl": imageUrl
    }
        response = requests.post(self.url, json = data, headers = self.headers)
        if response.status_code == 200:
            print(f"Success! You have {response.headers['X-remaining-credits']} credits remaining")
            return Image.open(BytesIO(response.content))
        else:
            raise Exception(f"Error: {response.status_code}")