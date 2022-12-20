import cv2
import numpy as np

#////////////////// find triangle ///////////////////////

img=cv2.imread("answer-sheet1.jpg")
img = cv2.resize(img, (650, 700))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 50, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("Number of contours detected:", len(contours))
for cnt in contours:
   approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
   if len(approx) == 3:
      img = cv2.drawContours(img, [cnt], -1, (0,255,255), 3)
      M = cv2.moments(cnt)
      if M['m00'] != 0.0:
         x = int(M['m10']/M['m00'])
         y = int(M['m01']/M['m00'])
start_point = (48, 130)
end_point = (600, 663)
color = (255, 0, 0)
thickness = 1
image = cv2.rectangle(img, start_point, end_point, color, thickness)
#cv2.imshow("rectangle", image)
cv2.imwrite("./1.jpg", image)
y, x, h, w = 50, 132, 590, 660
crop_image = image[x:w, y:h]
#cv2.imshow("Cropped", crop_image)
cv2.imwrite("./2.jpg", crop_image)

# # #//////////////////////////find rectangle////////////////////////////////

img_rgb = cv2.imread('2.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('temp.png', 0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)
cv2.imwrite('3.jpg', img_rgb)
img = cv2.imread('2.jpg')
start_point = (50, 450)
end_point = (245, 15)
color = (255, 0, 0)
thickness = 1
image = cv2.rectangle(img, start_point, end_point, color, thickness)
#cv2.imshow("rectangle", image)
cv2.imwrite("./4.jpg", image)
y, x, h, w = 70, 20, 230, 450
crop_image2 = image[x:w, y:h]
#cv2.imshow("Cropped", crop_image2)
cv2.imwrite("./5.jpg", crop_image2)
#cv2.imshow('', img)
cv2.waitKey(0)
# #/////////////////////find pentagon/////////////////////////
#
img_rgb = cv2.imread('2.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('temp2.png', 0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)
cv2.imwrite('6.png', img_rgb)
img = cv2.imread('2.jpg')
start_point = (305, 450)
end_point = (500, 15)
color = (200, 240, 0)
thickness = 1
image = cv2.rectangle(img, start_point, end_point, color, thickness)
#cv2.imshow("rectangle", image)
cv2.imwrite("./7.jpg", image)
y, x, h, w = 318, 24, 480, 444
crop_image3 = image[x:w, y:h]
#cv2.imshow("Cropped", crop_image3)
cv2.imwrite("./8.jpg", crop_image3)
#cv2.imshow('', image)
cv2.waitKey(0)
#/////////////////
img_rgb = cv2.imread('8.jpg')
img_rgb = cv2.resize(img_rgb, (400, 500))
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('temp3.png', 0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.75
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w+356, pt[1] + h), (0, 0, 255), 1)
cv2.imwrite('11.png',img_rgb)
#cv2.imshow('', img_rgb)
cv2.waitKey(0)

img_rgb = cv2.imread('5.jpg')
img_rgb = cv2.resize(img_rgb,(400, 500))
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('temp3.png', 0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.75
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w+356, pt[1] + h), (0, 0, 255), 1)
cv2.imwrite('10.png',img_rgb)
#cv2.imshow('', img_rgb)
cv2.waitKey(0)
