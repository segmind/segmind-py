import requests
from PIL import Image
from io import BytesIO
from .utils import toB64

class FaceSwap:
    """
    This API allows you to swap faces in images and is available at https://api.segmind.com/v1/sd2.1-faceswapper.

    The API accepts the following parameters:
        imageUrl: The URL of the image to be processed.
        maskUrl: The URL of the mask to be used for the face swap.
        file_type: The file type of the output image. Default is gif.

    The API returns the following:
        PIL Image with the faces swapped.

    It also prints the number of credits remaining in your account.
    """

    def __init__(self, api_key: str = None):
        self.url = "https://api.segmind.com/v1/sd2.1-faceswapper"
        self.headers = {"x-api-key": f"{api_key}"}
        if api_key is None:
            raise Exception("API Key is required")

    def generate(self, imageUrl: str, maskUrl: str, file_type: str = "gif"):
        data = {
            "input_face_image": toB64(imageUrl),
            "target_face_image": toB64(maskUrl),
            "file_type": file_type,
        }
        response = requests.post(self.url, json=data, headers=self.headers)
        if response.status_code == 200:
            print(
                f"Success! You have {response.headers['X-remaining-credits']} credits remaining"
            )
            return Image.open(BytesIO(response.content))
        else:
            raise Exception(f"Error: {response.status_code}")
