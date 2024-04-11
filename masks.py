import numpy as np
import matplotlib.pyplot as plt

mask0 = np.ones((21,21))
mask1 = np.ones((21,21))
mask2 = np.ones((21,21))
mask3 = np.ones((21,21))
mask4 = np.ones((21,21))
mask5 = np.ones((21,21))
mask6 = np.ones((21,21))
mask7 = np.ones((21,21))

for i in range(21):
    for j in range(21):
        if (i+j)%2 == 0:
            mask0[i,j] = 0
        if i%2 == 0:
            mask1[i,j] = 0
        if j%3 == 0:
            mask2[i,j] = 0
        if (i+j)%3 == 0:
            mask3[i,j] = 0
        if (i//2 + j//3)%2 == 0:
            mask4[i,j] = 0
        if (i*j)%2 + (i*j)%3 == 0:
            mask5[i,j] = 0
        if ((i*j)%2 + (i*j)%3)%2 == 0:
            mask6[i,j] = 0
        if ((i+j)%2 + (i*j)%3)%2 == 0:
            mask7[i,j] = 0
        
def initialize(qr):
    
    qr[0:8,0:8] = 1
    qr[0:8,-8:] = 1
    qr[-8:,0:8] = 1

    #set finder patterns
    finder = np.zeros((7,7))
    finder[1:6,1:6] = 1
    finder[2:5,2:5] = 0
    qr[0:7,0:7] = finder
    qr[0:7,-7:] = finder
    qr[-7:,0:7] = finder

    #set timing patterns
    qr[6,7:14] = 1
    qr[7:14,6] = 1
    qr[6,8] = 0
    qr[8,6] = 0
    qr[6,10] = 0
    qr[10,6] = 0
    qr[6,12] = 0
    qr[12,6] = 0



for mask in [mask0, mask1, mask2, mask3, mask4, mask5, mask6, mask7]:
    initialize(mask)

test = np.ones((21,21))
initialize(test)
plt.figure(figsize=(10,10))
plt.subplot(241)
plt.imshow(mask0, cmap='gray', interpolation='nearest')
plt.subplot(242)
plt.imshow(mask1, cmap='gray', interpolation='nearest')
plt.subplot(243)
plt.imshow(mask2, cmap='gray', interpolation='nearest')
plt.subplot(244)
plt.imshow(mask3, cmap='gray', interpolation='nearest')
plt.subplot(245)
plt.imshow(mask4, cmap='gray', interpolation='nearest')
plt.subplot(246)
plt.imshow(mask5, cmap='gray', interpolation='nearest')
plt.subplot(247)
plt.imshow(mask6, cmap='gray', interpolation='nearest')
plt.subplot(248)
plt.imshow(mask7, cmap='gray', interpolation='nearest')
plt.show()

#show test  
plt.imshow(test, cmap='gray', interpolation='nearest')
plt.show()

