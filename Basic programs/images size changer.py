import os, glob
import cv2

path = "emoji"

imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
a=0
for infile in imagePaths:
    im = cv2.imread(infile)
    b=cv2.resize(im, (500,500))
    cv2.imwrite("a/"+str(a)+".png",b)
    a=a+1
cv2.waitKey(1)
cv2.destroyAllWindows()