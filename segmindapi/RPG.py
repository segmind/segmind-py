from .T2I import T2I


class RPG(T2I):
    def __init__(self, api_key=None):
        super().__init__(url="https://api.segmind.com/v1/sd1.5-rpg", api_key=api_key)

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "boring, poorly drawn, bad artist, (worst quality:1.4), simple background, uninspired, (bad quality:1.4), monochrome, low background contrast, background noise, duplicate, crowded, (nipples:1.2), big breasts",
        samples=1,
        scheduler="ddim",
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
