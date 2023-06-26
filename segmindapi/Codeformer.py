import requests
from PIL import Image
from io import BytesIO

class Codeformer:
    """
        This API harnesses the power of CodeFormer, a robust face restoration algorithm designed specifically for old photos or AI-generated faces, and is available at https://api.segmind.com/v1/codeformer
        
        The API accepts a URL of the image to be processed and returns the image with the background removed.

        The API accepts the following parameters:
            imageUrl = str
                the link to the image

            scale = int
                The final upsampling scale of the image

            fidelity = int
                level of fidelity or quality desired for the generated image.
                values between 0 to 1.

            bg = int
                refers to the enhancement of the background present in the image.
                values between 0 to 1.

            face = int
                refers to the enhancement of the face present in the image.
                values between 0 to 1.

            base64 = str
                if the image is in base64 format or not.
                values: "true" or "false"
                
        The API returns the following:
            PIL Image with the face restored.

        It also prints the the number of credits remaining in your account.
    """
    def __init__(self, api_key = None):
        self.url = "https://api.segmind.com/v1/codeformer"
        self.headers = {"x-api-key": f"{api_key}"}
        if api_key is None:
            raise Exception("API Key is required")
    
    def generate(self, image_url, scale = 1, fidelity = 0.5, bg = 1, face = 1, base64 = "true"):
        data = {
        "scale": scale,
        "fidelity": fidelity,
        "bg": bg,
        "face": face,
        "imageUrl": image_url,
        "base64": base64
    }
        response = requests.post(self.url, json = data, headers = self.headers)
        if response.status_code == 200:
            print(f"Success! You have {response.headers['X-remaining-credits']} credits remaining")
            return Image.open(BytesIO(response.content))
        else:
            raise Exception(f"Error: {response.status_code}")
