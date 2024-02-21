from pyautogui import screenshot
import pyscreenshot

@staticmethod
def screenshotalle(Output):
        foto = screenshot()
        foto.save(Output)
@staticmethod
def screenshotSize(out, size2, size1, size3, size4):
        int(size1), int(size2)
        image = pyscreenshot.grab(bbox=(size1, size2, size3, size4))
        image.save(out)
