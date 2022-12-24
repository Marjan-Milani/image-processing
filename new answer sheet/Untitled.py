import cv2 as cv
import numpy as np

marker_list = ['temp9.png', 'temp2.png']
point = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 8:''}

k = 1
l = 0
dict_answer = {}

for j in marker_list:
    img_rgb = cv.imread('cropped2.png')
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread(j, 0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.72
    loc = np.where(res >= threshold)
    r1 = []
    r2 = []
    c1 = []
    c2 = []
    for pt in zip(*loc[::-1]):
        start = []
        r1.append(pt[0])
        r2.append(pt[0]+w)
        c1.append(pt[1])
        c2.append(pt[1]+h)

    cv.rectangle(img_rgb, (min(r1), min(c1)), (max(r2), max(c2)), (0, 0, 255), 2)
    img1 = img_rgb[min(c1):max(c2), min(r1):max(r2)]
    img_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    template = cv.imread('temp3.png', 0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.70
    loc = np.where(res >= threshold)
    pt_temp = (0, 0)
    for pt in zip(*loc[::-1]):
        if(abs(pt[1]-pt_temp[1])<10):
            pt_temp = pt
            continue
        pt_temp = pt
        start = []
        s = 8
        for i in range(5):
            img_crop = img_gray[pt[1]:pt[1] + h, (pt[0] + 50) + (20 * i):(pt[0] + 71) + (20 * i)]
            if (np.mean(img_crop) < 200):
                cv.rectangle(img1, ((pt[0] + 50) + (20 * i), pt[1]), ((pt[0] + 71) + (20 * i), pt[1] + h),
                             (0, 0, 255), 2)
                s = i
                break
        dict_answer[k] = point[s]
        k += 1
    l+= 1
    cv.imwrite('res'+str(l)+'.png', img1)

print(dict_answer)


