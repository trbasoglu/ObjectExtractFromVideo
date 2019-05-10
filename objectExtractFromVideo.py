from datetime import datetime
import cv2
import argparse

# Argument parsing
parser = argparse.ArgumentParser(description="This program can be used for extract objects from video streams. ")
parser.add_argument("-v", "--video", required=True, help="path of video file")
parser.add_argument("-x", "--x_size", required=False, help="crop size of x dimension", default=250)
parser.add_argument("-y", "--y_size", required=False, help="crop size of y dimension", default=250)
args = vars(parser.parse_args())

Path = args["video"]

cap = cv2.VideoCapture(Path)
i = 0
stop = False
while True:
    ok, frame = cap.read()
    if not ok:
        break
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1) & 0xff
    if k == 32 or stop:  # press space to pause video.It pauses after roi selection.
        bbox = cv2.selectROI("frame", frame, False)
        crop = frame[int(bbox[1]) - 50:int(bbox[1] + bbox[3]) + 50, int(bbox[0]) - 50:int(bbox[0] + bbox[2]) + 50]
        nameOfImage = "img_" + str(datetime.now().strftime('%d%m%y%H%M'))+'_'+str(i)+'.jpg'  # file name
        i += 1
        stop = True
        k1 = cv2.waitKey(0) & 0xff
        if k1 == 32:  # press space to play
            stop = False
        if len(crop) > 0:
            crop = cv2.resize(crop, (args["x_size"], args["y_size"]))
            cv2.imwrite(nameOfImage, crop)
    elif k == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
