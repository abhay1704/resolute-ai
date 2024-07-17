import easyocr
from PIL import Image
import numpy as np
import sys

def preprocess_image(image_path):
    img = Image.open(image_path).convert('L')
    base_width = 800
    w_percent = (base_width / float(img.size[0]))
    h_size = int((float(img.size[1]) * float(w_percent)))
    img = img.resize((base_width, h_size), Image.ANTIALIAS)
    return np.array(img)

def ocr_image(image_path):
    try:
        img = preprocess_image(image_path)
        reader = easyocr.Reader(['en'])
        result = reader.readtext(img)
        text = ' '.join([res[1] for res in result])
        return text
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ocr_script.py <path_to_image>")
    else:
        image_path = sys.argv[1]
        result = ocr_image(image_path)
        print("Text found in the image:")
        print(result)
