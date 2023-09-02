from .T2I import T2I


class DvArch(T2I):
    def __init__(self, api_key=None):
        super().__init__(url="https://api.segmind.com/v1/sd1.5-dvrach", api_key=api_key)

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "signature, soft, single floor,unclear, watermark, blurry, drawing, sketch, poor quality, ugly, text, type, word, logo, pixelated, low resolution, saturated, high contrast, oversharpened",
        samples=1,
        scheduler="euler_a",
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
