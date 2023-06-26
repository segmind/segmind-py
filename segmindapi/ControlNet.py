import requests
from PIL import Image
from io import BytesIO

class ControlNet:
    """
        This API allows you to generate images using various images using ControlNet and is available at https://api.segmind.com/v1/sd1.5-controlnet-canny, https://api.segmind.com/v1/sd1.5-controlnet-depth, https://api.segmind.com/v1/sd1.5-controlnet-openpose, https://api.segmind.com/v1/sd1.5-controlnet-scribble, https://api.segmind.com/v1/sd1.5-controlnet-softedge.

        The API accepts the following parameters:
        
        prompt: str
            Prompt to render, eg. "Stormtrooper giving a lecture"  

        imageUrl: str
            Input image URL.

        option: str
            Type of ControlNet.
            Options: ["Canny", "Depth", "OpenPose", "Scribble", "SoftEdge"]
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

        strength: float
            Controlnet conditioning, closeness to the original image.
            Default: 1; Range: 0 to 1
 
        The API returns the following:
            The generated image.
        
        It also prints the number of credits remaining in your account.
    """
    def __init__(self, api_key = None):
        self.headers = {"x-api-key": f"{api_key}"}
        if api_key is None:
            raise Exception("API Key is required")
    
    def generate(self, prompt : str, imageUrl, option, negative_prompt : str = "nude, disfigured, cartoon, blurry", samples = 1, scheduler = "UniPC", num_inference_steps = 50, guidance_scale = 10.5, seed = 98877465625, strength = 0.75):
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
        option = option.lower()
        if option == "canny":
            url = "https://api.segmind.com/v1/sd1.5-controlnet-canny"
        elif option == "depth":
            url = "https://api.segmind.com/v1/sd1.5-controlnet-depth"
        elif option == "openpose":
            url = "https://api.segmind.com/v1/sd1.5-controlnet-openpose"
        elif option == "scribble":
            url = "https://api.segmind.com/v1/sd1.5-controlnet-scribble"
        elif option == "softedge":
            url = "https://api.segmind.com/v1/sd1.5-controlnet-softedge"
        else:
            raise Exception("Invalid option")
        
        response = requests.post(url, json = data, headers = self.headers)
        if response.status_code == 200:
            print(f"Success! You have {response.headers['X-remaining-credits']} credits remaining")
            return Image.open(BytesIO(response.content))
        else:
            raise Exception(f"Error: {response.status_code}")