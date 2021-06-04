import os
import re
import time
import copy
from xer import *
from SATY import *
from ASMV import *
from STARTUP import *
from breakdown import *
import jieba.posseg as pseg
#from formerfill import *
#from resemblence import *
#from displaymode import *
#from RC import *

def admit(m,c,x):#  m最大过审量;c成熟点；x当前迭代次数__int,int,int
    if float(0)<=float(x)<=float(c/2):
        ans=int((8*m*x*x)/(4*c*c))
    elif float(c/2)<=float(x):
        ans=int( m-(8*m*(x-c)**2)/(4*c*c))
    else:
        ans=int(7700)#error exception
    if ans<=0:return(0)
    else:return(ans)

def eliminator(sentlist,prc,time,peak,mature):#淘汰子：list,list,int,int,int
    satylist=[]   
    for i in sentlist:
        #print(str(sentlist.index(i))+':     '+str(i))lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
        satylist.append(saty(i,prc,time,mature))
    for j in range(0,len(sentlist)-admit(peak,mature,time)):
        pos=satylist.index(min(satylist))
        del satylist[pos]
        del sentlist[pos]
    return(sentlist)

def mutator(sent):#原版list
    f1=[]
    tpst=[]
    for j in sent[0]:
        tpst.append(j[0])
        tpst=list(set(tpst))
    for i in sent[0]:
        i0=i[0]
        f1.append(ignore(sent,i))
        i0=i[0]
        #print('flag          '+str(f1))#flagflagflagflag
        if i0=='L':pass
        else:
            f1.append(augment(sent,i))
        if i0=='Z':
            if int(str(time.time())[-1])<10:f1.append(der(sent,i))
            if 'V' in tpst:f1.append(per(sent,i))
        elif i0=='W' or i0=='V':
            if int(str(time.time())[-1])<8:f1.append(aer(sent,i))
        elif i0=='B' or i0=='E':
            f1.append(der(sent,i))
            if int(str(time.time())[-1])<8:f1.append(aer(sent,i))
        elif i0=='D':
            if int(str(time.time())[-1])<8:f1.append(aer(sent,i))
            if 'Z' in tpst or 'B' in tpst or 'E' in tpst:
                if int(str(time.time())[-1])<5:f1.append(dz(sent,i))
        elif i0=='A':
            if 'V' in tpst or 'W' in tpst or 'D' in tpst or 'P' in tpst:
                if int(str(time.time())[-1])<5:f1.append(dz(sent,i))
        elif i0=='P':
            if int(str(time.time())[-1])<8:f1.append(aer(sent,i))
            if 'Z' in tpst:
                if int(str(time.time())[-1])<5:f1.append(dz(sent,i))
        else:pass#L
    return(f1)

#print(mutator([['Z1'],[0.5]]))


def darwin(sentlist,prc,out,peak,mature):#list list int输出结果数
    time=2
    f1=[]
    while 1==1:
        #print('\n'+'NOTING-PRESENT TIME : '+str(time)+'\n')
        #print('f1:'+str(f1))#DEBUGGER
        f1=[]
        for i in range(0,len(sentlist)):
            #print(sentlist[i])
            sentlist[i]=mainfill(sentlist[i],prc)
            sentlist[i]=replace(sentlist[i])
            f1.extend(mutator(sentlist[i]))
        for ii in f1:
            ii=replace(ii)
            mode=formerfill(ii[0],prc)
            lat=ii[1]
            f1[f1.index(ii)]=replace([mode,lat])
        #print(f1)
        sentlist=eliminator(f1,prc,time,peak,mature)
        time=time+1
        if time>mature and len(f1)<=out:return(sentlist)

def main():
    m=5
    p=10
    o=7
    prc=['L0','Z1','Aw90']
    #m=int(input("成熟点？"))
    #p=int(input("运算峰值"))
    #o=int(input("结果数？"))
    #prc=list(input("prc列表？"))
    sentlist=startup(prc)
    ans=darwin(sentlist,prc,o,p,m)
    for i in range(0,len(ans)):print('ANSWER '+str(i+1)+': '+str(ans[i]))

