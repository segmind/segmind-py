from .T2I import T2I


class Icbinp(T2I):
    def __init__(self, api_key=None):
        super().__init__(url="https://api.segmind.com/v1/sd1.5-icbinp", api_key=api_key)

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "((Semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime:1.4)), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate",
        samples=1,
        scheduler="dpmpp_2m",
        num_inference_steps=30,
        guidance_scale=10,
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
