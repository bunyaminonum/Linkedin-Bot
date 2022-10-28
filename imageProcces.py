import cv2
import numpy as np
import random

class Image:
    @staticmethod
    def image2():
        img = cv2.imread("photo.jpg", 1)
        img = cv2.resize(img, (500, 500))
        cv2.imshow("kare", img)
        for i in range(5000):
            eksenX = random.randint(0,500)
            eksenY = random.randint(0,500)
            img2=cv2.rectangle(img,(eksenX,eksenY),(eksenX+1,eksenY+1),(0,0,0),-1);
        for i in range(5000):
            eksenX = random.randint(0,500)
            eksenY = random.randint(0,500)
            img2=cv2.rectangle(img,(eksenX,eksenY),(eksenX+1,eksenY+1),(255,255,255),-1);


        cv2.imshow("photo",img2)
        cv2.waitKey(0);

    @staticmethod
    def qr():
        cv2.destroyAllWindows();

        '''siyah arkaplan oluşturmak için'''
        img = np.zeros((512, 512, 3), np.uint8);

        '''arkaplanı beyaza boyamak'''
        img.fill(255)

        '''sol üst -1 le içi boyandı'''
        img2 = cv2.rectangle(img, (20, 20), (40, 40), (0, 0, 0), -1)
        img2 = cv2.rectangle(img, (0, 0), (60, 60), (0, 0, 0), 2)

        '''sol alt'''
        img3 = cv2.rectangle(img, (20, 470), (40, 490), (0, 0, 0), -1)
        img3 = cv2.rectangle(img, (0, 450), (60, 510), (0, 0, 0), 2)

        '''sağ üst'''
        img4 = cv2.rectangle(img, (470, 20), (490, 40), (0, 0, 0), -1)
        img4 = cv2.rectangle(img, (450, 0), (510, 60), (0, 0, 0), 2)

        cv2.imshow("kare", img2)
        cv2.imshow("kare", img3)
        cv2.imshow("kare", img4)

        for i in range(5000):
            eksenX = random.randint(61, 502)
            eksenY = random.randint(61, 512)
            img5 = cv2.rectangle(img, (eksenX, eksenY), (eksenX + 5, eksenY + 5), (0, 0, 0), -1)
            cv2.imshow("kare", img5)

        for i in range(500):
            eksenX2 = random.randint(61, 438)
            eksenY2 = random.randint(0, 61)
            img6 = cv2.rectangle(img, (eksenX2, eksenY2), (eksenX2 + 5, eksenY2 + 5), (0, 0, 0), -1)
            cv2.imshow("kare", img6)

        for i in range(500):
            eksenX3 = random.randint(0, 61)
            eksenY3 = random.randint(61, 442)
            img7 = cv2.rectangle(img, (eksenX3, eksenY3), (eksenX3 + 5, eksenY3 + 5), (0, 0, 0), -1)
            cv2.imshow("kare", img7)

        cv2.waitKey(0);
        cv2.destroyAllWindows();

qr = Image()
qr.qr()

image = Image()
image.image2()

