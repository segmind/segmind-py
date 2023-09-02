# Segmind API Wrapper

Wrapper for Segmind API for using Generative models. 
Visit [Website](https://www.segmind.com/)

## Usage

* Import Required Model Class
<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  `from segmindapi import Kadinsky`
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

<br> `from segmindapi import ControlNet`
<br> `model = ControlNet(api_key)`
<br> `img = model.generate(prompt, imageUrl, option)`

For additional options, check Docstring of the model.
### SD2_1
Text-to-image Stable diffusion 2.1 model that can generate images given a natural language prompt.
<br> `from segmindapi import SD2_1`
<br> `model = SD2_1(api_key)`
<br> `img = model.generate(prompt)`

For additional options, check Docstring of the model.

### Kadinsky
Image-to-image Kadinsky model that can generate images given a natural language prompt.
<br> `from segmindapi import Kadinsky`
<br> `model = Kadinsky(api_key)`
<br> `img = model.generate(prompt)`

For additional options, check Docstring of the model.

### SD1_5 Img2Img

A text-to-image diffusion model that can create photorealistic images from any given text input, and additionally has the ability to fill in missing parts of an image by using a mask.
<br> `from segmindapi import SD1_5`

For additional options, check Docstring of the model.

### ERSGAN

An image-to-image model that upscales low-resolution images into high-resolution ones using a GAN trained on a dataset of high-resolution images.
<br> `from segmindapi import ERSGAN`

For additional options, check Docstring of the model.

### BackgroundRemoval
The background removal model efficiently separates the main subject or the object from its surrounding background, resulting in a clean and isolated foreground.
<br> `from segmindapi import BackgroundRemoval`

For additional options, check Docstring of the model.

### Codeformer 
CodeFormer is a robust face restoration algorithm for old photos or AI-generated faces.
<br> `from segmindapi import Codeformer`

For additional options, check Docstring of the model.

### SAM
Segment Anything Model (SAM) is a state-of-the-art image segmentation model that can segment any object in an image.
<br> `from segmindapi import SAM`
<br> `model = SAM(api_key)`
<br> `img = model.generate(imageUrl)`

For additional options, check Docstring of the model.

### FaceSwap
FaceSwap is a state-of-the-art face swapping model that can swap faces in images and videos.
<br> `from segmindapi import FaceSwap`
<br> `model = FaceSwap(api_key)`
<br> `img = model.generate(imageUrl, maskUrl)`

For additional options, check Docstring of the model.



## Dependencies
* PIL (Python Imaging Library)