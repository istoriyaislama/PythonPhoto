import photo


#Image#
#Open
photo.photographs.photographs.imageOpen("image.jpeg")

#Open for Windows
photo.photographs.photographs.imageOpenWindows("image.jpeg")

#Crop
photo.photographs.photographs.imageCrop("image.jpeg", 0, 0, 100, 200, "imageCrop.jpg")

#Text in Image
photo.photographs.photographs.imageFont("image.jpeg", "PythonPhoto", "arial.ttf", 15, "imagefont.jpg")

#Counter
photo.photographs.photographs.imageCounter("image.jpeg", "imageCounter.jpg")

#Blur
photo.photographs.photographs.imageBlur("image.jpeg", "imageBlur.jpg")

#Thumbnail
photo.photographs.photographs.imageThumbnail("image.jpeg", "imageThumbnail.jpg", 100, 120)

#Turn over
photo.photographs.photographs.imageTurnOver("image.jpeg", 100, "imageTurnOver.jpeg")

#Sharpen
photo.photographs.photographs.imageSharpen("image.jpeg", "imageSharpen.jpg")

#Convert JPG in PNG or PNG in JPG
photo.photographs.photographs.imageJpgInPng("image.jpeg", "imageJpgInPng.png")
#photo.photographs.photographs.imagePngInJpg("image.png", "imagePngInJpg.jpg")

#Image Black-White
photo.photographs.photographs.imageBlackWhite("image1.jpeg")

#Image Black-White Save
photo.photographs.photographs.imageBlackWhiteSave("image1.jpeg", "out.png")

#Edge Enhance
photo.photographs.photographs.imageEdgeEnhance("image.jpeg", "out.png")

#Edge Enhance More
photo.photographs.photographs.imageEdgeEnhanceMore("image.jpeg", "out.png")

#Screenshot#
#Screenshot all ekran
photo.screenshotImage.screenshotImage.screenshotalle("screenshot.png")

#Screenshot size
photo.screenshotImage.screenshotImage.screenshotSize("PythonPhoto.png", 720, 720, 1280, 820)

#Video#
#Video
photo.video.video.video("PythonPhoto", 720, 720, 30.0, 'w')