#for i in range(1,2):main()

def DEMOsentence(m,p,o,prc):#外部端口
    sentlist=startup(prc)
    ans=darwin(sentlist,prc,o,p,m)[0]
    return(ans[0])
'''****************************我是分隔线****************************'''
#print(DEMOsentence(5,10,7,['L0','Z1','Aw90']))
from imagine import DEMOimagine
#print(DEMOsentence(5,10,7,['L0','Z1','Aw90']))
#print(DEMOimagine(3,'不知'))
def ran():
    return(int(str(time.time())[-1]))
def tag(txt):#str
    words=pseg.cut(txt)
    for w in words:
        #print(str(w.flag)+' '+str(txt),end='__')
        return(str(w.flag))

def typ(txt):#str
    raw=txt[0]
    if raw=='n' or raw=='m' or raw=='r':
        if int(str(time.time())[-1])<4:return('ZBEPVA')
        else:return('ZBEP')#V为名词活用为动词、A为名词作状语
    elif raw=='v':
        if int(str(time.time())[-1])<4:return('VWZBEP')
        else:return('VW')#ZBEP为动词活用为名词
    elif raw=='a':
        if int(str(time.time())[-1])<4:return('DPV')
        return('DP')#V为形容词活用为动词
    elif raw=='d':return('AP')
    elif raw=='c':return('L')
    else:return('ZBEP')#本应为X
#mess=str(input("?"))
#print('tag: '+str(tag(mess)))
#print('typ: '+str(typ(mess)))

def typ_fake(txt):#str
    if txt=='ZBEP':
        r=ran()
        if r==1 or r==2 or r==7:return('Z')
        elif r==3 or r==4 or r==8:return('B')
        elif r==5 or r==6 or r==9:return('E')
        else:return('P')
    elif txt=='VW':
        r=ran()
        if float(r)<3.0:return('V')
        else:return('W')
    elif txt=='DP':
        r=ran()
        if float(r)<8.0:return('D')
        else:return('P')
    elif txt=='AP':
        r=ran()
        if float(r)<8.0:return('A')
        else:return('P')
    elif txt=='L':return('L')
    else:return('X')

def sentfill(ori_sent,A,B):#list,str,str.七言模式单句填充
    sent=copy.deepcopy(ori_sent)
    #print(A)
    As=DEMOimagine(99,A)[1:]
    Bs=DEMOimagine(99,B)[1:]
    cdd=list(set(As+Bs))
    #print(cdd)
    for ii in range(0,len(sent)):
        i=sent[ii]
        #print('i: '+str(i))
        if str(i[-1])=='0' or str(i[-1])=='1' or str(i[-1])=='2' or str(i[-1])=='3' or str(i[-1])=='4' or str(i[-1])=='5' or str(i[-1])=='6' or str(i[-1])=='7' or str(i[-1])=='8' or str(i[-1])=='9':pass
        else:continue#跳过已填之词
        for j in cdd:
            #print('  j: '+str(j))
            if len(j)==len(re.findall(r'[A-Z]',i)):pass#长度符合要求
            else:continue
            #print(i[0]+' '+str(list(typ(tag(j)))))
            if i[0] in list(typ(tag(j))):pass#类型相符
            else:continue
            sent[ii]=j
            cdd.remove(j)
    return(sent)
    
