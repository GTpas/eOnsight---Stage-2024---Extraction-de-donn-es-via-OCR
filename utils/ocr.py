import easyocr


def extract_text(image_path, min_confidence=0.8):
    reader = easyocr.Reader(['fr'])
    results = reader.readtext(image_path, detail=1)
    text_data = []
    for (bbox, text, confidence) in results:
        if confidence >= min_confidence:
            (top_left, top_right, bottom_right, bottom_left) = bbox
            left = min(top_left[0], bottom_left[0])
            top = min(top_left[1], top_right[1])
            width = max(top_right[0], bottom_right[0]) - left
            height = max(bottom_left[1], bottom_right[1]) - top
            text_data.append({
                'text': text,
                'left': left,
                'top': top,
                'width': width,
                'height': height,
                'confidence': confidence
            })
    return text_data
