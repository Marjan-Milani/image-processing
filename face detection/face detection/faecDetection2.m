
close all
clc
aa=5;
for s=1:frameNum
% Create a cascade detector object.
facedetector = vision.CascadeObjectDetector('FrontalFaceCART');
filename=strcat('frame',num2str(s),'.png');
img=imread(filename);
img=rgb2gray(img);
BB=step(facedetector,img);
iimg=insertObjectAnnotation(img,'rectangle',BB,'Face');
% figure(1);
% imshow(iimg);
% title('DetectFace');
bbox=[];
% while isempty(bbox)
% videoFrame = step(facedetector,img);
% bbox = step(facedetector, videoFrame);
% end
num=0;
 N=size(BB,1);
for i = 1:N

 %videoFrame=insertObjectAnnotation(videoFrame, 'rectangle', bbox(i,:), 'Face','color','red');
 iimgg = insertObjectAnnotation(img,'rectangle',BB,'Face');
 %videoFrame = insertShape(videoFrame, 'rectangle', bbox(i,:),'color','red');
 iimg = insertShape(img, 'rectangle', BB,'color','red');
% bboxPoints{i}=bbox2points(bbox(i, :));
 num=num+1;
end
figure(1);
imshow(iimgg);
title(['There are ',num2str(num),' faces']);
filenamee=strcat('frameE',num2str(s),'.png');
print('-djpeg',filenamee)
end