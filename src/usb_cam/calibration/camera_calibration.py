import numpy as np
import cv2
import glob

# Chessboard size
chessboard_size = (6, 9)  # Inner corners (columns, rows)
square_size = 0.01  # 1 cm

# Termination criteria for corner detection
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Prepare object points, like (0,0,0), (1,0,0), ..., (6,5,0)
objp = np.zeros((chessboard_size[0] * chessboard_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2) * square_size

# Arrays to store object points and image points from all images
objpoints = []  # 3D points in real-world space
imgpoints = []  # 2D points in image plane

# Images folder path
images_folder = 'images/*.jpg'  # Change this to your folder path and file extension

# Get images
images = glob.glob(images_folder)

# Loop through images
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)

    # If found, add object points, image points
    if ret:
        objpoints.append(objp)

        # Refine corner positions
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, chessboard_size, corners2, ret)
        cv2.imshow('img', img)
        cv2.waitKey(500)

cv2.destroyAllWindows()

# Perform camera calibration
ret, camera_matrix, distortion_coefficients, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# Print camera matrix and distortion coefficients
print("Camera Matrix:\n", camera_matrix)
print("\nDistortion Coefficients:\n", distortion_coefficients)

# Calculate rectification matrix and projection matrix
h, w = gray.shape[:2]
new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, distortion_coefficients, (w, h), 1, (w, h))
rectification_matrix, _ = cv2.getOptimalNewCameraMatrix(camera_matrix, distortion_coefficients, (w, h), 1, (w, h))

# Calculate projection matrix directly
projection_matrix = np.zeros((3, 4))
projection_matrix[:, :3] = rectification_matrix[:, :3]  # Copy rectification matrix to first 3 columns
projection_matrix[0, 3] = 13  # Adjust x-axis translation (tx)
projection_matrix[1, 3] = 16  # Adjust y-axis translation (ty)
projection_matrix[2, 3] = 1893  # Adjust z-axis translation (tz)

# Print rectification matrix and projection matrix
print("\nRectification Matrix:\n", rectification_matrix)
print("\nProjection Matrix:\n", projection_matrix)
