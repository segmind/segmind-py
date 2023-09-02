from .T2I import T2I


class Samaritan(T2I):
    def __init__(self, api_key=None):
        super().__init__(
            url="https://api.segmind.com/v1/sd1.5-samaritan_3d", api_key=api_key
        )

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "EasyNegativeV2 ng_deepnegative_v1_75t greyscale (worst quality, low quality)",
        samples=1,
        scheduler="euler_a",
        num_inference_steps=20,
        guidance_scale=7.5,
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
