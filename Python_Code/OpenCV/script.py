import cv2

# Gary level
img=cv2.imread("galaxy.jpg",0)
# color level
# img=cv2.imread("galaxy.jpg",1)

print(type(img))
print(img)
print(img.shape) #resolution
print(img.ndim) #dimension

resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
# cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.imshow("Galaxy", img)
cv2.waitKey(2000)
cv2.destroyAllWindows()
