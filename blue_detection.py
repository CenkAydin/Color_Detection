import cv2
import numpy as np

def blue_detection():
    kamera = cv2.VideoCapture(0)
    sayac = True
    kamera.set(3, 640)
    kamera.set(4, 480)
    while sayac is True:
        ret, frame = kamera.read()
        frame = cv2.flip(frame, 1, )

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        kernal = np.ones((5, 5), "uint8")

        #mavi
        blue_lower = np.array([110,50,50])
        blue_higher = np.array([130,255,255])

        blue_mask = cv2.inRange(hsv, blue_lower, blue_higher)
        bluemask_dilate = cv2.dilate(blue_mask, kernal)
        bluemask_blur = cv2.GaussianBlur(bluemask_dilate, (5, 5), 4 / 6)

        blue_contours, hierarchy = cv2.findContours(bluemask_blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        i = 0
        for pic, contour in enumerate(blue_contours):
            area = cv2.contourArea(contour)
            if area > 3000:
                x, y, w, h = cv2.boundingRect(contour)
                i = i + 1
                if i == 2:
                    break
                cisim_yatay = x + (w // 2)  # cismin merkezi
                cisim_dikey = y + (h // 2)
                print(cisim_dikey, cisim_yatay)
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                frame = cv2.circle(frame, (cisim_yatay, cisim_dikey), 5, (0, 0, 255), -1)


                if y < 10 and x <= 360:
                    frame = cv2.putText(frame, f"yatay={cisim_yatay} dikey={cisim_dikey}", (x, y + h + 20),
                                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                                        (0, 0, 255), 3)
                elif y < 10 and x > 360:
                    frame = cv2.putText(frame, f"yatay={cisim_yatay} dikey={cisim_dikey}", (350, y + h + 20),
                                        cv2.FONT_HERSHEY_SIMPLEX,
                                        1, (0, 0, 255), 3)
                elif y > 10 and x <= 360:
                    frame = cv2.putText(frame, f"yatay={cisim_yatay} dikey={cisim_dikey}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                        (0, 0, 255), 3)
                elif y > 10 and x > 360:
                    frame = cv2.putText(frame, f"yatay={cisim_yatay} dikey={cisim_dikey}", (350, y), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                        (0, 0, 255), 3)
        cv2.imshow("FRAME", frame)
        cv2.imshow("BLUE", blue_mask)
        if cv2.waitKey(1) == ord("q"):
            break

    kamera.release()
    cv2.destroyAllWindows()

blue_detection()
