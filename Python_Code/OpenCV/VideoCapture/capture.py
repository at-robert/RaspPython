import cv2, time

# from video file
# video=cv2.VideoCapture("movie.mp4")
# So far, this works in the Windows 7 environment
video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    print(check)
    print(frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # time.sleep(3)
    # To show gray video
    # cv2.imshow("Capturing",gray)
    # To show color video
    cv2.imshow("Capturing",frame)

    key = cv2.waitKey(1)
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows
