from segmindapi import *
import PIL

def getKey():
    with open("api_key.txt", "r") as f:
        api_key = f.read()
    return api_key

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
    assert type(SD2_1(api_key).generate(prompt = "calico cat wearing a cosmonaut suit, 3d render, pixar style, 8k, high resolution")) == PIL.JpegImagePlugin.JpegImageFile

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

def test_tinySD():
    api_key = getKey()
    assert type(TinySD(api_key).generate(prompt = "cyborg in a battlefield, explosions, highly detailed")) == PIL.JpegImagePlugin.JpegImageFile

def test_SDXL():
    api_key = getKey()
    assert type(SDXL(api_key).generate(prompt = "cinematic film still, 4k, realistic, ((cinematic photo:1.3)) of panda wearing a blue spacesuit, sitting in a bar, Fujifilm XT3, long shot, ((low light:1.4)), ((looking straight at the camera:1.3)), upper body shot, somber, shallow depth of field, vignette, highly detailed, high budget Hollywood movie, bokeh, cinemascope, moody, epic, gorgeous, film grain, grainy")) == PIL.JpegImagePlugin.JpegImageFile

def test_PortraitSD():
    api_key = getKey()
    assert type(PortraitSD(api_key).generate(prompt = "RAW closeup portrait photo of a 25-year-old american, long brunette hair, pale skin, deep smile.")) == PIL.JpegImagePlugin.JpegImageFile

def test_SmallSD():
    api_key = getKey()
    assert type(SmallSD(api_key).generate(prompt = "a toy panda standing on a pile of broccoli")) == PIL.JpegImagePlugin.JpegImageFile

def test_CyberRealistic():
    api_key = getKey()
    assert type(CyberRealistic(api_key).generate(prompt = "Photo of a burger with cheese from food photograph, food photography, photorealistic, ultra realistic, maximum detail, foreground focus, recipes.com, epicurious, instagram, 8k, volumetric light, cinematic, octane render, uplight, no blur, depth of field, dof, bokeh, 8k")) == PIL.JpegImagePlugin.JpegImageFile

def test_Paragon():
    api_key = getKey()
    assert type(Paragon(api_key).generate(prompt = "a photo of Jason, solo, in frame, somber, apocalyptic city, dark theme, extremely detailed eyes, detailed symmetric realistic face extremely detailed natural skin texture, peach fuzz, messy hair, masterpiece, absurdres, artillery fire in the background, award winning ")) == PIL.JpegImagePlugin.JpegImageFile

def test_RealisticVision():
    api_key = getKey()
    assert type(RealisticVision(api_key).generate(prompt = "((selfie)) photo of an american girl and guy, smiling, (yosemite:1.3), mountains, wearing a backpack, red top, hiking jacket, rocks, river, wood, analog style (look at viewer:1.2) (skin texture), close up, cinematic light, ((night sky:1.2)), (milkiway:1.4), sidelighting, Fujiflim XT3, DSLR, 50mm, (long windblown hair)")) == PIL.JpegImagePlugin.JpegImageFile

def test_Reliberate():
    api_key = getKey()
    assert type(Reliberate(api_key).generate(prompt = "a photo of catherine, solo, in frame, smiling, summer floral outfit, dark theme, extremely detailed eyes, detailed symmetric realistic face extremely detailed natural skin texture, peach fuzz, messy hair, masterpiece, absurdres, artillery fire in the background, award winning")) == PIL.JpegImagePlugin.JpegImageFile

def test_Revanimated():
    api_key = getKey()
    assert type(Revanimated(api_key).generate(prompt = "advanced aircraft, gundam, dark black robot, spaceship, long, giant guns, futuristic design, scifi, in space, supernova, stars, planets, (8k, RAW photo, best quality, ultra high res, photorealistic, masterpiece, ultra-detailed, Unreal Engine),best quality, warrior,((cinematic look)), insane details, advanced weapon, fight, battle, epic, power, combat, shoot, shooting, missiles, bombs, explosions, rockets, jetpack, defence, attacking,wide angle")) == PIL.JpegImagePlugin.JpegImageFile

def test_Colorful():
    api_key = getKey()
    assert type(Colorful(api_key).generate(prompt = "((( splash of colorful paint))) Colorful, beautiful cat lady, dark, splash, disembodied head, Black ink flow, photorealistic, intricately detailed, fluid gouache, calligraphy, acrylic, watercolor art, 8k concept art, intricately detailed, complex, elegant, expansive, fantastical, (style-paintmagic),(style of Kim Keever:1.2),  (cat), disembodied head, photorealistic, intricately detailed, 8k concept art, intricately detailed, complex, elegant, expansive, fantastical")) == PIL.JpegImagePlugin.JpegImageFile

