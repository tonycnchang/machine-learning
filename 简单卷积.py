import numpy as np
from PIL import Image

image = Image.open("zhaopian.jpg").convert("L")
old_data = np.asarray(image)#(shape:196,259)
old_sha = old_data.shape

c = np.zeros((old_sha[0],1))
r = np.zeros((1,old_sha[1]+2))

pic = np.c_[c,old_data,c]
pic = np.r_[r,pic,r]

sha = pic.shape
new = np.zeros(sha)

he_x = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
he_y = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
he_xy = np.array([[-1,-1,0],[-1,0,1],[0,1,1]])
prew_x = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
prew_y = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
prew_xy = np.array([[-2,-1,0],[-1,0,1],[0,1,2]])
laplace1 = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
laplace2 = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

he_list = ["he_x","he_y","he_xy","prew_x","prew_y","prew_xy","laplace1","laplace2"]

for he in he_list:
    for i in range(sha[0]-2):
        for j in range(sha[1]-2):
            view = pic[i:i+3,j:j+3]
            point = np.sum(view*eval(he))
            new[i,j] = point
    im = Image.fromarray(np.uint8(new)).save("convole_" + he + ".png")
#im = Image.fromarray(np.uint8(data))
#im.show()

