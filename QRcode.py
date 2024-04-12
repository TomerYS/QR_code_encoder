import numpy as np
import matplotlib.pyplot as plt
from base_template import initialize

# Initialize the QR code matrix
qr = np.ones((21,21))

initialize(qr)

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