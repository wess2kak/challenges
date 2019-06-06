from os import path
from PIL import Image, ImageFont, ImageDraw

IMAGE_X = 2400
IMAGE_Y = 828
PADDING = 100
WIDTH_OFFSET = -10  # because of italics
DESCENDING_CHARACTERS = ['y', 'p', 'g', 'j', 'q']


def supreme_logo(message):
    """Create a Supreme style logo using input string and PIL"""
    if not path.exists('futura.otf'):
        return print("failed: missing 'futura.otf' in the same directory")
    w, h = None, None
    font, font_size = None, 600
    message_fits = False

    new_image = Image.new('RGB', (IMAGE_X, IMAGE_Y), (237, 28, 36))
    d = ImageDraw.Draw(new_image)
    while not message_fits:
        font = ImageFont.truetype('futura.otf', font_size)
        w, h = d.textsize(message, font=font)
        if w >= IMAGE_X - PADDING or h >= IMAGE_Y - PADDING:
            font_size -= 1
        else:
            message_fits = True

    descender = False
    for letter in DESCENDING_CHARACTERS:
        if letter in message:
            descender = True
    d.text((((IMAGE_X - w) / 2) + WIDTH_OFFSET, ((IMAGE_Y - h) / 2) + -50 if descender else
            ((IMAGE_Y - h) / 2) + -75), message, font=font, fill=(255, 255, 255))
    new_image.save('supreme_' + message.replace(' ', '').replace('/', '').replace('*', '') + '.png',
                   'PNG', optimize=True)


words = ["Supreme"]
for word in words:
    if not path.exists('supreme_' + word.replace(' ', '').replace('/', '').replace('*', '') + '.png'):
        supreme_logo(word)
    else:
        print('skipped', word)
