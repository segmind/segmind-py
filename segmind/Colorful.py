from .T2I import T2I


class Colorful(T2I):
    def __init__(self, api_key=None):
        super().__init__(
            url="https://api.segmind.com/v1/sd1.5-colorful", api_key=api_key
        )

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "(low quality:1.4), (worst quality:1.4), (monochrome:1.1), normal quality, cropped, fingers, deformed, distorted, disfigured, limb, hands, anatomy, long neck, negative_hand-neg, skin blemishes, flowers",
        samples=1,
        scheduler="dpmpp_sde_ancestral",
        num_inference_steps=25,
        guidance_scale=9,
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
