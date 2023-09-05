from .T2I import T2I


class SciFi(T2I):
    def __init__(self, api_key=None):
        super().__init__(url="https://api.segmind.com/v1/sd1.5-scifi", api_key=api_key)

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "blurry, blurred, amateur, ugly, low quality, sketch, low resolution, warped, crooked, deformed, cartoony, low detail",
        samples=1,
        scheduler="dpmpp_2m",
        num_inference_steps=30,
        guidance_scale=5,
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
