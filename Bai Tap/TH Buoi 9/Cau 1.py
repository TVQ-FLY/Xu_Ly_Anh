import cv2
import matplotlib.pyplot as plt

img = cv2.imread("")
anh_xam = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, otsu = cv2.threshold(anh_xam, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.subplot(131), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(132), plt.imshow(cv2.cvtColor(anh_xam, cv2.COLOR_BGR2RGB))
plt.subplot(133), plt.imshow(cv2.cvtColor(otsu, cv2.COLOR_BGR2RGB))
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()