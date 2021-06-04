import re
import os
import random
from breakdown import *
'''this module will contribute four seeds according to the per_RClist given'''

sent=[      [['Z0','W0'],[1.05,1.05]],     [['Z0','W0','B0'],[1.03,1.03,1.03]],     
            [['Z0','W0','B0','E0'],[1.025,1.025,1.025,1.025]],
            [['Z0','V0','Pz00'],[1.05,1.01,1.05]]                           ]

sentz=[      [['Z9','W9'],[1.05,1.05]],     [['Z9','W9','B9'],[1.03,1.03,1.03]],     
            [['Z9','W9','B9','E9'],[1.025,1.025,1.025,1.025]],
            [['Z9','V9','Pz99'],[1.05,1.01,1.05]]                           ]

def resemblence(lst):#list
    
    typelist=[]
    lentype=int(0)
    k=float(0.0)
    
    for i in lst:typelist.append(len(i))
    lentype=len(list(set(typelist)))
    k=1-lentype/len(lst)#字数雷同度
    
    tptplist=[]
    typetype=int(0)
    v=float(0.0)
    
    for j in lst:tptplist.append(breakdown(j)[0])
    typetype=len(list(set(tptplist)))
    v=1-typetype/len(lst)#成分类型雷同度
    
    if len(lst)>10:return(float(k*v))
    elif 7<len(lst)<=10:return(float(k*v/1.05))
    elif 5<len(lst)<=7:return(float(k*v/1.1))
    elif 3<len(lst)<=5:return(float(k*v/1.15))
    elif 2<len(lst)<=3:return(float(k*v/1.2))
    elif 1<len(lst)<=2:return(float(k*v/1.3))
    else:return(float(k*v/1.5))

def startup(per_RClist):#相似度越高，复句越多
    ans=[]
    mmm=resemblence(per_RClist)
    a=random.randint(1,4)
    b=random.randint(1,4)
    c=random.randint(1,4)
    d=random.randint(1,4)
    if mmm>0.4:#一个单句，三个复句
        ans.append(sent[a-1])
        ans.append(zhuanzhe(sent[c-1],sent[d-1]))
        ans.append(zhuanzhe(sent[a-1],sentz[b-1]))
        ans.append(zhuanzhe(sent[a-1],sentz[c-1]))
    elif 0.15<mmm<=0.4:#两个单句，两个复句
        ans.append(sent[a-1])
        ans.append(sent[b-1])
        ans.append(zhuanzhe(sent[c-1],sentz[d-1]))
        ans.append(zhuanzhe(sent[a-1],sentz[b-1]))
    elif 0.09<mmm<=0.15:#三个单句，一个复句
        ans.append(sent[a-1])
        ans.append(sent[b-1])
        ans.append(sent[c-1])
        ans.append(zhuanzhe(sent[b-1],sentz[d-1]))
    else:#四个单句
        ans.append(sent[a-1])
        ans.append(sent[b-1])
        ans.append(sent[c-1])
        ans.append(sent[d-1])
    return(ans)



def zhuanzhe(sent1,sent2):#list,list
    list3=[]
    list4=[]
    ans=[]
    a=sent1[0]
    b=sent1[1]
    c=sent2[0]
    d=sent2[1]
    for i in a:list3.append(i)
    for j in b:list4.append(j*0.9)
    list3.append('L0')#!!!!!!!!!!!!!!!!!!!!!【有待改善】
    list4.append(1)
    for ii in c:list3.append(ii)
    for jj in d:list4.append(jj*1.1)
    ans.append(list3)
    ans.append(list4)
    return(ans)

'''for i in startup(['W1','W1','W1','W1','B2']):
    print(i)'''
