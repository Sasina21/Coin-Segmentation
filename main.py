import cv2
import numpy as np

# read video

cap = cv2.VideoCapture("Coin2.mp4")                     # if open camera just index of camera

while(cap.read()) :
    ref, frame = cap.read()
    roi = frame[:1080, 0:1920]                          # region of interest

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      # convert to gray pic
    gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)     # reduce noise

    thresh = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 1)
                                                        # adaptive threshold

    kernel = np.ones((3, 3), np.uint8)                  # arrays
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=5)   # morphology

    # show
    cv2.imshow("Show", closing)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# close

cap.release()
cv2.destroyAllWindows()

