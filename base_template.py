import numpy as np

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
    qr[13,8] = 0