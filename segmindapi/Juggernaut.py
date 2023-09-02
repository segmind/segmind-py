from .T2I import T2I


class Juggernaut(T2I):
    def __init__(self, api_key=None):
        super().__init__(
            url="https://api.segmind.com/v1/sd1.5-juggernaut", api_key=api_key
        )

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "(worst quality, low quality, normal quality, lowres, low details, oversaturated, undersaturated, overexposed, underexposed, grayscale, bw, bad photo, bad photography, bad art)++++, (watermark, signature, text font, username, error, logo, words, letters, digits, autograph, trademark, name)+, (blur, blurry, grainy), morbid, ugly, asymmetrical, mutated malformed, mutilated, poorly lit, bad shadow, draft, cropped, out of frame, cut off, censored, jpeg artifacts, out of focus, glitch, duplicate, (airbrushed, cartoon, anime, semi-realistic, cgi, render, blender, digital art, manga, amateur)++, (3D ,3D Game, 3D Game Scene, 3D Character), (bad hands, bad anatomy, bad body, bad face, bad teeth, bad arms, bad legs, deformities)++",
        samples=1,
        scheduler="dpmpp_2m",
        num_inference_steps=25,
        guidance_scale=5,
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
