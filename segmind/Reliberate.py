from .T2I import T2I


class Reliberate(T2I):
    def __init__(self, api_key=None):
        super().__init__(
            url="https://api.segmind.com/v1/sd1.5-reliberate", api_key=api_key
        )

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "airbrushed,3d, render, painting, anime, manga, illustration, (deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, (mutated hands and fingers:1.4), disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation,bige yes, teeth,nose piercing,(((extra arms)))cartoon,young,child ",
        samples=1,
        scheduler="dpmpp_sde_ancestral",
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
