import requests
from PIL import Image
from io import BytesIO

class Kadinsky:
    """
        This API allows you to transform text descriptions into corresponding image representations and is available at https://api.segmind.com/v1/kandinsky2.1-txt2img.
        
        The API accepts the following parameters:
            prompt: The text description of the image to be generated.
            negative_prompt: The text description of the image to be avoided.
            samples: The number of images to be generated. The default value is 1.
            scheduler: The scheduler to be used for the generation. The default value is DDIM.
            num_inference_steps: The number of inference steps to be used for the generation. The default value is 20.
            guidance_scale: The guidance scale to be used for the generation. The default value is 7.5.
            seed: The seed to be used for the generation. The default value is 1024.
            img_width: The width of the image to be generated. The default value is 512.
            img_height: The height of the image to be generated. The default value is 512.
        
        The API returns the following:
            The generated image.
        
        It also prints the number of credits remaining in your account.
    """
    def __init__(self, api_key : str = None):
        self.url = "https://api.segmind.com/v1/kandinsky2.1-txt2img"
        self.headers = {"x-api-key": f"{api_key}"}
        if api_key is None:
            raise Exception("API Key is required")
        
    
    def generate(self, prompt : str, negative_prompt : str = "NONE", samples = 1, scheduler = "DDIM", num_inference_steps = 20, guidance_scale = 7.5, seed = 1024, img_width = 512, img_height = 512):
        data = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "samples": f"{samples}",
        "scheduler": scheduler,
        "num_inference_steps": f"{num_inference_steps}",
        "guidance_scale": f"{guidance_scale}",
        "seed": f"{seed}",
        "img_width": f"{img_width}",
        "img_height": f"{img_height}"
    }
        response = requests.post(self.url, json = data, headers = self.headers)
        if response.status_code == 200:
            print(f"Success! You have {response.headers['X-remaining-credits']} credits remaining")
            return Image.open(BytesIO(response.content))
        else:
            raise Exception(f"Error: {response.status_code}")

        