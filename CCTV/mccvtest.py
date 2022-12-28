from facenet_pytorch import MTCNN
import torch
import numpy as np
import mmcv, cv2
from PIL import Image, ImageDraw
from IPython import display

# yeki a chizaei k yad gereftam ineke age esm file py
# tasadofan esm yeki a library ha bashe, error circular mide
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print('Running on device: {}'.format(device))
mtcnn = MTCNN(keep_all=True, device=device)
video = mmcv.VideoReader('video3.mp4')
frames = [Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)) for frame in video]
frames_tracked = []
for i, frame in enumerate(frames):
    print('\r frame: {}'.format(i + 1), end='')
    boxes, _ = mtcnn.detect(frame)
    frame_draw = frame.copy()
    draw = ImageDraw.Draw(frame_draw)
    for box in boxes:
        draw.rectangle(box.tolist(), outline=(255, 0, 0), width=6)
    frames_tracked.append(frame_draw.resize((640, 360), Image.BILINEAR))
print('\nDone')
 # Save video
d = display.display(frames_tracked[0], display_id=True)
dim = frames_tracked[0].size
fourcc = cv2.VideoWriter_fourcc(*'FMP4')
video_tracked = cv2.VideoWriter('video_tracked.mp4', fourcc, 25.0, dim)
for frame in frames_tracked:
    video_tracked.write(cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR))
video_tracked.release()

# namayesh
cap1 = cv2.VideoCapture('video_tracked.mp4')
while(cap1.isOpened()):
  ret, frame = cap1.read()
  if ret == True:
    cv2.imshow('Frame', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  else:
    break
cap1.release()
cv2.destroyAllWindows()
