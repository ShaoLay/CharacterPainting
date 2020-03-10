from PIL import Image


WIDTH = 80
HEIGHT = 80
image_path = '1984475946.jpg'
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    im = Image.open(image_path)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    txt = ""

    for i in range(WIDTH):
        for j in range(HEIGHT):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print(txt)