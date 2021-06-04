import re
import os
from displaymode import *
from breakdown import *

def consaty(sentence,per_RClist):#list.list
    value_list=sentence[1]
    name_list=sentence[0]
    dis_sent=displaymode(sentence)#list → str
    sumsaty=0.00
    for i in per_RClist:#每个需求目标
        saty=1.00
        n=float(len(re.findall(r'[A-Z]',i)))
        t=float(len(re.findall(str(breakdown(i)),dis_sent)))
        nzbv=((t/n)**(0.05*t)-1)**2
        k=1-nzbv**0.5#字数满意度：每个词的字数满意度
        sumv=0.000
        v=0.00
        for j in sentence[0]:
            jj=breakdown(j)
            if jj==breakdown(i):
                bgh=name_list.index(j)
                v=v+sentence[1][bgh]#强调度（内容满意度）
            sumv=sumv+v
        saty=saty*k*sumv
        sumsaty=sumsaty+saty
    return(sumsaty)

def numsaty(sent,t,c,length=7):#list,int,int,int默认为七
    m=len(re.findall(r'[A-Z]',displaymode(sent)))#整句字数
    if m>length:n=length/m
    else:n=m/length
    #print('n:'+str(n))
    strict=(t/(c*1.5))**(1+2.3/c)
    return(n*(1-strict))
#for i in range(1,8):print(numsaty(['A','A','A','A','A'],i,5))
'''sentence=[['Dz11','Z1Z1','W1','W2','B2'],[0.2,0.2,0.2,0.2,0.2]]
rclist=['Z1Z1','W1','B2']
print(saty(sentence,rclist))'''

def saty(sentence,per_RClist,time,c):#list.list.index（迭代次数）.index（成熟点）
    return(consaty(sentence,per_RClist)*(numsaty(sentence,time,c))**3)#省略一参数

#print('saty:'+str(saty([['Z9Z9Z9', 'V9', 'Ap00', 'Pz90Pz90Pz90Pz90'], [12.600000000000001, 1.01, 1.0, 4.494000000000001]],['Z9','D9D9','V9','V8'],7,5)))
#print('consaty:'+str(consaty([['Z9Z9Z9', 'V9', 'Ap00', 'Pz90Pz90Pz90Pz90'], [12.600000000000001, 1.01, 1.0, 4.494000000000001]],['Z9','D9D9','V9','V8'])))
#print('numsaty:'+str(numsaty([['Z9Z9Z9', 'V9', 'Ap00', 'Pz90Pz90Pz90Pz90'], [12.600000000000001, 1.01, 1.0, 4.494000000000001]],7,5)))