#print(sentfill(['Z0','儿童','B9','父母','E0'],'儿童','父母'))
#print(DEMOimagine(8,'一日不见'))
def main7unit():
    #title=str(input('（七言绝句模式）请输入标题'))
    title='万邦'
    titles=DEMOimagine(8,title)
    tgtles=[]
    tptles=[]
    tptles_fake=[]
    for i in titles:tgtles.append(tag(i))
    for i in tgtles:tptles.append(typ(i))
    for i in tptles:tptles_fake.append(typ_fake(i))
    '''print(titles)
    print(tgtles)
    print(tptles)
    print(tptles_fake)'''
    A1=tptles_fake[0]
    B1=tptles_fake[1]
    A2=tptles_fake[2]
    B2=tptles_fake[3]
    A3=tptles_fake[4]
    B3=tptles_fake[5]
    A4=tptles_fake[6]
    B4=tptles_fake[7]
    if A1==B1:
        A1=A1+'8'
        B1=B1+'9'
    else:
        A1=A1+'9'
        B1=B1+'9'
    if A2==B2:
        A2=A2+'8'
        B2=B2+'9'
    else:
        A2=A2+'9'
        B2=B2+'9'
    if A3==B3:
        A3=A3+'8'
        B3=B3+'9'
    else:
        A3=A3+'9'
        B3=B3+'9'
    if A4==B4:
        A4=A4+'8'
        B4=B4+'9'
    else:
        A4=A4+'9'
        B4=B4+'9'
    #print('finished')
    A1=A1*len(titles[0])
    B1=B1*len(titles[1])
    A2=A2*len(titles[2])
    B2=B2*len(titles[3])
    A3=A3*len(titles[4])
    B3=B3*len(titles[5])
    A4=A4*len(titles[6])
    B4=B4*len(titles[7])
    #tptles_fake_ready=[A1,B1,A2,B2,A3,B3,A4,B4]
    #print(tptles_fake_ready)
    try:sent1=DEMOsentence(5,10,7,[A1,B1])
    except:sent1=[]
    try:sent2=DEMOsentence(5,10,7,[A2,B2])
    except:sent2=[]
    try:sent3=DEMOsentence(5,10,7,[A3,B3])
    except:sent3=[]
    try:sent4=DEMOsentence(5,10,7,[A4,B4])
    except:sent4=[]
    if sent1==[]:
        if sent2==[]:sent1=copy.deepcopy(sent4)
        else:sent1=copy.deepcopy(sent2)
    if sent2==[]:
        if sent1==[]:sent2=copy.deepcopy(sent3)
        else:sent2=copy.deepcopy(sent1)
    if sent3==[]:
        if sent4==[]:sent3=copy.deepcopy(sent1)
        else:sent3=copy.deepcopy(sent4)
    if sent4==[]:
        if sent3==[]:sent4=copy.deepcopy(sent2)
        else:sent4=copy.deepcopy(sent3)
    #print(str(sent1)+'\n'+str(sent2)+'\n'+str(sent3)+'\n'+str(sent4))
    for i in range(0,6):
        if sent1[i]==A1:sent1[i]=titles[0]
        elif sent1[i]==B1:sent1[i]=titles[1]
        if sent2[i]==A2:sent1[i]=titles[2]
        elif sent2[i]==B2:sent2[i]=titles[3]
        if sent3[i]==A3:sent1[i]=titles[4]
        elif sent3[i]==B3:sent3[i]=titles[5]
        if sent4[i]==A4:sent1[i]=titles[6]
        elif sent4[i]==B4:sent4[i]=titles[7]
    #print(str(sent1)+'\n'+str(sent2)+'\n'+str(sent3)+'\n'+str(sent4))
    sent1=sentfill(sent1,titles[0],titles[1])
    sent2=sentfill(sent2,titles[2],titles[3])
    sent3=sentfill(sent3,titles[4],titles[5])
    sent4=sentfill(sent4,titles[6],titles[7])
    sent11=''
    sent22=''
    sent33=''
    sent44=''
    for i in sent1:sent11=sent11+i
    for i in sent2:sent22=sent22+i
    for i in sent3:sent33=sent33+i
    for i in sent4:sent44=sent44+i
    if len(sent11)>7:sent11=sent11[:7]
    if len(sent22)>7:sent22=sent22[:7]
    if len(sent33)>7:sent33=sent33[:7]
    if len(sent44)>7:sent44=sent44[:7]
    print('   '+title)
    print(sent11+'，')
    print(sent22+'。')
    print(sent33+'，')
    print(sent44+'。')

def main7():
    try:main7unit()
    except:print('exception')
    
while 1==1:
    time.sleep(0)
    main7()
    


