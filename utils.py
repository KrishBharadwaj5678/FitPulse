import numpy as np

# Angle calculation
def calculate_angle(a,b,c):
    a = np.array(a) # shoulder
    b = np.array(b) # elbow
    c = np.array(c) # wrist

    # Computes angle in radians using arctangent formula
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    # Converts radians to degrees
    angle = abs(radians * 180.0 / np.pi)

    # Keeps angle in range 0–180°
    if angle > 180:
        angle = 360 - angle
    return angle