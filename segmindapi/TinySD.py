from .T2I import T2I


class TinySD(T2I):
    def __init__(self, api_key=None):
        super().__init__(
            url="https://api.segmind.com/v1/tinysd1.5-txt2img", api_key=api_key
        )

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "(deformed iris, deformed pupils, semi-realistic, cgi, render, sketch, cartoon, drawing, anime), text, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, BadDream, UnrealisticDream",
        samples=1,
        scheduler="dmpp_2m",
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
