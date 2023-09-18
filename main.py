import cv2

# read video

cap = cv2.VideoCapture("Coin2.mp4") #if open camera just index of camera

while(cap.read()) :
    ref, frame = cap.read()

    cv2.imshow("Show", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# close

cap.release()
cv2.destroyAllWindows()

