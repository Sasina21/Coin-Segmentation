import cv2

# read video

cap = cv2.VideoCapture("Coin2.mp4")                     # if open camera just index of camera

while(cap.read()) :
    ref, frame = cap.read()
    roi = frame[:1080, 0:1920]                          # region of interest

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      # convert to gray pic
    gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)     # reduce noise

    # show
    cv2.imshow("Show", gray_blur)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# close

cap.release()
cv2.destroyAllWindows()