def test_Cartoon():
    api_key = getKey()
    assert type(Cartoon(api_key).generate(prompt = "(8k, best quality, masterpiece:1.2), (finely detailed),kuririn,  1boy,solo,cowboy shot, (bald:1.3), dwarf,(lime green long wizard robes:1.5), smile,open mouth, outdoors, (hut), forest, flowers, parted lips,black eyes,(black belt:1.3), (buckle), lime-green long sleeves,((purple stocking hat:1.2)), ((oversized clothes)), brown shoes,lime-green very long sleeves,arms behind back ")) == PIL.JpegImagePlugin.JpegImageFile

def test_EdgeOfRealism():
    api_key = getKey()
    assert type(EdgeOfRealism(api_key).generate(prompt = "RAW commercial photo the pretty instagram fashion model, ((smiling)), in the red sweater, yellow cap posing in new york city, in the style of colorful geometrics, guy aroch, helene knoop, glowing pastels, bold lines, bright colors, sun-soaked colours, Fujifilm X-T4, Sony")) == PIL.JpegImagePlugin.JpegImageFile

def test_EpicRealism():
    api_key = getKey()
    assert type(EpicRealism(api_key).generate(prompt = "a photo of a 25-year-old american, long brunette hair, pale skin, deep smile, wearing a red polka dress, red door background. hyperrealistic. photorealism, 4k, extremely detailed")) == PIL.JpegImagePlugin.JpegImageFile

def test_RPG():
    api_key = getKey()
    assert type(RPG(api_key).generate(prompt = "warrior, warhammer 40k, space marine, intricate ornamented, Smoke Gray Aluminum Beige armor, adepta sororitas, dynamic posture, Alpine desert landscape background, volumetric cinematic lighting, (highly detailed skull:0.8), realistic reflections, cinematic composition")) == PIL.JpegImagePlugin.JpegImageFile

def test_SciFi():
    api_key = getKey()
    assert type(SciFi(api_key).generate(prompt = "futuristic sci-fi high-tech city of Atlantis in late afternoon light, wispy clouds in a blue sky")) == PIL.JpegImagePlugin.JpegImageFile

def test_Samaritan():
    api_key = getKey()
    assert type(Samaritan(api_key).generate(prompt = "1 beautiful woman, office suit, coat, shirt, silver hair, hand Sui Ishida (best quality, masterpiece)")) == PIL.JpegImagePlugin.JpegImageFile

def test_RCNZ():
    api_key = getKey()
    assert type(RCNZ(api_key).generate(prompt = "a duck, warm vibrant colours, natural lighting, dappled lighting, diffused lighting, absurdres, highres, 8k, uhd, hdr, rtx, unreal 5, octane render, RAW photo, photorealistic, global illumination, subsurface scattering")) == PIL.JpegImagePlugin.JpegImageFile

def test_MajicMix():
    api_key = getKey()
    assert type(MajicMix(api_key).generate(prompt = "best quality, masterpiece, (photorealistic:1.4), 1boy, (50 years old:1.2) beard, dramatic lighting, hyper quality, intricate detail, ultra realistic, maximum detail, foreground focus, instagram, 8k, volumetric light, cinematic, octane render, uplight, no blur, 8k")) == PIL.JpegImagePlugin.JpegImageFile

def test_ManmaruMix():
    api_key = getKey()
    assert type(ManmaruMix(api_key).generate(prompt = "masterpiece,best quality, dog, 1girl, sitting,park,looking at viewer")) == PIL.JpegImagePlugin.JpegImageFile

def test_Juggernaut():
    api_key = getKey()
    assert type(Juggernaut(api_key).generate(prompt = "Portrait photo of bearded guy in a worn mech suit, ((light bokeh)), intricate, (steel metal [rust]), elegant, sharp focus, photo by greg rutkowski, soft lighting, vibrant colors, (masterpiece), ((streets)), (detailed face)+, eye iris")) == PIL.JpegImagePlugin.JpegImageFile

def test_Icbinp():
    api_key = getKey()
    assert type(Icbinp(api_key).generate(prompt = "A red vintage car on the streets of Newyork, front view, car in the center of the road, hyper quality, intricate detail, masterpiece, photorealistic, ultra realistic, maximum detail, foreground focus, instagram, 8k, volumetric light, cinematic, octane render, uplight, no blur, 8k")) == PIL.JpegImagePlugin.JpegImageFile

