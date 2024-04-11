import numpy as np
import matplotlib.pyplot as plt

# Initialize the QR code matrix
qr = np.ones((21,21))

# Set the finder patterns
# Top left
qr[0:7,0:7] = 0
qr[1:6,1:6] = 1
qr[2:5,2:5] = 0

# Top right
qr[0:7,-7:] = 0
qr[1:6,-6:-1] = 1
qr[2:5,-5:-2] = 0

# Bottom left
qr[-7:,0:7] = 0
qr[-6:-1,1:6] = 1
qr[-5:-2,2:5] = 0

# Set the timing patterns
qr[6,8:13] = 0
qr[6,9] = 1
qr[6,11] = 1

qr[8:13,6] = 0
qr[9,6] = 1
qr[11,6] = 1


# add outer padding
qr = np.pad(qr, 4, mode='constant', constant_values=1)


# Display the QR code with grid 21x21
plt.imshow(qr, cmap='gray', interpolation='nearest')
plt.show()