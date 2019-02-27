
import hashlib
import time
from PIL import Image
import os
import numpy as np

import math

class vectorCompare:
    def magnitude(self,im):
        return np.linalg.norm(im)
    
    def relation(self,test,im1):
        test=test.flatten()
        im1=im1.flatten()
        test=test/255
        im1=im1/255
        #print test
        #print im1
        #print test.shape
        if im1.shape[0]<test.shape[0]:
            test=np.delete(test,list(np.arange(0,test.shape[0]-im1.shape[0])))
        if im1.shape[0]>test.shape[0]:
            im1=np.delete(im1,list(np.arange(0,im1.shape[0]-test.shape[0])))
        product=np.dot(im1.T,test)
        return product/(self.magnitude(test)*self.magnitude(im1))
        #sim=0.5+0.5*cos

        #return sim
'''    print im1.shape[1]
        if test.shape[1]<im1.shape[1]:
            im1=np.delete(im1,list(np.arange(test.shape[1],im1.shape[1])),axis=1)
            test=test/255
            im1=im1/255
            test=test.reshape(test.shape[0]*test.shape[1],1)
            im1=im1.reshape(im1.shape[0]*im1.shape[1],1)
            product=np.dot(im1.T,test)
'''

        
        
#def builtV(im):
    
#    count = 0
#    data={}
#    for i in im.getdata():
#        data[count]=i
#        count += 1
#    return data

v = vectorCompare()

iconset = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


imageset=[]
a=[]

for letter in iconset:
    for img in os.listdir('./iconset/%s/'%(letter)):
        if img !="Thumbs.db" and img != ".DS_Store":
            a=np.array(Image.open("./iconset/%s/%s"%(letter,img)))
        imageset.append({letter:a})#字典里面不是什么都能包含

#print imageset
#for letter in iconset:
#    for img in os.listdir('./iconset/%s/'%(letter)):
#        temp = []
#        if img != "Thumbs.db" and img != ".DS_Store": # windows check...
#            temp.append(buildvector(Image.open("./iconset/%s/%s"%(letter,img))))
#        imageset.append({letter:temp})
#初始化图片
im=Image.open("captcha.gif")
im.convert("P")

#im.show()
#print (im)
#print im.size

im2=Image.new("P",im.size,255)
#im2.save('D:\\1.gif')

for x in range(im.size[0]):
    for y in range(im.size[1]):
        pix=im.getpixel((x,y))
        if pix==220 or pix==227:
            im2.putpixel((x,y),0)
#im2.show()
#im2.save('D:\\1.gif')


#剪切图片
#im3=im2.crop((0,0,42,22))
#im3.show()

#找单词的个数
inletter=False
foundletter=False
start=0
end=0
letters=[]

for x in range(im2.size[0]):
    for y in range(im2.size[1]):
        pix=im2.getpixel((x,y))
        if pix!=255:
            inletter=True
    if foundletter==False and inletter==True:
            foundletter=True
            start=x
    if foundletter==True and inletter==False:
            foundletter=False
            end=x
            letters.append((start,end))
    inletter=False
    
    
#print letters


#裁剪照片
count=0
for letter in letters:
    m=hashlib.md5()
    im3=im2.crop((letter[0],0,letter[1],im2.size[1]))
#保存图片
#m.update("%s%s"%(time.time(),count))
#im3.save("./%s.gif"%(m.hexdigest()))
#count +=1
    guess=[]
    for image in imageset:
        for x,img in image.iteritems():
            if img != []:
                guess.append((v.relation(np.array(im3),img),x))
                #print x+';'
    guess.sort(reverse=True)
    print guess[0]
