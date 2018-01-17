import numpy as np
from alexnet import alexnet

WIDTH = 40
HEIGHT = 69
LR = 1e-3
EPOCH = 8
MODEL_NAME = 'FlappyDL-{}-{}-{}-epochs.model'.format(LR,'alexnet',EPOCH)

model = alexnet(WIDTH,HEIGHT,LR)

train_data = np.load('training.npy')

train = train_data[:-500]
test = train_data[-500:]

X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
y = [i[1] for i in train]

test_X = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
test_y = [i[1] for i in test]

model.fit({'input': X},{'targets': y}, n_epoch=EPOCH,
          validation_set=({'input': test_X}, {'targets': test_y}),
          snapshot_step=50, show_metric=True, run_id=MODEL_NAME)

model.save(MODEL_NAME)


