import cv2
import pyautogui
import numpy as np

class video:
    def video(name, sizeVideo1, sizeVideo2, fps, key):
        videoname = f"{name}.avi"
        screnSize = (sizeVideo1, sizeVideo2)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(videoname, fourcc, fps, (screnSize))
        while True:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
            if cv2.waitKey(1) == ord(key):
                break
        cv2.destroyAllWindows()
        out.release()