import numpy as np
import matplotlib.pyplot as plt

def get_alignment_pattern_centers(version):
    # Dictionary mapping QR versions to their respective alignment pattern centers
    alignment_centers = {
        2: [6, 18],
        3: [6, 22],
        4: [6, 26],
        5: [6, 30],
        6: [6, 34],
        7: [6, 22, 38],
        8: [6, 24, 42],
        9: [6, 26, 46],
        10: [6, 28, 50],
        11: [6, 30, 54],
        12: [6, 32, 58],
        13: [6, 34, 62],
        14: [6, 26, 46, 66],
        15: [6, 26, 48, 70],
        16: [6, 26, 50, 74],
        17: [6, 30, 54, 78],
        18: [6, 30, 56, 82],
        19: [6, 30, 58, 86],
        20: [6, 34, 62, 90],
        21: [6, 28, 50, 72, 94],
        22: [6, 26, 50, 74, 98],
        23: [6, 30, 54, 78, 102],
        24: [6, 28, 54, 80, 106],
        25: [6, 32, 58, 84, 110],
        26: [6, 30, 58, 86, 114],
        27: [6, 34, 62, 90, 118],
        28: [6, 26, 50, 74, 98, 122],
        29: [6, 30, 54, 78, 102, 126],
        30: [6, 26, 52, 78, 104, 130],
        31: [6, 30, 56, 82, 108, 134],
        32: [6, 34, 60, 86, 112, 138],
        33: [6, 30, 58, 86, 114, 142],
        34: [6, 34, 62, 90, 118, 146],
        35: [6, 30, 54, 78, 102, 126, 150],
        36: [6, 24, 50, 76, 102, 128, 154],
        37: [6, 28, 54, 80, 106, 132, 158],
        38: [6, 32, 58, 84, 110, 136, 162],
        39: [6, 26, 54, 82, 110, 138, 166],
        40: [6, 30, 58, 86, 114, 142, 170]
    }
    
    # Return the centers for the given version, or an empty list if the version is 1 (no alignment patterns)
    return alignment_centers.get(version, [])

def initialize(version):
    
    size = version*4 + 17
    qr = np.ones((size,size))
    
    #set finder patterns
    qr[0:8,0:8] = 1
    qr[0:8,-8:] = 1
    qr[-8:,0:8] = 1
    finder = np.zeros((7,7))
    finder[1:6,1:6] = 1
    finder[2:5,2:5] = 0
    qr[0:7,0:7] = finder
    qr[0:7,-7:] = finder
    qr[-7:,0:7] = finder

    #set timing patterns
    for i in range(8, size-8):
        qr[6,i] = (i % 2)
        qr[i,6] = (i % 2)

    #dark module
    qr[(4*version) + 9, 8] = 0

    if version > 1:
        alignment_pattern = np.zeros((5,5))
        alignment_pattern[1:4,1:4] = 1
        alignment_pattern[2,2] = 0

        alignment_centers = get_alignment_pattern_centers(version)
        for i in alignment_centers:
            for j in alignment_centers:
                #check collision with finder patterns:
                if not((i < 9 and j < 9) or (i < 9 and j > size-9) or (i > size-9 and j < 9)):
                    qr[i-2:i+3,j-2:j+3] = alignment_pattern
        
    return qr


for i in range(1, 40):
    qr_code = initialize(i)
    size = qr_code.shape[0]

    fig, ax = plt.subplots()
    cax = ax.matshow(qr_code, cmap='gray')

    # Set grid to appear between cells
    ax.set_xticks(np.arange(-0.5, size, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, size, 1), minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=0.5)

    # Hide major grid lines and labels to clean up the plot
    ax.grid(which='major', linestyle='', linewidth=0)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    plt.title(f"QR Version {i}")
    plt.show()

