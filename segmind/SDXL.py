from .T2I import T2I
import random
import requests
from io import BytesIO
from PIL import Image

"""
"style": "base",
  "samples": 1,
  "scheduler": "UniPC",
  "num_inference_steps": 25,
  "guidance_scale": 8,
  "strength": 0.2,
  "seed": 468685,
  "img_width": 1024,
  "img_height": 1024,
  "refiner": true,
  "high_noise_fraction": 0.8,
  "base64": false


"""

class SDXL(T2I):
    def __init__(self, api_key=None):
        super().__init__(
            url="https://api.segmind.com/v1/sdxl1.0-txt2img", api_key=api_key
        )

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, blurry, bad anatomy, blurred, watermark, grainy, signature, cut off, draft",
        samples=1,
        style="base",
        scheduler="UniPC",
        num_inference_steps=25,
        guidance_scale=8,
        seed=None,
        strength=0.2,
        refiner=True,
        high_noise_fraction=0.8,
        base64=False,
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
            "refiner": refiner,
            "high_noise_fraction": f"{high_noise_fraction}",
            "base64": base64,
        }
        response = requests.post(self.url, json=data, headers=self.headers)
        if response.status_code == 200:
            print(
                f"Success! You have {response.headers['X-remaining-credits']} credits remaining"
            )
            return Image.open(BytesIO(response.content))
        else:
            raise Exception(f"Error: {response.status_code}")
