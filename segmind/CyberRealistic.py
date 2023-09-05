from .T2I import T2I


class CyberRealistic(T2I):
    def __init__(self, api_key=None):
        super().__init__(
            url="https://api.segmind.com/v1/sd1.5-cyberrealistic", api_key=api_key
        )

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "CyberRealistic_Negative",
        samples=1,
        scheduler="dpmpp_2m",
        num_inference_steps=25,
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
