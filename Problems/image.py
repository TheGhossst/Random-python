import cv2
from google.colab.patches import cv2_imshow

def import_image(file_path):
    image = cv2.imread(file_path)
    return image

def convert_to_black_white(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return bw

def convert_to_grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def blur_image(image, kernel_size=(5, 5)):
    blurred = cv2.GaussianBlur(image, kernel_size, 0)
    return blurred

image_path = "/content/image_2024-05-03_145440972.png"
image = import_image(image_path)

bw_image = convert_to_black_white(image)

gray_image = convert_to_grayscale(image)

blurred_image = blur_image(image)

cv2_imshow(image)
cv2_imshow(bw_image)
cv2_imshow(gray_image)
cv2_imshow(blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()