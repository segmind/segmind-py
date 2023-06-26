import requests
from PIL import Image
from io import BytesIO

class SD2_1:
    """
    SDT2I is a class that allows you to generate images from text using the Segmind API.
    The API is available at https://api.segmind.com/v1/sd2.1-txt2img.

    The API accepts the following parameters:

        prompt: str
            Prompt to render, eg. "Stormtrooper giving a lecture"  

        negative_prompt: str
            Prompts to exclude, eg. "bad anatomy, bad hands, missing fingers"
            Default: None

        samples: int
            Number of output images 
            Default: 1

        scheduler: str
        Type of scheduler.
        Options: ["DDIM", "DPM Multi", "DPM Single", "Euler a", "Euler", "Heun", "DPM2 a Karras", "DPM2 Karras", "LMS", "PNDM", "DDPM", "UniPC"]
        Default: UniPC

        num_inference_steps: int
            Number of denoising steps.
            Default: 20; Max: 50

        guidance_scale: float
            Scale for classifier-free guidance
            Default: 7.5

        seed: int
            Seed for image generation.
            Default: Random

        shape: int
            Image resolution. Options are 512 x 512 or 768 x 768.
            Options: ["512","768"]
            Default: 512

        base64: boolean
            Base64 encoding of the output image. 
            Optional 
            Default: false
    """
    def __init__(self, api_key = None):
        self.url = "https://api.segmind.com/v1/sd2.1-txt2img"
        self.headers = {"x-api-key": f"{api_key}"}
        if api_key is None:
            raise Exception("API Key is required")
    
    def generate(self, prompt, negative_prompt = "nude, disfigured, blurry", samples = 1, scheduler = "DDIM", num_inference_steps = 25, guidance_scale = 7.5, seed = 17123564234):
        data = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "samples": f"{samples}",
        "scheduler": scheduler,
        "num_inference_steps": f"{num_inference_steps}",
        "guidance_scale": f"{guidance_scale}",
        "seed": f"{seed}"
    }
        response = requests.post(self.url, json = data, headers = self.headers)
        if response.status_code == 200:
            print(f"Success! You have {response.headers['X-remaining-credits']} credits remaining")
            return Image.open(BytesIO(response.content))
        else:
            raise Exception(f"Error: {response.status_code}")