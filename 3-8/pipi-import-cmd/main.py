
from PIL import Image

amir = Image.open('/Users/hothaifa/Documents/amir.jpg')

age = int(input('enter your age ::'))

if age > 18:
    amir.show()
