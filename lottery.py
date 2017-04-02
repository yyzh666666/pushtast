#coding:utf-8
import random
import time

#双色球彩票
def lottery():
    redball=range(1,34)
    blueball=range(1,16)
    result=[]
    result=random.sample(redball,6)  #选6个红球
    result=sorted(result)
    result.append(random.choice(blueball)) #蓝球
    return result
a=time.strftime("%Y-%m-%d %H %M %S", time.localtime())
a=str(a)+".txt"
f=open(a,"w")   #以时间函数命名文件
for  i in range(100):
    once=str(lottery())+"\n"
    f.write(once)
print "OK"
f.close() 

 
    
        
       
    
