faceDetector = vision.CascadeObjectDetector();
videoFileReader = vision.VideoFileReader('Test.mp4');
videoFrame      = step(videoFileReader);
bbox            = step(faceDetector, videoFrame);
videoOut = insertObjectAnnotation(videoFrame,'rectangle',bbox,'Face');
figure, imshow(videoOut), title('FACE');