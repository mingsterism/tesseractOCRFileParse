# import pyscreenshot as ImageGrab
from PIL import ImageGrab
from io import BytesIO


if __name__ == "__main__":
    # part of the screen
    im=ImageGrab.grab(bbox=(10, 250, 3010, 1680)) # X1,Y1,X2,Y2
    with BytesIO() as f:
    	im.save(f, format='JPEG')
    	print(dir(f))
    	
    # print(dir(im))
    # bytes1 = im.tobytes()
    # print(len(bytes1))
    # # print(bytes1)
    # bytes2 = im.convert("RGB").tobytes()
    # print(len(bytes2))
    # print(len(im))
    # print(im1.size)
    # im.show()
#-#