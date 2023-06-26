import requests
from PIL import Image
from io import BytesIO

class SD1_5:
    """
        This API allows you to generate images from images and inpaint images using the SD v1.5. It is available at https://api.segmind.com/v1/sd1.5-img2img and https://api.segmind.com/v1/sd1.5-inpainting.
        The API accepts a prompt and returns the generated image.

        The API accepts the following parameters:
            prompt: str
                Prompt to render, eg. "Stormtrooper giving a lecture"  

            imageUrl: str
                Input reference image URL.

            negative_prompt: str
                Prompts to exclude, eg. "bad anatomy, bad hands, missing fingers"
                Default: None

            samples: int
                Number of output images 
                Default: 1

            scheduler: enum
                Type of scheduler.
                Options: ["DDIM", "DPM Multi", "DPM Single", "Euler a", "Euler", "Heun", "DPM2 a Karras", "DPM2 Karras", "LMS", "PNDM", "DDPM"]
                Default: DDIM

            num_inference_steps: int
                Number of denoising steps.
                Default: 20; Max: 50

            guidance_scale: float
                Scale for classifier-free guidance
                Default: 7.5

            seed: int
                Seed for image generation.
                Default: Random

            strength: float
                How much to transform the reference image
                Default: 1; Range: 0 to 1

            maskUrl: str
                Input mask image URL. Only required for sd1.5-inpainting
    """

    def __init__(self, api_key = None):
        self.headers = {"x-api-key": f"{api_key}"}
        if api_key is None:
            raise Exception("API Key is required")    

    def generate(self, prompt : str, imageUrl, maskUrl = None, negative_prompt : str = "nude, disfigured, blurry", samples = 1, scheduler = "DDIM", num_inference_steps = 50, guidance_scale = 10.5, seed = 98877465625, strength = 0.75):
        data = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "samples": f"{samples}",
        "scheduler": scheduler,
        "num_inference_steps": f"{num_inference_steps}",
        "guidance_scale": f"{guidance_scale}",
        "seed": f"{seed}",
        "strength": f"{strength}",
        "imageUrl": imageUrl
    }
        if maskUrl:
            data["maskUrl"] = maskUrl
            url = "https://api.segmind.com/v1/sd1.5-inpainting"
        else:
            url = "https://api.segmind.com/v1/sd1.5-img2img"
        response = requests.post(url, json = data, headers = self.headers)
        if response.status_code == 200:
            print(f"Success! You have {response.headers['X-remaining-credits']} credits remaining")
            return Image.open(BytesIO(response.content))
        else:
            raise Exception(f"Error: {response.status_code}")