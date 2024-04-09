import cv2
import numpy as np

dog = cv2.imread('./assets/dog.jpg', cv2.IMREAD_GRAYSCALE)
cat = cv2.imread('./assets/cat.jpg', cv2.IMREAD_GRAYSCALE)

dog2 = cv2.resize(dog, (cat.shape[1], cat.shape[0]))

diff = dog2.astype(int) - cat.astype(int)
im_diff_center = np.floor_divide(diff, 2) + 128

cv2.imwrite('results/diff.jpg', im_diff_center)