import math
from PIL import Image
import numpy as np

im0=Image.open("0.gif")
im1=Image.open("test.gif")

'''def builtV(im):
    
    count = 0
    data={}
    for i in im.getdata():
        data[count]=i
        count += 1
    return data'''

topvalue=0
'''a={}
b={}
a=builtV(im0)
b=builtV(im1)'''
'''for word,count in builtV(im0).iteritems():
     if builtV(im1).has_key(word):
        topvalue +=count*builtV(im1)[word]

print topvalue'''


test=np.array(im1)
a=np.array(im0)
test=test/255
a=a/255
print test
print a
test=test.reshape(test.shape[0]*test.shape[1],1)
a=a.reshape(a.shape[0]*a.shape[1],1)
product=np.dot(a.T,test)
print product
'''
test=np.array(im1)
a=np.array(im0)
print test

#product=np.matmul(test,a)
lenth1=np.linalg.norm(test)
lenth2=np.linalg.norm(a)
lenth=lenth1*lenth2
cos=topvalue/lenth
sml=0.5+0.5*cos
print sml
#print product
'''
lenth1=np.linalg.norm(test)
lenth2=np.linalg.norm(a)
lenth=lenth1*lenth2
cos=product/lenth
sml=0.5+0.5*cos
print sml
print test.shape
