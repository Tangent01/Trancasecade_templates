import cv2 as cv


def object_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)
    cv.imshow('Video', image)

    detector = cv.CascadeClassifier(r'E:\Python\Project_Box\Extracted_ROI\xml\cascade.xml')
    objects = detector.detectMultiScale(blurred, 1.10, 3)

    for x, y, w, h in objects:
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 127, 255), 2)

    cv.imshow('Detection', image)
    # cv.imwrite(r'E:\Python\Project_Box\Factory', image)


def video(path):
    capture = cv.VideoCapture(path)
    while True:
        ret, frame = capture.read()
        object_detection(frame)
        # cv.imshow('Video', frame)
        if cv.waitKey(10) & 0xff == ord('q'):
            break


video_path = r'E:\Python\Project_Box\Videos\1.mp4'
screenshot_path = r'E:\Python\Project_Box\Screenshots\2.jpg'

src = cv.imread(screenshot_path)

video(video_path)
# object_detection(src)

cv.waitKey(0)
cv.destroyAllWindows()
