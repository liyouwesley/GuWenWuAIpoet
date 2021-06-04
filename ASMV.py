import re
import os
from displaymode import *
from breakdown import *

def replace(sent):#多次迭代unitreplace确保处理彻底
    while '' in sent[0]:
        sent=unitreplace(sent)
    return(sent)

def unitreplace(sentence):#basic sentence,list（原属于前ASMV）
    #m=float(len(re.findall(r'[A-Z]',displaymode(sentence))))#单句总字数
    #m=m*0.817**(m-1)#临时算法，连坐
    tt=0.0
    for i in sentence[1]:tt=tt+i
    for j in range(1,len(sentence[1])+1):
        n=len(re.findall(r'[A-Z]',displaymode(sentence)))#单词总字数
        sentence[1][j-1]=(sentence[1][j-1]/tt)*barrier(n,style='strict')
#trashcart模块
    for k in sentence[0]:
        kind=sentence[0].index(k)
        if k=='' and sentence[1][kind]==0.0:
            del sentence[0][kind]
            del sentence[1][kind]
    return(sentence)

def barrier(n,style):#单词增广限制模块，float单词总字数,str限制严格程度
    if style=='strict':
        if n==1:return(float(1))
        elif n==2:return(float(1.5))#1.5
        elif n==3:return(float(1.8))#1.8
        elif n==4:return(float(2))#2
        else:return(float(2.1))#2.1
    else:pass
    
'''sent1=[['Dz11','Z1Z1','W1','W2','B2'],[0.5,0.8,0.2,0.2,0.2]]
print(replace(sent1))
'''

def count(string):#combou模块
    a=len(string)
    b=len(breakdown(string))
    combou=int(a/b)
    return(combou)

def formerfill(sentence,prc):#this sentence is purified
    senth=[]
    sentt=[]
    sentht=[]
    prch=[]
    prct=[]
    prcht=[]
    #print(sentence)
    for i in sentence:
        bki=breakdown(i)
        senth.append(bki[0])
        sentt.append(bki[-1])
        sentht.append(bki[0]+bki[-1])
    for j in prc:
        bkj=breakdown(j)
        prch.append(bkj[0])
        prct.append(bkj[-1])
        prcht.append(bkj[0]+bkj[-1])
#以上为准备活动
    for i in range(0,len(sentence)):
        if sentht[i] in prcht:pass#无主确认
        else:
            k=sentence[i]
            kh=senth[i]
            kt=sentt[i]
            kht=sentht[i]
            for j in range(0,len(prc)):
                
                if prcht[j] in sentht:pass
                else:
                    #print('ok')？！
                    v=prc[j]
                    vh=prch[j]
                    vt=prct[j]
                    vht=prcht[j]
                    if kh==vh:
                        if kh in ['A','L']:pass
                        else:#追索子
                            for n in sentence:
                                if len(breakdown(n))==4:
                                    if n[1:3].upper()==kht:
                                        combou=count(n)
                                        single=n[0:2]+vt+n[3]
                                        sentence[sentence.index(n)]=single*combou#modification
                        single=breakdown(k)[0:-1]+vt
                        combou=count(k)
                        sentence[i]=single*combou#self-modification
                        break
    return(sentence)

def mainfill(sentence,per_RClist):#原装版
    pure=sentence[0]
    vale=sentence[1]
    ans1=formerfill(pure,per_RClist)
    ans=[]
    ans.append(pure)
    ans.append(vale)
    return(ans)

