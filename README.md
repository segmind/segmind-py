# Segmind API Wrapper

Wrapper for Segmind API for using Generative models. 
Visit [Website](https://www.segmind.com/)

## Installation

Simply Install the pip package by typing the following in the terminal:
<br>

`pip install segmind`

## Usage

* Import Required Model Class
<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  `from segmind import Kadinsky`
* Instantite Model Class with your [API Key](https://cloud.segmind.com/keys)
<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  `model = Kadinsky(api_key)`
* Generate Image
<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  `img = model.generate(prompt)`
* View Image
<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  `img.show()`

## Models Supported

Check Available [Models](https://docs.segmind.com/models)

### ControlNet 

Image to Image using Stable Diffusion 1.5.
<br>
Available Options:
* Canny
* Depth
* OpenPose
* Scribble
* SoftEdge

<br> `from segmind import ControlNet`
<br> `model = ControlNet(api_key)`
<br> `img = model.generate(prompt, imageUrl, option)`

For additional options, check Docstring of the model.
### SD2_1
Text-to-image Stable diffusion 2.1 model that can generate images given a natural language prompt.
<br> `from segmind import SD2_1`
<br> `model = SD2_1(api_key)`
<br> `img = model.generate(prompt)`

For additional options, check Docstring of the model.

### Kadinsky
Image-to-image Kadinsky model that can generate images given a natural language prompt.
<br> `from segmind import Kadinsky`
<br> `model = Kadinsky(api_key)`
<br> `img = model.generate(prompt)`

For additional options, check Docstring of the model.

### SD1_5 Img2Img

A text-to-image diffusion model that can create photorealistic images from any given text input, and additionally has the ability to fill in missing parts of an image by using a mask.
<br> `from segmind import SD1_5`

For additional options, check Docstring of the model.

### ERSGAN

An image-to-image model that upscales low-resolution images into high-resolution ones using a GAN trained on a dataset of high-resolution images.
<br> `from segmind import ERSGAN`

For additional options, check Docstring of the model.

### BackgroundRemoval
The background removal model efficiently separates the main subject or the object from its surrounding background, resulting in a clean and isolated foreground.
<br> `from segmind import BackgroundRemoval`

For additional options, check Docstring of the model.

### Codeformer 
CodeFormer is a robust face restoration algorithm for old photos or AI-generated faces.
<br> `from segmind import Codeformer`

For additional options, check Docstring of the model.

### SAM
Segment Anything Model (SAM) is a state-of-the-art image segmentation model that can segment any object in an image.
<br> `from segmind import SAM`
<br> `model = SAM(api_key)`
<br> `img = model.generate(imageUrl)`

For additional options, check Docstring of the model.

### FaceSwap
FaceSwap is a state-of-the-art face swapping model that can swap faces in images and videos.
<br> `from segmind import FaceSwap`
<br> `model = FaceSwap(api_key)`
<br> `img = model.generate(imageUrl, maskUrl)`

For additional options, check Docstring of the model.

### SDOutpainting

The SDOutpainting model is used for outpainting tasks, where the model is given a part of an image and it needs to generate the rest of the image.
<br> `from segmind import SDOutpainting`
<br> `model = SDOutpainting(api_key)`
<br> `img = model.generate(imageUrl)`

For additional options, check Docstring of the model.

### Word2Img

A text-to-image model that can generate images from any given text input.
<br> `from segmind import Word2Img`
<br> `model = Word2Img(api_key)`
<br> `img = model.generate(image, prompt)`

For additional options, check Docstring of the model.

### QRGenerator

A QR code generator that can generate QR codes from any given text input.
<br> `from segmind import QRGenerator`
<br> `model = QRGenerator(api_key)`
<br> `img = model.generate(prompt, qr_text)`

For additional options, check Docstring of the model.

### Text To Image

We support several text to image models:

* Stable Diffusion XL 1.0
* Segmind Tiny-SD
* Segmind Tiny-SD (Portrait)
* Segmind Small-SD
* Paragon
* Realistic Vision
* Reliberate
* Revanimated
* Colorful
* Cartoon
* Edge of Realism
* Epic Realism
* RPG
* Scifi
* Cyber Realistic
* Samaritan
* RCNZ - Cartoon    
* Manmarumix
* Majicmix
* Juggernaut Final
* Icbinp
* Fruit Fusion
* Flat 2d
* Fantassified Icons
* DvArch
* Dream Shaper
* Deep Spaced Diffusion
* Cute Rich Style
* All in one pixel
* 526mix

You can check the complete list of models [here](https://segmind.com/models).
## Examples

| Model | Code Example | Generated Image |
| --------------- | --------------- | --------------- |
| Stable Diffusion XL | `SDXL(api_key).generate(prompt = "cinematic film still, 4k, realistic, ((cinematic photo:1.3)) of panda wearing a blue spacesuit, sitting in a bar, Fujifilm XT3, long shot, ((low light:1.4)), ((looking straight at the camera:1.3)), upper body shot, somber, shallow depth of field, vignette, highly detailed, high budget Hollywood movie, bokeh, cinemascope, moody, epic, gorgeous, film grain, grainy")` | <img src="https://www.segmind.com/_next/image?url=%2Fsdxl2.jpeg&w=2048&q=75"> |
| Stable Diffusion Outpainting | `SDOutpainting(api_key).generate(image = "https://www.segmind.com//image5.png", prompt = "streets in italy")` | <img src = "https://www.segmind.com/_next/image?url=%2Foutpainting-output.jpeg&w=2048&q=75"> |
| QR Generator | `QRGenerator(api_key).generate(prompt = "A mouth-watering pizza topped with gooey cheese and fresh ingredients, Close-up, Realistic Style, Art Inspirations from Food Photography", qr_text = "www.segmind.com")` | <img src = "https://www.segmind.com/_next/image?url=%2Fqr_output.jpeg&w=2048&q=75"> |
| Word2Img | `Word2Img(api_key).generate(image = "https://www.segmind.com//word2img_input.png", prompt = "top-view, A mouth-watering pizza topped with gooey cheese and fresh ingredients,Food Photography")` | <img src="https://www.segmind.com/_next/image?url=%2Fword2img_output.jpeg&w=2048&q=75"> |
| Kadinsky | `Kadinsky(api_key).generate("tiny isometric city on a tiny floating island, highly detailed, 3d render")` | ![image](https://github.com/segmind/segmind-py/assets/95569637/2f48bfc0-99fb-47b6-a0c2-02f3691d2597) |
| Stable Diffusion v2.1 | `SD2_1(api_key).generate("calico cat wearing a cosmonaut suit, 3d render, pixar style, 8k, high resolution")` | ![image](https://github.com/segmind/segmind-py/assets/95569637/aa615370-abfe-4e4d-aa68-be1144abfce3) |
| Stable Diffusion img2img | `SD1_5(api_key).generate(prompt = "A fantasy landscape, trending on artstation, mystical sky", imageUrl= "https://segmind.com/sd-img2img-input.jpeg")` | ![image](https://github.com/segmind/segmind-py/assets/95569637/954c62f2-74c2-4fa7-8e2b-89c51c433efc) |
| Stable Diffusion Inpainting | `SD1_5(api_key).generate(prompt = "mecha robot sitting on a bench", imageUrl= "https://segmind.com/inpainting-input-image.jpeg", maskUrl= "https://segmind.com/inpainting-input-mask.jpeg")` | ![image](https://github.com/segmind/segmind-py/assets/95569637/9e350c5b-4c65-4ded-a45f-4b99d87b64f6) |
| ControlNet Openpose | `ControlNet(api_key).generate(prompt = "a beautiful fashion model, wearing a red polka dress, red door background. hyperrealistic. photorealism, 4k, extremely detailed", imageUrl = "https://segmind.com/fashion2.jpeg", option="OpenPose")` | ![image](https://github.com/segmind/segmind-py/assets/95569637/fcc9eea0-9de7-4cf8-bedf-d20aa1d15013) |
| ControlNet Scribble | `ControlNet(api_key).generate(prompt = "steampunk underwater helmet, dark ocean background", imageUrl = "https://segmind.com/scribble-input.jpeg", option="Scribble")` | ![image](https://github.com/segmind/segmind-py/assets/95569637/59ff42ba-9d40-4854-bfd5-e6bb2d3bb58e) |
| ControlNet Soft Edge | `ControlNet(api_key).generate(prompt = "royal chamber with fancy bed", imageUrl = "https://segmind.com/soft-edge-input.jpeg", option="SoftEdge")` | ![image](https://github.com/segmind/segmind-py/assets/95569637/b33cf3d1-8fdc-4dbe-a059-78d1fb140188) |
| ControlNet Depth | `ControlNet(api_key).generate(prompt = "young african american man, black suit, smiling, white background", imageUrl = "https://segmind.com/depth.jpeg", option="Depth")` | ![image](https://github.com/segmind/segmind-py/assets/95569637/6061cfcb-1e42-4a96-a8c9-a28614ca7456) |
| ControlNet Canny | `ControlNet(api_key).generate(prompt = "a colorful bird, 4k", imageUrl = "https://segmind.com/canny-input.jpeg", option="Canny")` | ![image](https://github.com/segmind/segmind-py/assets/95569637/2d30867f-3d2f-410a-934a-cd2a3dd9464c) |
| Background Removal | `BackgroundRemoval(api_key).generate(imageUrl = "https://segmind.com/bg-removal.jpg")` | ![image](https://github.com/segmind/segmind-py/assets/95569637/f91495d1-8e9d-424a-882b-efc7aa9502f2) |
| Face Swapper | `FaceSwap(api_key).generate(imageUrl = "https://segmind.com/elon.jpg", maskUrl = "https://segmind.com/burn.gif")` | ![image](https://github.com/segmind/segmind-py/assets/95569637/244ff6d2-350a-41bb-ae35-78e86fb8ca5e) |
| Codeformer | `Codeformer(api_key).generate(imageUrl = "https://segmind.com/codeformer_input.png")` | ![image](https://github.com/segmind/segmind-py/assets/95569637/60b4ce21-e634-4f8b-b155-273c57c07c22) |
| ESRGAN | `ESRGAN(api_key).generate(imageUrl = "https://segmind.com/butterfly.png")` | ![image](https://github.com/segmind/segmind-py/assets/95569637/d7ec5624-c62f-4820-a40c-7417b71e6a8d) |
| SAM | `SAM(api_key).generate(imageUrl = "https://segmind.com/kitchen.jpg")` | ![image](https://github.com/segmind/segmind-py/assets/95569637/7f3d8834-a52c-49b4-b66b-93c52c0b5dfe) |

## Dependencies
* PIL (Python Imaging Library)
