import os, cv2\
import pytesseract
import numpy as np
from PIL import Image

src_path = 'C:\Users\subshna\Downloads\Excel Redline Markup-1.pdf'

def image2text(filepath):
    img = cv2.imread(filepath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((1,1), np.uint8)

    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    cv2.imwrite(src_path + 'remove_noise.png', img)

    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite(src_path + 'thres.png', img)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
    result = pytesseract.image_to_string(Image.open(src_path + 'thres.png'))

    return result