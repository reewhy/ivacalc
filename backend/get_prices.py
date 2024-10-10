try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

from pytesseract import Output
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10, 500)
fontScale = 2
fontColor = (0, 0, 0)
thickness = 2
lineType = 2


def get_grayscale(image):
    print(image)
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def ResizeWithAspectRatio(image, width=1280, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)


def calculate(value):
    if value == '':
        return None
    if value.startswith(','):
        return None
    if value.startswith('.'):
        return None
    if ',' in value:
        value = value.replace(',', '.')
    if ' ' in value:
        return None

    val = float(value)

    perc = (val * 22) / 100

    return str(val + perc)


def format(text):
    new_v = calculate(text)

    if new_v == None:
        return None

    return text + " = " + new_v


# If you don't have tesseract executable in your PATH, include the following:
#pytesseract.pytesseract.tesseract_cmd = r'/usr/share/tesseract-ocr'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

def process(name='IMG_20241010_223812.jpg'):
    print('Processing..')
    print(name)
    cropped_image = cv2.imread('../' + name)

    gray = get_grayscale(cropped_image)
    img = cv2.threshold(gray, 100, 205, cv2.THRESH_BINARY)[1]
    # Simple image to string
    d = pytesseract.image_to_data(img, config="-c tessedit_char_whitelist=0123456789., --psm 6",
                                  output_type=Output.DICT)

    n_boxes = len(d['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, format(d['text'][i]),
                    (x, y + 2),
                    font,
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)

    cv2.namedWindow('output', cv2.WINDOW_NORMAL)

    resize = ResizeWithAspectRatio(img)

    cv2.imwrite(f"../output.jpg", resize)

    f = open('../result.txt', "w")

    for i in range(n_boxes):
        tx = d['text'][i]
        if tx == '' or tx.startswith('.') or tx.startswith(','):
            continue
        f.write(tx)
        f.write('\n')

if __name__ == "__main__":
    process()