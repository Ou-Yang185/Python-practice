from PIL import  Image,ImageDraw,ImageFont
 
def addNum(nub,filepath):
    img = Image.open(filepath)
    width,height = img.size
    fontSize =int(height/20)
    draw = ImageDraw.Draw(img)
    ttFont = ImageFont.truetype('C:\\windows\\Fonts\\Arial.ttf',fontSize);  #图片位置，及添加数字大小 
    draw.text((width-80,0),str(nub),(256,0,0),font=ttFont)     #确定显示的 位置，数字，颜色，字体
    del draw
    img.save('D:/360/qq_addNub.jpg')
    img.show()
if __name__ == '__main__':
    filepath='D:\\360\\test.jpg'
    addNum(1000000,filepath)