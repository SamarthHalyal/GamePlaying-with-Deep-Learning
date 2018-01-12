import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import ReleaseKey, PressKey, W, A, S, D 
lt = 0

def draw_lines(img,lines):
    global lt
    try:
        for line in lines:
            coords = line[0]
            print((coords[0], coords[1]), (coords[2], coords[3]), time.time()-lt)
            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), (255,255,255), 20)
    except:
        pass

def draw_ball(img,circles):
    if circles is not None:
        circles = np.round(circles[0,:]).astype("int")
        for x,y,r in circles:
            cv2.circle(img,(x,y),r,(0,255,0),4)
    cv2.imshow("window2",img)

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    processed_img = cv2.GaussianBlur(processed_img, (5,5), 0)
    vertices = np.array([[50,0],[150,0],[150,600],[50,600]], np.int32)
    processed_img = roi(processed_img, [vertices])

    # more info: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
    #                          edges       rho   theta   thresh         # min length, max gap:        
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180,np.array([]),5,50)
    circles = cv2.HoughCircles(processed_img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)
    draw_ball(original_image,circles)
    draw_lines(processed_img,lines)
    return processed_img

def roi(img, vertices):
    #blank mask:
    mask = np.zeros_like(img)
    # fill the mask
    cv2.fillPoly(mask, vertices, 255)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked

def main():
    global lt
    lt = last_time = time.time()
    while(True):
        screen =  np.array(ImageGrab.grab(bbox=(0,80,400,675)))
        new_screen = process_img(screen)
        lt = last_time = time.time()
        cv2.imshow('window', new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


main()
