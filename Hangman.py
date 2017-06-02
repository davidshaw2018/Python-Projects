'''
Created on May 25, 2017

@author: davidshaw
'''

def add(x,y):
    if y==0:
        return x

    else:
        return add(x+1,y-1)

print (add(3,4))




