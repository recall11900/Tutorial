#导入Image类
from PIL import Image

#使用Image的对象读取图片
def get_chars(pi):
	
image_name='logo1.jpg'
img = Image.open(image_name)
#将图片转为灰度图像
img = img.convert('L')

w,h=img.size

if w>100:
	h= int((100/w) *h /2)
	w=100
img=img.resize((w,h),Image.ANTIALIAS)

#将缩小的图片像素点的颜色值转为字符并存放到列表
data =[]

chars=[' ',',','1','+','n','D','@','M']

for i in range(0, h):
	line=' '
	for j in range(0,w):
		pi =img.getpixel((j,i))

		for k in range(0,8):
			if pi<(k+1)*32:
				line+= chars[7-k]
				break
	data.append(line)


file = open(image_name+'.txt','w')
for d in data:
	print(d,file=file)

file.close()
print('转换成功')