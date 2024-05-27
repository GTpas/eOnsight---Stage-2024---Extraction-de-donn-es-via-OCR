import cv2

def load_image(image_path):
    return cv2.imread(image_path)

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray
