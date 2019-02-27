#得到图片的有效信息
from PIL import Image
im = Image.open("captcha.gif")
im.convert("P")
a=im.histogram()
print a

value={}
for i in range(len(a)):
    value[i]=a[i]
print value
for j,k in sorted(value.items(),key=lambda x:x[1],reverse=True)[:10]:
    print j,k

