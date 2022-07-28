
import cv2
from deepface import DeepFace
import random
import os


def musicPlay(songPath):
    playLiat = os.listdir(songPath)
    n = random.randint(0, len(playLiat)-1)
    os.startfile(os.path.join(songPath, playLiat[n]))


def emotionChekar(emotion):
    if emotion == "happy":
        musicPlay('song\happy')

    elif emotion == "angry":
        musicPlay('song\\angrry')

    elif emotion == "disgust":
        musicPlay('song\disgust')

    elif emotion == "sad":
        musicPlay('song\sad')


    elif emotion == "surprise":
        musicPlay('song\surprise')

    elif emotion == "fear":
        musicPlay('song\\faer')

    else:
        musicPlay('song\\natural')

faceCascats = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(1)

while(cam.isOpened()):
    ret, fram = cam.read()

    gry = cv2.cvtColor(fram, cv2.COLOR_BGR2GRAY)
    face = faceCascats.detectMultiScale(gry, 1.1, 4)
    #cv2.imwrite("pic source/img.png", fram);
    #img = cv2.imread('pic source/img.png')
    cv2.waitKey(100)
    try:
        faceInfo = DeepFace.analyze(img_path=fram, actions=['emotion'])
    except:
        print("No face emotion detected")
        continue


    xx = 0
    yy = 0
    for (x, y, w, h) in face:
        cv2.rectangle(fram, (x, y), (x + w, y + h), (0, 0, 255), 2)
        xx = x
        yy = y
    global emotion
    emotion = "NONE"
    emotion = faceInfo['dominant_emotion']

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(fram, emotion, (xx-50, yy-50), font, 4, (255, 0, 0), 5, cv2.LINE_4)
    cv2.imshow("Detected your Emotion", fram)
    cv2.waitKey(7000)
    if emotion != "":
        emotionChekar(emotion)
        break
else:
    print('Can not open your camera')



#cv2.waitKey(10000)
cam.release()
cv2.destroyAllWindows()



