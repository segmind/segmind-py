import requests
from PIL import Image
from io import BytesIO

class SAM:
    """
        This API allows you to generate Segmentation Masks using SAM (Segment Anything Model) and is available at https://api.segmind.com/v1/sam-img2mask.

        The API accepts the following parameters:
            imageUrl: The URL of the image to be processed.

        The API returns the following:
            The segmentation mask of the image.

        It also prints the number of credits remaining in your account.      
    """
    def __init__(self, api_key : str = None):
        self.url = "https://api.segmind.com/v1/sam-img2img"
        self.headers = {"x-api-key": f"{api_key}"}
        if api_key is None:
            raise Exception("API Key is required")
    
    def generate(self, imageUrl : str):
        data = {
        "imageUrl": imageUrl
    }
        response = requests.post(self.url, json = data, headers = self.headers)
        if response.status_code == 200:
            print(f"Success! You have {response.headers['X-remaining-credits']} credits remaining")
            return Image.open(BytesIO(response.content))
        else:
            raise Exception(f"Error: {response.status_code}")