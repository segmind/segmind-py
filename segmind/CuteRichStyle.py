from .T2I import T2I


class CuteRichStyle(T2I):
    def __init__(self, api_key=None):
        super().__init__(
            url="https://api.segmind.com/v1/sd1.5-cuterichstyle", api_key=api_key
        )

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "pencil draw, bad photo, bad draw , anime,ironman,robot,animals,explosions,text,letters,ugly",
        samples=1,
        scheduler="dpmpp_sde_ancestral",
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
