from PIL import Image
import numpy as np
from imageshuffle import imageshuffle
from imageshuffle import imagescramble
import matplotlib.pyplot as plt

img = Image.open('tests\\lena.png')
ar = np.asarray(img)

# key = 1234
# s = imageshuffle.Rand( key )
# enc = s.enc( ar )
# dec = s.dec( enc )
# imgplot = plt.imshow(enc)
# plt.show()
# imgplot = plt.imshow(dec)
# plt.show()

key = 5678
s = imageshuffle.RandBlock( key, [8,8] )
enc = s.enc( ar )
dec = s.dec( enc )
imgplot = plt.imshow(enc)
plt.show()
imgplot = plt.imshow(dec)
plt.show()

key = 1234
s = imageshuffle.Rand( key )
enc = s.enc( ar )
dec = s.dec( enc )
imgplot = plt.imshow(enc)
plt.show()
imgplot = plt.imshow(dec)
plt.show()

key = 5678
s = imageshuffle.RandBlock( key, [8,8] )
enc = s.enc( ar )
dec = s.dec( enc )
imgplot = plt.imshow(enc)
plt.show()
imgplot = plt.imshow(dec)
plt.show()