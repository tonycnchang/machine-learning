import os
import math
from PIL import Image

def composite(band,parameter):
    c1 = parameter[0]
    mu1 = parameter[2]
    sigma1 = parameter[3]
    c2 = parameter[1]
    mu2 = paramter[4]
    sigma2 = parameter[5]

    p1 = []
    p2 = []
    for pixel in band:
        p1.append(c1 * gauss(pixel,mu1,sigma1))
        p2.append(c2 * gauss(pixel,mu2,sigma2))

    scale(p1)
    scale(p2)
    return[p1,p2]

if __name__ == "__main__":
    im = Image.open("bullet.jpg")
    print(im.size,im.mode)

    im = im.split()[0]
    nb = []

    data = list(im.getdata())
    parameter = GMM(data)
    t = composite(data,paramter)

    im1 = Image.new("L",im.size)
    im1.putdata(t[0])
