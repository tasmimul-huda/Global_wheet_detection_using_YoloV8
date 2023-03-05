from pathlib import Path
import os
from ultralytics import YOLO
import cv2

Path('D:/globalwheet/predicted_output/').mkdir(parents=True, exist_ok=True)


model_path = os.path.join('D:/globalwheet/', 'runs', 'detect', 'train', 'weights', 'best.pt')
print(model_path)
# Load a model
model = YOLO(model_path)  # load a custom model
for img in os.listdir('D:/globalwheet/Dataset/test'):
    print(img.split('.')[0])
    img_path = os.path.join('D:/globalwheet/Dataset/test/', img)
#     print(img_path)
    res = model(img_path)
    res_plotted = res[0].plot()
#     cv2.imshow("result", res_plotted)
    cv2.imwrite('D:/globalwheet/predicted_output/{}_op.png'.format(img.split('.')[0]),res_plotted)