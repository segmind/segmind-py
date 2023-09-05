from .T2I import T2I


class Flat2D(T2I):
    def __init__(self, api_key=None):
        super().__init__(url="https://api.segmind.com/v1/sd1.5-flat2d", api_key=api_key)

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "(worst quality:0.8), verybadimagenegative_v1.3 easynegative, (surreal:0.8), (modernism:0.8), (art deco:0.8), (art nouveau:0.8)",
        samples=1,
        scheduler="dpmpp_2m",
        num_inference_steps=20,
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
