import cv2

# 表示
img = cv2.imread("./assets/dog.jpg")
# cv2.imshow('color', img)
# cv2.waitKey(0)

# 拡大
exp = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
# cv2.imshow('color', exp)
# cv2.waitKey(0)

# 縮小
red = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
# cv2.imshow('color', red)
# cv2.waitKey(0)

concat = cv2.hconcat([cv2.vconcat([red, red, red, red]), cv2.vconcat([img, img]), exp])

cv2.imwrite('./results/dog_concat.jpg', concat)

# 回転
rot90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('./results/dog_rotate_90.jpg', rot90)
# cv2.imshow('color', rot90)
# cv2.waitKey(0)

rotm90 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
# cv2.imshow('color', rotm90)
# cv2.waitKey(0)

rot180 = cv2.rotate(img, cv2.ROTATE_180)
cv2.imwrite('./results/dog_rotate_180.jpg', rot180)
# cv2.imshow('color', rot180)
# cv2.waitKey(0)

# 2値化
img = cv2.imread("./assets/dog.jpg", 0)
ret, thr = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)
cv2.imwrite('./results/dog_threshold.jpg', thr)
cv2.imshow('threshold', thr)
cv2.waitKey(0)
cv2.destroyAllWindows()