from PIL import Image
import requests
from io import BytesIO
from base64 import b64encode
from .utils import toB64


class QRGenerator:
    """
    This API allows you to transform text descriptions into corresponding image representations and is available at https://api.segmind.com/v1/qrsd1.5-txt2img.

    The API accepts the following parameters:
        prompt: The text description of the image to be generated.
        negative_prompt: The text description of the image to be avoided.
        scheduler: The scheduler to be used for the generation. The default value is dpmpp_2m.
        num_inference_steps: The number of inference steps to be used for the generation. The default value is 25.
        guidance_scale: The guidance scale to be used for the generation. The default value is 7.5.
        control_scale: The control scale to be used for the generation. The default value is 1.9.
        control_start: The control start to be used for the generation. The default value is 0.19.
        control_end: The control end to be used for the generation. The default value is 1.
        samples: The number of images to be generated. The default value is 1.
        seed: The seed to be used for the generation. The default value is 1234567.
        size: The size of the image to be generated. The default value is 768.
        qr_text: The text to be encoded in the QR code. The default value is www.segmind.com.
        invert: The invert to be used for the generation. The default value is False.
        base64: The base64 to be used for the generation. The default value is False.

    The API returns the following:
        The generated image.

    It also prints the number of credits remaining in your account.

    """

    def __init__(self, api_key=None):
        self.url = "https://api.segmind.com/v1/qrsd1.5-txt2img"
        self.headers = {"x-api-key": f"{api_key}"}
        if api_key is None:
            raise Exception("API Key is required")

    def generate(
        self,
        prompt,
        negative_prompt="None",
        scheduler="dpmpp_2m",
        num_inference_steps=25,
        presets="presetOne",
        guidance_scale=7.5,
        control_scale=1.8,
        control_start=0.19,
        control_end=1,
        samples=1,
        seed=1234567,
        size=768,
        qr_text="www.segmind.com",
        invert=False,
        base64=False,
    ):
        data = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "scheduler": scheduler,
            "num_inference_steps": f"{num_inference_steps}",
            "presets": presets,
            "guidance_scale": f"{guidance_scale}",
            "control_scale": control_scale,
            "control_start": control_start,
            "control_end": control_end,
            "samples": samples,
            "seed": seed,
            "size": size,
            "qr_text": qr_text,
            "invert": invert,
            "base64": f"{base64}",
        }
        response = requests.post(self.url, json=data, headers=self.headers)
        if response.status_code == 200:
            print(
                f"Success! You have {response.headers['X-remaining-credits']} credits remaining"
            )
            return Image.open(BytesIO(response.content))
        else:
            raise Exception(f"Error: {response.text}")
