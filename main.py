import cvzone
from cvzone.HandTrackingModule import HandDetector
import cv2
import pyautogui as auto

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    # Get image frame
    success, img = cap.read()
    hands, img = detector.findHands(img, draw=True)

    if hands:
        # Hand 1
        hand1 = hands[0]
        HandLandMarkList1 = hand1["lmList"]  # List of 21 Landmark points
        length,info,frame = detector.findDistance(HandLandMarkList1[4][0:2],HandLandMarkList1[8][0:2],img)
        length = round(length)

        if length<25:
            auto.press('up')

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        break

