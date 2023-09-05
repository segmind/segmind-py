from .T2I import T2I


class Cartoon(T2I):
    def __init__(self, api_key=None):
        super().__init__(
            url="https://api.segmind.com/v1/sd1.5-disneyB", api_key=api_key
        )

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "bad-hands-5, (worst quality:2), (low quality:2),EasyNegative,lowres, ((1girl,fur trim,bangs,((hair)),((limes,sash)),underwear,necklace,choker,grass,motor vehicle,car,buttons,holding:1.2,monochrome,bad eyes,bad hands,underwear)), ((grayscale)",
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
