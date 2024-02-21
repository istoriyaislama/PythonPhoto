from photo import photographs, screenshotImage, video


#Image#
#Open
foto = photographs.imageOpen("image.jpeg")

#Open for Windows
photographs.imageOpenWindows("image.jpeg")

#Crop
photographs.imageCrop("image.jpeg", 0, 0, 100, 200, "imageCrop.jpg")

#Text in Image
photographs.imageFont("image.jpeg", "PythonPhoto", "arial.ttf", 15, "imagefont.jpg")

#Counter
photographs.imageCounter("image.jpeg", "imageCounter.jpg")

#Blur
photographs.imageBlur("image.jpeg", "imageBlur.jpg")

#Thumbnail
photographs.imageThumbnail("image.jpeg", "imageThumbnail.jpg", 100, 120)

#Turn over
photographs.imageTurnOver("image.jpeg", 100, "imageTurnOver.jpeg")

#Sharpen
photographs.imageSharpen("image.jpeg", "imageSharpen.jpg")

#Convert JPG in PNG or PNG in JPG
photographs.imageJpgInPng("image.jpeg", "imageJpgInPng.png")
#photographs.imagePngInJpg("image.png", "imagePngInJpg")

#Image Black-White
photographs.imageBlackWhite("image1.jpeg")

#Image Edge Enhance
photographs.imageEdgeEnhance("image.jpeg", "imageout.jpeg")

#Image Edge Enhance More
photographs.imageEdgeEnhanceMore("image.jpg", "imageout.jpeg")

#Image Box Blur
photographs.imageBoxBlur("image.jpeg", "imageout.jpeg")

#Image Color 3D LUT
photographs.imageColor3DLUT("image.jpeg", "imageout.jpeg")

#Image Emboss
photographs.imageEmboss("image.jpeg", "imageout.jpeg")

#Screenshot#
#Screenshot all ekran
screenshotImage.screenshotalle("screenshot.png")

#Screenshot size
screenshotImage.screenshotSize("PythonPhoto.png", 720, 720, 1280, 820)

#Video#
#Video
video.video("PythonPhoto", 720, 720, 30.0, 'w')
