import cv2
import numpy as np

# frame per second = 15
# resolution = 1024*768

camera = cv2.VideoCapture(0)
out = cv2.VideoWriter('Output.mp4', -1, 15.0, (1024,768))

while(camera.isOpened):
        print 'camera is opened'
        ret, frame = camera.read()
        print 'camera read'
        if ret == True:
            frame = cv2.flip(frame,0)
            out.write(frame)
            print 'frame wrote'

            # cv2.imshow('frame',frame)
            if cv2.waitKey(1) == ord('q'):
                print 'wating for input'
                break

        else:
            print 'why am i here?'
            break

camera.release()
out.release()
cv2.destroyAllWindows()
