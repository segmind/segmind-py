"""
import requests


api_key = "YOUR API-KEY"
url = "https://api.segmind.com/v1/sd1.5-deepspacediffusion"

# Request payload
data = {
  "prompt": "jwst, nebula, spiral galaxy,mixed colors,outerspace, hyper quality, intricate detail, ultra realistic, maximum detail, foreground focus, instagram, 8k, volumetric light, cinematic, octane render, uplight, no blur, 8k",
  "negative_prompt": "ng_deepnegative_v1_75t,badhandv4, (worst quality:2), (low quality:2), (normal quality:2), lowres,watermark, single color, monochrome",
  "scheduler": "dpmpp_2m",
  "num_inference_steps": 30,
  "guidance_scale": 7,
  "samples": 1,
  "seed": 720692329,
  "img_width": 512,
  "img_height": 768
}

response = requests.post(url, json=data, headers={'x-api-key': api_key})
print(response)

"""

from .T2I import T2I


class DeepSpaceDiffusion(T2I):
    def __init__(self, api_key=None):
        super().__init__(
            url="https://api.segmind.com/v1/sd1.5-deepspacediffusion", api_key=api_key
        )

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "ng_deepnegative_v1_75t,badhandv4, (worst quality:2), (low quality:2), (normal quality:2), lowres,watermark, single color, monochrome",
        samples=1,
        scheduler="dpmpp_2m",
        num_inference_steps=30,
        guidance_scale=7,
        seed=None,
        strength=0.75,
    ):
        return super().generate(
            prompt=prompt,
            negative_prompt=negative_prompt,
            samples=samples,
            scheduler=scheduler,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            seed=seed,
            strength=strength,
        )
