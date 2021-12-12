print()
#def plus(*nums):
#    res = 0
#    for i in nums:
#        res += i
#		#print(res)
#    return res


#res = plus(5,3,2,1,10)
#print(res)


#dt = {'sep':' # ', 'end':'\n\n'}
#print('hello', 'world', **dt)


#def fun(**settings):
#    settings.setdefault('name', 'Hello')
#    settings.setdefault('attack', 50)
#    settings.setdefault('defense', 0)
#    settings.setdefault('hp', 150)
#    print(settings)

#fun(name='sky', attack=100, hp=500)


#def fun(*args, **kwargs):
#    print(args, kwargs, sep='\n')
#fun(1,2,3, name='sky', attack=100, hp=500)


#def fun(a, *args, kw1, **kwargs):
#    print(a, args, kw1, kwargs, sep=' # ')
#fun(1, 2, 3, 4, 5, kw1=6, g=7, f=8, l=9)


#!uer/bin/env python3
# -*- coding: utf-8 -*-
import os

filepath = 'D:/python-training/1.jpg'
size = (os.path.getsize(filepath))/1000
print('%s = %d kbytes' %(filepath, size))





print('運行結束... \n')