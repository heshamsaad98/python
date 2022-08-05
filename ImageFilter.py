from PIL import Image, ImageFilter

befor = Image.open("hesham.jpg")

after = befor.filter(ImageFilter.BLUR)

after.save("out.jpg")
