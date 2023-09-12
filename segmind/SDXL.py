from .T2I import T2I


class SDXL(T2I):
    def __init__(self, api_key=None):
        super().__init__(
            url="https://api.segmind.com/v1/sdxl1.0-txt2img", api_key=api_key
        )

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, blurry, bad anatomy, blurred, watermark, grainy, signature, cut off, draft",
        samples=1,
        scheduler="dpmmp_sde_ancestral",
        num_inference_steps=25,
        guidance_scale=7,
        seed=None,
        strength=0.75,
        style = "base",
        high_noise_fraction = 0.8
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
            style = style,
            high_noise_fraction = high_noise_fraction
        )
