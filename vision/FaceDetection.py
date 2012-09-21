#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Owner
#
# Created:     19/09/2012
# Copyright:   (c) Owner 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import numpy as np
import cv2
import cv2.cv as cv
from opencv.video import create_capture
from opencv.common import clock, draw_str

class FaceDetection:
    alreadydetected = False
    responsetext = "messagetrigger a person came into view messagetrigger"
    defcascade = os.path.join(os.path.dirname(__file__), 'opencv', 'haarcascade_frontalface_alt.xml')
    defnested = os.path.join(os.path.dirname(__file__), 'opencv', 'haarcascade_eye_tree_eyeglasses.xml')


    def detect(self, img, cascade):
        rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv.CV_HAAR_SCALE_IMAGE)
        if len(rects) == 0:
            return []
        rects[:,2:] += rects[:,:2]
        return rects

    def draw_rects(self, img, rects, color):
        for x1, y1, x2, y2 in rects:
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

    def __init__(self):
        pass

    def start(self, queue, cascade_file = defcascade,
            nested_file = defnested):
        #import sys, getopt

        #args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
        try: video_src = video_src[0]
        except: video_src = 0

        cascade = cv2.CascadeClassifier(cascade_file)
        nested = cv2.CascadeClassifier(nested_file)

        cam = create_capture(video_src, fallback='synth:bg=../cpp/lena.jpg:noise=0.05')

        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = cv2.equalizeHist(gray)

            t = clock()
            rects = self.detect(gray, cascade)
            vis = img.copy()
            self.draw_rects(vis, rects, (0, 255, 0))
            if not self.alreadydetected and len(rects) > 0:
                queue.put(self.responsetext)
                self.alreadydetected = True
            for x1, y1, x2, y2 in rects:
                roi = gray[y1:y2, x1:x2]
                vis_roi = vis[y1:y2, x1:x2]
                subrects = self.detect(roi.copy(), nested)
                self.draw_rects(vis_roi, subrects, (255, 0, 0))
            dt = clock() - t

            draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))
            cv2.imshow('facedetect', vis)

            if 0xFF & cv2.waitKey(5) == 27:
                break
        cv2.destroyAllWindows()


import multiprocessing
if __name__ == '__main__':
    fd = FaceDetection()
    message_queue = multiprocessing.Queue()
    vision_process = multiprocessing.Process(name='vision',target=fd.start, args=(message_queue,))
    #fd.start(message_queue)
    vision_process.start()