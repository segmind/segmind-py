import requests
from PIL import Image
from io import BytesIO
import random


class T2I:
    def __init__(self, url, api_key=None):
        self.headers = {"x-api-key": f"{api_key}"}
        self.url = url
        if api_key is None:
            raise Exception("API Key is required")

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "nude, disfigured, blurry",
        samples=1,
        scheduler="dmpp_2m",
        num_inference_steps=25,
        guidance_scale=7,
        seed=None,
        strength=0.75,
        style = "base",
        high_noise_fraction = 0.8
    ):
        if not seed:
            seed = random.randint(0, 1000000000)
        data = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "samples": f"{samples}",
            "scheduler": scheduler,
            "img_height": 1024,
            "img_width": 1024,
            "num_inference_steps": f"{num_inference_steps}",
            "guidance_scale": f"{guidance_scale}",
            "seed": f"{seed}",
            "strength": f"{strength}",
            "style":style,
            "high_noise_fraction":f"{high_noise_fraction}"
        }
        response = requests.post(self.url, json=data, headers=self.headers)
        if response.status_code == 200:
            print(
                f"Success! You have {response.headers['X-remaining-credits']} credits remaining"
            )
            return Image.open(BytesIO(response.content))
        else:
            raise Exception(f"Error: {response.status_code}")
