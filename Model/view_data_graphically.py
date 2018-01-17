import pandas as pd
import numpy as np
from collections import Counter
from random import shuffle
import cv2

train_data = np.load('training_data_v2.npy')

df = pd.DataFrame(train_data)

for data in train_data:
   img = data[0]
   keys = data[1]
   cv2.imshow('test',img)
   print(keys)
   if cv2.waitKey(25) & 0XFF == ord('q'):
       cv2.destroyAllWindows()
       break
