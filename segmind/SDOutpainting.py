import requests
from PIL import Image
from io import BytesIO
from .utils import toB64


class SDOutpainting:
    """
    This API allows you to outpaint images. It is available at https://api.segmind.com/v1/sd1.5-outpaint.
    The API accepts a URL of the image to be processed and returns the "uncropped" image.

    The API accepts the following parameters:
        image = str
            the link to the image
        prompt = str
            Prompts to render
        negative_prompt = str
            prompts to exclude
        scheduler = str
            type of scheduler
        num_inference_steps = int
            Number of denoising steps.
        img_width = int
            Desired result image width
        img_height = int
            Desired result Image Height
        scale = int
            Scale for classifier-free guidance
        strength = int
            Strength controls how much the images can vary
        offset_x = int
            Offset of the init image on the horizontal axis from the left.
        offset_y = int
            Offset of the init image on the vertical axis from the top.
        guidance_scale = float
            Scale for classifier-free guidance
        mask_expand = int
            Mask Expansion in pixels uniformly in all four sides, this sometimes helps the model to achieve more seamless results.
        seed = int
            Seed for image generation. The default value is 1234567.

    The API returns the following:
        PIL Image of the Outpaint.

    It also prints the the number of credits remaining in your account.
    """

    def __init__(self, api_key=None):
        self.url = "https://api.segmind.com/v1/sd1.5-outpaint"
        self.headers = {"x-api-key": f"{api_key}"}
        if api_key is None:
            raise Exception("API Key is required")

    def generate(
        self,
        image,
        prompt,
        negative_prompt="None",
        scheduler="DDIM",
        num_inference_steps=25,
        img_width=1024,
        img_height=1024,
        scale=1,
        strength=1,
        offset_x=256,
        offset_y=256,
        guidance_scale=7.5,
        mask_expand=8,
        seed=1234567,
    ):
        data = {
            "image": toB64(image),
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "scheduler": scheduler,
            "num_inference_steps": num_inference_steps,
            "img_width": img_width,
            "img_height": img_height,
            "scale": scale,
            "strength": strength,
            "offset_x": offset_x,
            "offset_y": offset_y,
            "guidance_scale": guidance_scale,
            "mask_expand": mask_expand,
            "seed": seed,
        }
        response = requests.post(self.url, json=data, headers=self.headers)
        if response.status_code == 200:
            print(
                f"Success! You have {response.headers['X-remaining-credits']} credits remaining"
            )
            return Image.open(BytesIO(response.content))
        else:
            raise Exception(f"Error: {response.status_code}")
