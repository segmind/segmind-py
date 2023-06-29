from segmindapi import *
import PIL

def getKey():
    with open("api_key.txt", "r") as f:
        api_key = f.readline()
    return str(api_key)

def test_BackgroundRemoval():
    api_key = getKey()
    assert type(BackgroundRemoval(api_key).generate(imageUrl = "https://segmind.com/bg-removal.jpg")) == PIL.PngImagePlugin.PngImageFile

def test_FaceSwap():
    api_key = getKey()
    assert type(FaceSwap(api_key).generate(imageUrl = "https://segmind.com/elon.jpg", maskUrl = "https://segmind.com/burn.gif")) == PIL.GifImagePlugin.GifImageFile

def test_Codeformer():
    api_key = getKey()
    assert type(Codeformer(api_key).generate(imageUrl = "https://segmind.com/codeformer_input.png")) == PIL.JpegImagePlugin.JpegImageFile

def test_ESRGAN():
    api_key = getKey()
    assert type(ESRGAN(api_key).generate(imageUrl = "https://segmind.com/butterfly.png")) == PIL.JpegImagePlugin.JpegImageFile

def test_SAM():
    api_key = getKey()
    assert type(SAM(api_key).generate(imageUrl = "https://segmind.com/kitchen.jpg")) == PIL.JpegImagePlugin.JpegImageFile

def test_Kadinsky():
    api_key = getKey()
    assert type(Kadinsky(api_key).generate(prompt = "tiny isometric city on a tiny floating island, highly detailed, 3d render")) == PIL.JpegImagePlugin.JpegImageFile

def test_SD2_1():
    api_key = getKey()
    assert type(Kadinsky(api_key).generate(prompt = "calico cat wearing a cosmonaut suit, 3d render, pixar style, 8k, high resolution")) == PIL.JpegImagePlugin.JpegImageFile

def test_SD1_5():
    api_key = getKey()
    assert type(SD1_5(api_key).generate(prompt = "mecha robot sitting on a bench", imageUrl= "https://segmind.com/inpainting-input-image.jpeg", maskUrl= "https://segmind.com/inpainting-input-mask.jpeg")) == PIL.JpegImagePlugin.JpegImageFile
    assert type(SD1_5(api_key).generate(prompt = "A fantasy landscape, trending on artstation, mystical sky", imageUrl= "https://segmind.com/sd-img2img-input.jpeg")) == PIL.JpegImagePlugin.JpegImageFile

def test_ControlNet():
    api_key = getKey()
    assert type(ControlNet(api_key).generate(prompt = "a beautiful fashion model, wearing a red polka dress, red door background. hyperrealistic. photorealism, 4k, extremely detailed", imageUrl = "https://segmind.com/fashion2.jpeg", option="OpenPose")) == PIL.JpegImagePlugin.JpegImageFile
    assert type(ControlNet(api_key).generate(prompt = "steampunk underwater helmet, dark ocean background", imageUrl = "https://segmind.com/scribble-input.jpeg", option="Scribble")) == PIL.JpegImagePlugin.JpegImageFile
    assert type(ControlNet(api_key).generate(prompt = "royal chamber with fancy bed", imageUrl = "https://segmind.com/soft-edge-input.jpeg", option="SoftEdge")) == PIL.JpegImagePlugin.JpegImageFile
    assert type(ControlNet(api_key).generate(prompt = "young african american man, black suit, smiling, white background", imageUrl = "https://segmind.com/depth.jpeg", option="Depth")) == PIL.JpegImagePlugin.JpegImageFile
    assert type(ControlNet(api_key).generate(prompt = "a colorful bird, 4k", imageUrl = "https://segmind.com/canny-input.jpeg", option="Canny")) == PIL.JpegImagePlugin.JpegImageFile