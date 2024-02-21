from PIL import Image, ImageFilter, ImageFont, ImageDraw
import sys



@staticmethod
def imageOpen(photo):
        try:
            foto = Image.open(photo)
            return foto
        except FileNotFoundError:
           return f"Error no file: {photo}"

@staticmethod
def imageBlur(photoBlur, photoBlurOutput):
        try:
            original = Image.open(photoBlur)
        except FileNotFoundError:
            print(f"Error no file: {photoBlur}")

        blurred = original.filter(ImageFilter.BLUR)
        original.show()
        blurred.show()
        blurred.save(photoBlurOutput)

@staticmethod
def imageThumbnail(photoThumbnail, photoThumbnailOutput, size1, size2):
        size = (size1, size2)
        saved = photoThumbnailOutput
        img = Image.open(photoThumbnail)
        img.thumbnail(size)
        img.save(saved)
        img.show()

@staticmethod
def imageOpenWindows(photoOpen):
        try:
            foto = Image.open(photoOpen)
            foto.show()
        except FileNotFoundError:
            print(f"Error no file: {photoOpen}")

@staticmethod
def imageCounter(photoCounter, photoCounterOut):
        img = Image.open(photoCounter)
        img = img.filter(ImageFilter.CONTOUR)
        img.save(photoCounterOut)
        img.show()

@staticmethod
def imageCrop(photoCrop, sizeCrop1, sizeCrop2, sizeCrop3, sizeCrop4, photoCropOutput):
        image = Image.open(photoCrop)
        cropped = image.crop((sizeCrop1, sizeCrop2, sizeCrop3, sizeCrop4))
        cropped.save(photoCropOutput)
        cropped.show()

@staticmethod
def imageTurnOver(photoTurnOver, photoTurnOverRadius, photoTurnOverOutput):
        try:
            tatras = Image.open(photoTurnOver)
        except IOError:
            print(f"Error no file: {photoTurnOver}")
            sys.exit(1)

        rotated = tatras.rotate(photoTurnOverRadius)
        rotated.save(photoTurnOverOutput)

@staticmethod
def imageFont(fontOpen, fontText, font1, sizefont, fontOutput):
         try:
             tatras = Image.open(fontOpen)
         except:
             print("Unable to load image")
             sys.exit(1)

         idraw = ImageDraw.Draw(tatras)
         text = fontText

         font = ImageFont.truetype(font1, size=sizefont)

         idraw.text((10, 10), text, font=font)

         tatras.save(fontOutput)
@staticmethod
def imageSharpen(sharpenOpen, sharpenOutput):
        image = Image.open(sharpenOpen)
        blurred_jelly = image.filter(ImageFilter.SHARPEN)
        blurred_jelly.save(sharpenOutput)
@staticmethod
def imageJpgInPng(Open, Output):
        try:
            tatras = Image.open(Open)
        except IOError:
            print("Unable to load image")
            sys.exit(1)

        tatras.save(Output, 'png')
@staticmethod
def imagePngInJpg(Open, Output):
        try:
            tatras = Image.open(Open)
        except IOError:
            print("Unable to load image")
            sys.exit(1)

        tatras.save(Output, 'jpg')
@staticmethod
def imageBlackWhite(Open):
        try:
            tatras = Image.open(Open)
        except IOError:
            print("Unable to load image")
            sys.exit(1)

        grayscale = tatras.convert('L')
        grayscale.show()
@staticmethod
def imageBlackWhiteSave(Open, Output):
        try:
            tatras = Image.open(Open)
        except IOError:
            print("Unable to load image")
            sys.exit(1)

        grayscale = tatras.convert('L')
        grayscale.save(Output)
        grayscale.show()
@staticmethod
def imageDeateil(openPhoto, outPhoto):
        image = Image.OPEN(openPhoto)
        imageout = image.filter(ImageFilter.DETAIL)
        imageout.save(outPhoto)
        imageout.show()
@staticmethod
def imageEdgeEnhance(open, out):
        img = Image.OPEN(open)
        imgout = img.filter(ImageFilter.EDGE_ENHANCE)
        imgout.save(out)
        imgout.show()
@staticmethod
def imageEdgeEnhanceMore(open, out):
        img = Image.OPEN(open)
        imgout = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        imgout.save(out)
        imgout.show()
@staticmethod
def imageBoxBlur(open, out):
        img = Image.OPEN(open)
        imgout = img.filter(ImageFilter.BoxBlur)
        imgout.save(out)
        imgout.show()
@staticmethod
def imageColor3DLUT(open, out):
        img = Image.OPEN(open)
        imgout = img.filter(ImageFilter.Color3DLUT)
        imgout.save(out)
        imgout.show()
@staticmethod
def imageEmboss(open, out):
        img = Image.OPEN(open)
        imgout = img.filter(ImageFilter.EMBOSS)
        imgout.save(out)
        imgout.show()

