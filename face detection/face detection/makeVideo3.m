video = VideoWriter('Test.mp4.avi');
%create the video object
open(video); %open the file for writing
for as=1:frameNum %where N is the number of images
 fileNamee=strcat('frameE',num2str(s),'.png');
 Ii = imread(fileNamee); %read the next image
 writeVideo(video,Ii); %write the image to file
end
close(video); %close the file
winopen Test.mp4.avi


video = VideoWriter('capture'); %create the video object
open(video); %open the file for writing
for as=1:frameNum %where N is the number of images
 fileNamee=strcat('frameE',num2str(as),'.png');
 Ii = imread(fileNamee); %read the next image
 writeVideo(video,Ii); %write the image to file
end
close(video); %close the file