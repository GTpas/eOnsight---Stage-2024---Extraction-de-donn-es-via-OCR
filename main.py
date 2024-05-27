import json
from utils.ocr import extract_text
import cv2
import numpy as np

def convert_numpy_types(data):
    if isinstance(data, dict):
        return {key: convert_numpy_types(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_numpy_types(element) for element in data]
    elif isinstance(data, np.integer):
        return int(data)
    elif isinstance(data, np.floating):
        return float(data)
    elif isinstance(data, np.ndarray):
        return data.tolist()
    else:
        return data

def main():
    image_path = 'data/Genova.png'
    output_path = 'TextOutput/textOutputResult.json'

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    preprocessed_image = 'data/preprocessed_image.png'
    cv2.imwrite(preprocessed_image, gray)

    text_data = extract_text(preprocessed_image)

    text_data = convert_numpy_types(text_data)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(text_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()

