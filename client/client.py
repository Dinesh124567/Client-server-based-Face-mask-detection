import requests
import get_scanned_client as gsc
import cv2
import time
import numpy as np


def camera_interface(url = "http://localhost:8000/facemask_detect"):
    # Open the camera
    cap = cv2.VideoCapture(0)
    
    
    while True:
        
        # Read and display each frame
        ret, img = cap.read()
        cv2.imshow("face mask detection", img)

        k = cv2.waitKey(125)

        TIMER = int(2)
        prev = time.time()
        while TIMER >= 0:
            ret, img = cap.read()

            font = cv2.FONT_HERSHEY_SIMPLEX

            cv2.imshow("face mask detection", img)
            cv2.waitKey(125)

            cur = time.time()

            if cur-prev >= 1:
                prev = cur
                TIMER = TIMER-1
                # Press Esc to exit
            if k == 27:
                break

        else:
            ret, img = cap.read()

            is_success, im_buf_arr = cv2.imencode(".jpg", img)
            byte_im = im_buf_arr.tobytes()

            cv2_image = gsc.get_scanned_from_api(byte_im, url)
            
            img = cv2_image
            cv2.imshow("face mask detection", img)

            cv2.waitKey(2000)
            cv2.imwrite('camera.jpg', img)

        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

import sys
url="http://localhost:8000/facemask_detect"
if len(sys.argv) >1:
    url = sys.argv[1]

camera_interface(url)
