import cv2
cap = cv2.VideoCapture('video3.mp4')     # type 0 for using webcam
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while(True):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.05,
		minNeighbors=3,
		minSize=(25, 25),
		flags=cv2.CASCADE_SCALE_IMAGE)
	print("Found {0} faces!".format(len(faces)))
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (220, 240, 0), 2)
	cv2.imshow('frame', frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q") or key == 27:
		break
cap.release()
cv2.destroyAllWindows()