def varify(sent,prc):#原装list,list
    Z=[0,1,2,3,4,5,6,7,8,9]
    W=[0,1,2,3,4,5,6,7,8,9]
    B=[0,1,2,3,4,5,6,7,8,9]
    D=[0,1,2,3,4,5,6,7,8,9]
    Z=[0,1,2,3,4,5,6,7,8,9]
    #C=[0,1,2,3,4,5,6,7,8,9]
    V=[0,1,2,3,4,5,6,7,8,9]
    P=[0,1,2,3,4,5,6,7,8,9]
    E=[0,1,2,3,4,5,6,7,8,9]
    L=[0,1,2,3,4,5,6,7,8,9]
    for i in prc:
        if i[0]=='Z':Z.remove(int(i[-1]))
        elif i[0]=='W':W.remove(int(i[-1]))
        elif i[0]=='B':B.remove(int(i[-1]))
        elif i[0]=='D':D.remove(int(i[-1]))
        elif i[0]=='A':S.remove(int(i[-1]))
        elif i[0]=='V':V.remove(int(i[-1]))
        elif i[0]=='P':P.remove(int(i[-1]))
        elif i[0]=='E':E.remove(int(i[-1]))
        elif i[0]=='L':L.remove(int(i[-1]))
        else:pass
    for j in sent[0]:
        if j[0]=='Z':
            if int(j[-1]) in Z:Z.remove(int(j[-1]))
            else:
                single=breakdown(j)[:-1]+str(Z[0])
                combou=int(len(j)/len(breakdown(j)))
                sent[0][sent[0].index(j)]=single*combou
                del Z[0]
        elif j[0]=='W':
            if int(j[-1]) in W:W.remove(int(j[-1]))
            else:
                single=breakdown(j)[:-1]+str(W[0])
                combou=int(len(j)/len(breakdown(j)))
                sent[0][sent[0].index(j)]=single*combou
                del W[0]
        elif j[0]=='B':
            if int(j[-1]) in B:B.remove(int(j[-1]))
            else:
                single=breakdown(j)[:-1]+str(Z[0])
                combou=int(len(j)/len(breakdown(j)))
                sent[0][sent[0].index(j)]=single*combou
                del B[0]
        elif j[0]=='D':
            if int(j[-1]) in D:D.remove(int(j[-1]))
            else:
                single=breakdown(j)[:-1]+str(Z[0])
                combou=int(len(j)/len(breakdown(j)))
                sent[0][sent[0].index(j)]=single*combou
                del D[0]
        elif j[0]=='A':
            if int(j[-1]) in A:A.remove(int(j[-1]))
            else:
                single=breakdown(j)[:-1]+str(Z[0])
                combou=int(len(j)/len(breakdown(j)))
                sent[0][sent[0].index(j)]=single*combou
                del A[0]
        elif j[0]=='V':
            if int(j[-1]) in V:V.remove(int(j[-1]))
            else:
                single=breakdown(j)[:-1]+str(Z[0])
                combou=int(len(j)/len(breakdown(j)))
                sent[0][sent[0].index(j)]=single*combou
                del V[0]
        elif j[0]=='P':
            if int(j[-1]) in P:P.remove(int(j[-1]))
            else:
                single=breakdown(j)[:-1]+str(Z[0])
                combou=int(len(j)/len(breakdown(j)))
                sent[0][sent[0].index(j)]=single*combou
                del P[0]
        elif j[0]=='E':
            if int(j[-1]) in E:E.remove(int(j[-1]))
            else:
                single=breakdown(j)[:-1]+str(Z[0])
                combou=int(len(j)/len(breakdown(j)))
                sent[0][sent[0].index(j)]=single*combou
                del Z[0]
        elif j[0]=='L':
            if int(j[-1]) in L:L.remove(int(j[-1]))
            else:
                single=breakdown(j)[:-1]+str(Z[0])
                combou=int(len(j)/len(breakdown(j)))
                sent[0][sent[0].index(j)]=single*combou
                del L[0]
        else:pass
    return(sent)

#print(['Z0Z0', 'V0', 'Pz00', 'W0', 'Z9', 'V9', 'Pz99'])
#print(['Z1','V1','W1','W1','B2'])
#print(formerfill(['Z0Z0', 'V0', 'Pz00', 'W0', 'Z9', 'V9', 'Pz99'],['Z1','V1','W1','W1','B2']))
#print(mainfill([['Z1Z1', 'V0', 'Pz10', 'W0', 'Z9', 'V9', 'Pz99'],[0.1,0.1,0.1,0.1,0.1,0.1,0.4]],['Z1','V1','P7','Z2','B2']))
#print(varify([['W0','W0','W0','W0','W0'],[0.2,0.2,0.2,0.2,0.2]],['W3','W4','Z5']))

def datasetcleaner():
    with open('dataset.txt','r',encoding='utf-8') as file:data=file.readlines()
    j=0
    while j<len(data):
        print(str(j)+'/'+str(len(data)))
        i=data[j][:-1]
        data[j]=i
        try:
            a=re.split(r'|',i)[0]
            b=re.split(r'|',i)[1]
            x=re.split(r':',i)[-1]
        except:
            del data[j]
            continue
        try:
            a=re.split(r'[\u4e00-\u9fa5]+',a)
            aa=''
            for i in a:aa=aa+i
            b=re.split(r'[\u4e00-\u9fa5]+',b)
            bb=''
            for i in b:bb=bb+i
            if aa+bb=='':pass
            else:
                del data[j]
                continue
            x=re.split(r'\d+',x)
            if x==['', '.', '']:pass
            else:
                del data[j]
                continue
        except:
            del data[j]
            continue
        j+=1
    data=set(data)
    data=list(data)
    data.sort()
    with open('dataset.txt','w') as file:
        for i in data:file.write(i+'\n')
                               
#datasetcleaner()
