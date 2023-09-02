from .T2I import T2I


class AllInOnePixel(T2I):
    def __init__(self, api_key=None):
        super().__init__(
            url="https://api.segmind.com/v1/sd1.5-allinonepixel", api_key=api_key
        )

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "out of frame, duplicate, watermark, signature, text, error, deformed",
        samples=1,
        scheduler="euler",
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
