from PIL import Image,ImageFilter

with Image.open("stay.jpg") as original:
    pic_gray = original.convert("L")
    pic_gray.save("bw_pic.jpg")
    pic_blured = original.filter(ImageFilter.BLUR)
    pic_up = original.transpose(Image.ROTATE_90) 
    pic_gray.show()