import numpy as np
import matplotlib.pyplot as plt

# Initialize the QR code matrix
qr = np.ones((21,21))

def initialize(qr):
    #set finder patterns
    finder = np.zeros((7,7))
    finder[1:6,1:6] = 1
    finder[2:5,2:5] = 0
    qr[0:7,0:7] = finder
    qr[0:7,-7:] = finder
    qr[-7:,0:7] = finder
    
    #set timing patterns
    qr[6,8:13] = 0
    qr[6,9] = 1
    qr[6,11] = 1
    qr[8:13,6] = 0
    qr[9,6] = 1
    qr[11,6] = 1

def to_byte(data):
    #convert data to bytes
    data = data.encode('utf-8')
    data = list(data)
    data = [format(x, '08b') for x in data]
    data = ''.join(data)
    data += '0' * 4
    return data

print(to_byte('Hello World!'))


# add outer padding
qr = np.pad(qr, 4, mode='constant', constant_values=1)
# Display the QR code with grid 21x21
plt.imshow(qr, cmap='gray', interpolation='nearest')
plt.show()