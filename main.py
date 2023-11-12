import cv2
import matplotlib.pyplot as plt
import numpy as np
#Bu satırda fotoğraf açma okuma yapılıyor:
foto=cv2.imread("picture.png")
cv2.imshow("picture.png",foto)

B = foto[:,:,0]
G = foto[:,:,1]
R = foto[:,:,2]


from matplotlib import pyplot as plt
#Bu satırda fotoyu grileştirme yapıyoruz:
imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
plt.imshow(imgGray, cmap='gray')
plt.show()


#Bu satırda grileştirilmiş fotoğrafın histogramı açık kodla hesaplanıyor:
histog = np.zeros(256)
for i in range(foto.shape[0]):
    for j in range(foto.shape[1]):
        pixel_deg= foto[i, j]
        histog[pixel_deg] += 1

plt.bar(range(256), histog)
plt.show()