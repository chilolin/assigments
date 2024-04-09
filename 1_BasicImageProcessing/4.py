import cv2
import matplotlib.pyplot as plt

image = cv2.imread('./assets/dog.jpg', cv2.IMREAD_GRAYSCALE)

def calculate_features_image(detector, image):
    keypoints = detector.detect(image)
    return cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


cv2.imwrite('results/orb.jpg', calculate_features_image(detector=cv2.ORB_create(), image=image))

cv2.imwrite('results/sift.jpg', calculate_features_image(detector=cv2.SIFT_create(), image=image))

cv2.imwrite('results/akaze.jpg', calculate_features_image(detector=cv2.AKAZE_create(), image=image))
