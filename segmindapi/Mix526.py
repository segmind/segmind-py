from .T2I import T2I


class Mix526(T2I):
    def __init__(self, api_key=None):
        super().__init__(url="https://api.segmind.com/v1/sd1.5-526mix", api_key=api_key)

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "<neg-sketch-2>, illustration, unreal, unclear",
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
