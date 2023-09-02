from .T2I import T2I


class DreamShaper(T2I):
    def __init__(self, api_key=None):
        super().__init__(
            url="https://api.segmind.com/v1/sd1.5-dreamshaper", api_key=api_key
        )

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "cartoon, 3d, sketches, (painting by bad-artist), (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, bad anatomy, (bad-hands-5), (badhandv4), fat, curvy, thick, dull, simple background, ugly, mole, skin tags, acne, freckles, lightning. veil, hat, hood, ((blurry)), ((monochrome)), ((from side)), ((back turned)), Far away, back turned,",
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