def test_FruitFusion():
    api_key = getKey()
    assert type(FruitFusion(api_key).generate(prompt = "few large strawberries falling into a pink liquid, milk bath photography, strawberry, slow - mo high speed photography, flowing milk, realistic jelly splashes, super high speed photography, berries dripping juice, fight with strawberries, strawberry granules, inspired by Alberto Seveso, berries dripping, high speed photography, award winning macro photography, culinary art photography, splash image")) == PIL.JpegImagePlugin.JpegImageFile

def test_Flat2D():
    api_key = getKey()
    assert type(Flat2D(api_key).generate(prompt = "(best-quality:0.8), (best-quality:0.8), perfect anime illustration of a Celestial Morbid Gaelic [Doghouse:Toyota:5] with a face, detailed with Cloth patterns, inside a Worn-Out Bar, Summer, equirectangular 360, Masterpiece, Sad, Surrealism Art, backlight, telephoto lens, Kodak portra, Lavender background, full of color, trending on artstation, trending on CGSociety")) == PIL.JpegImagePlugin.JpegImageFile

def test_FantassifiedIcons():
    api_key = getKey()
    assert type(FantassifiedIcons(api_key).generate(prompt = "a magical  sailor moon themed shield intricate, pastel color scheme, high quality, 8k, highly detailed")) == PIL.JpegImagePlugin.JpegImageFile

def test_DeepSpaceDiffusion():
    api_key = getKey()
    assert type(DeepSpaceDiffusion(api_key).generate(prompt = "jwst, nebula, spiral galaxy,mixed colors,outerspace, hyper quality, intricate detail, ultra realistic, maximum detail, foreground focus, instagram, 8k, volumetric light, cinematic, octane render, uplight, no blur, 8k")) == PIL.JpegImagePlugin.JpegImageFile

def test_DreamShaper():
    api_key = getKey()
    assert type(DreamShaper(api_key).generate("(masterpiece, best quality, absurdres, intricate), fantasy, (woman, extremely delicate and beautiful, looking at viewer, (floating long hair)), (standing over tiny village), colorhalf00d, fog, smoke, haunting, spooky, creepy, dark themed, 8k GC wallpaper, Trending on artstation, octance render, unreal engine, volumetrics dtx, award winning digital art, ink, official art, painting by anna dittmann")) == PIL.JpegImagePlugin.JpegImageFile

def test_DvArch():
    api_key = getKey()
    assert type(DvArch(api_key).generate(prompt = "dvArchModern, 85mm, f1.8, portrait, photo realistic, hyperrealistic, orante, super detailed, intricate, dramatic, sun lighting, shadows, high dynamic range, modern interior, beach house, mexico")) == PIL.JpegImagePlugin.JpegImageFile

def test_CuteRichStyle():
    api_key = getKey()
    assert type(CuteRichStyle(api_key).generate(prompt = "cbzbb , elon musk ,charachter ,cute, little,  beautiful, devian art, trending artstation, digital art, detailed, cute, realistic, humanoide, character, tiny,cinematic sho ,cinematic lights,elon musk,looks happy")) == PIL.JpegImagePlugin.JpegImageFile

def test_AllInOnePixel():
    api_key = getKey()
    assert type(AllInOnePixel(api_key).generate(prompt = "futuristic abandoned city landscape, pale colors, 16 bit style, pixelart, gamedev, game asset background")) == PIL.JpegImagePlugin.JpegImageFile

def test_526Mix():
    api_key = getKey()
    assert type(Mix526(api_key).generate(prompt = "POV photo of an amazing snozboffle milkshake with chocolate syrup on a plain glass. busy retro diner interior background, people in background, kodak vision 3")) == PIL.JpegImagePlugin.JpegImageFile

def test_SDOutpainting():
    api_key = getKey()
    assert type(SDOutpainting(api_key).generate(image = "https://www.segmind.com//image5.png", prompt = "streets in italy")) == PIL.JpegImagePlugin.JpegImageFile

def test_Word2Img():
    api_key = getKey()
    assert type(Word2Img(api_key).generate(image = "https://www.segmind.com//word2img_input.png", prompt = "top-view, A mouth-watering pizza topped with gooey cheese and fresh ingredients,Food Photography")) == PIL.JpegImagePlugin.JpegImageFile

def test_QRGenerator():
    api_key = getKey()
    assert type(QRGenerator(api_key).generate(prompt = "A mouth-watering pizza topped with gooey cheese and fresh ingredients, Close-up, Realistic Style, Art Inspirations from Food Photography", qr_text = "www.segmind.com")) == PIL.JpegImagePlugin.JpegImageFile

if __name__ == "__main__":
    test_QRGenerator()