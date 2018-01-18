import cv2
import imutils
import numpy as np

def get_line(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    lines = cv2.HoughLines(edges,1,np.pi/180,50)
    for rho,theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        # cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    print(x1,x2,y1,y2)
    cx = int((x1+x2)/2)
    cy = int((y1+y2)/2)
    print(cx,cy)
    # cv2.circle(img,(cx,cy),5,(0,255,0),-1)

    cv2.imshow('frame',img)
    cv2.waitKey(0)
    return cx,cy

def rotate(cx,cy, img):
    height, width,_ = img.shape
    print(width, height)
    xpercent = int(abs((cx/width)*100))
    ypercent = int(abs((cy/height)*100))

    print("xpercent, ypercent", xpercent, ypercent)
    if xpercent>50:
        print("point in right palne and vertical")
        # Todo: rotate clock by 90*

        r = imutils.rotate_bound(img, 90)
        cv2.imshow("roatated", r)
        cv2.waitKey(0)

    elif xpercent>0 and 0 < ypercent<50:
        print("point in upper left plane and vertical")
        # Todo: rotate anti-clock by 90*
        r = imutils.rotate_bound(img, -90)
        cv2.imshow("roatated", r)
        cv2.waitKey(0)

    elif xpercent<=0 :
        print("point in upper left plane and horizontal")
        # Todo: rotate clock by 180*
        r = imutils.rotate_bound(img , 180)
        cv2.imshow("roatated", r)
        cv2.waitKey(0)
    else :
        print("No rotation needed")
        r = img

    cv2.imwrite("test.png", r)


def getline(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)
    for x1, y1, x2, y2 in lines[0]:
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow('getline',image)

img = cv2.imread("PATH TO IMAGE")

if __name__ == "__main__":
    # main(sys.argv[1:])
    cx,cy = get_line(img)
    image = rotate(cx,cy, img)
    getline(img)

