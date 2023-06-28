from PIL import ImageGrab



def fullScreenShot():
    image = ImageGrab.grab()
    # can use image.save
    return image

def fullScreenShot(path):
    image = ImageGrab.grab()
    image.save(path)

# 捕捉特定区域的截图
# x1, y1, x2, y2 = 100, 100, 500, 500
# regionarea = (x1, y1, x2, y2)
# image = ImageGrab.grab(bbox=regionarea)
# image.save("region_screenshot.png")