clc
clear all;
close all;
VideoObject=VideoReader('Test.mp4');
frameNum=VideoObject.NumberOfFrames;
for ii=1:VideoObject.NumberOfFrames;
 filename=strcat('frame',num2str(ii),'.png');
 Singleframe=read(VideoObject,ii);
 imwrite(Singleframe,filename);
end