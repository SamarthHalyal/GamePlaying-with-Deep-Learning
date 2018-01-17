import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import ReleaseKey, PressKey, W
from getkeys import key_check
from alexnet import alexnet
import os

WIDTH = 40
HEIGHT = 69
LR = 1e-3
EPOCH = 8
MODEL_NAME = 'FlappyDL-{}-{}-{}-epochs.model'.format(LR,'alexnet',EPOCH)

model = alexnet(WIDTH,HEIGHT,LR)
model.load(MODEL_NAME)

def jump():
    PressKey(W)
    ReleaseKey(W)


def main():
    last_time = time.time()
    paused = False
    while(True):
        screen =  np.array(ImageGrab.grab(bbox=(0,90,400,690)))
        screen = cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen,(WIDTH,HEIGHT))        
        
        print("Frame took {} seconds".format(time.time()-last_time))  
        last_time = time.time()


        prediction = model.predict([screen.reshape(WIDTH,HEIGHT,1)])[0]
        moves = list(np.around(prediction))
        print(moves,prediction)

        if moves == [1,0]:
            jump()
            print("Hey\nI\nJumped")

        keys = key_check()
        
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(W)
                
        
        cv2.imshow('window', screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


main()
