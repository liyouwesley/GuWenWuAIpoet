import jieba
import re
import time

try:
    with open('dataset\dataset.txt','r') as file:data=file.readlines()
except:
    with open('dataset\dataset.txt','r',encoding='utf-8') as file:data=file.readlines()

for i in range(0,len(data)):data[i]=data[i][:-1]
#print(data)

def purify(shi):#single lined text as str
    shi=re.split(r'::',shi)[-1]#strip off titles,authors,etc
    shi=re.split(r'。|？|！',shi)#devided by lian,str to list
    for i in shi:
        if i=='\n' or i=='':del shi[shi.index(i)]#clear up
        else:
            shi[shi.index(i)]=re.split(r'，',i)#devided as ju
    for i in shi:
        for j in i:
            if j=='' or j=='\n':del shi[shi.index(j)]#clear up
            else:shi[shi.index(i)][i.index(j)]=list(jieba.cut(j))

    for lian in shi:#ci length>4,dispute
        for ju in lian:
            for ci in ju:
                if len(ci)>4:del shi[shi.index(lian)][lian.index(ju)][ju.index(ci)]
    return(shi)#list

def gps(subject):#str
    H=int((len(data))/2)
    footprint=[-1,len(data)]
    while 1==1:
        #print('gps: '+str(subject))
        #print('H: '+str(H)+'  fp: '+str(footprint)+'  lendata: '+str(len(data)))
        if H==len(data):return(int(float(H)-0.5))
        if data[H][:len(subject)]==subject:
            #print('subject found')
            return(H)
        footprint.append(H)
        footprint=list(set(footprint))
        footprint.sort()
        #print('距上一个脚印距离: '+str(float(H-footprint[footprint.index(H)-1]))+'; 距下一个脚印距离: '+str(float(footprint[footprint.index(H)+1]-H)))
        '''if float(H-footprint[footprint.index(H)+1])<1.5 and (H-footprint[footprint.index(H)+1])>0:
            return(float(H)+0.5)#int(H-1)forward
        elif float(footprint[footprint.index(H)+1]-H)<1.5 and (footprint[footprint.index(H)+1]-H)>0:
            return(float(H)-0.5)#H       backward'''#replace at below
        compare=[data[H],subject]
        compare.sort()
        #print('H: '+str(H)+'   fp: '+str(footprint))
        if H==0:return(float(-0.5))
        if compare.index(subject)==0:
            if float(H-footprint[footprint.index(H)+1])<1.5 and (H-footprint[footprint.index(H)+1])>0:
                #print('forward')
                return(float(H)-0.5)#int(H-1)forward
            H=int((H+footprint[footprint.index(H)-1])/2)#应向前
        else:
            if float(footprint[footprint.index(H)+1]-H)<1.5 and (footprint[footprint.index(H)+1]-H)>0:
                #print('backward')
                return(float(H)+0.5)#H       backward
            H=int((H+footprint[footprint.index(H)+1])/2)#应向后
    pass
    #return(H)

def writein(A,B,style):
    if len(re.split(r'[\u4e00-\u9fa5]+',A))==2 and len(re.split(r'[\u4e00-\u9fa5]+',B))==2:pass
    else:return()
    if style=='ju':style='0.8'
    elif style=='lian':style='0.9'
    elif style=='ci':
        #print(A+'|'+B+':'+'1.00')
        location=gps(str(A+'|'+B))
        if '.' in list(str(location)):data.insert(int(float(location)+0.5),A+'|'+B+':'+'1.00')
        else:data[location]=A+'|'+B+':'+'1.00'
        return()
    else:style='0.95'#shi
    location=gps(str(A+'|'+B))
    #print(data)
    #print(str(A+'|'+B)+':'+str(location))
    #print('')
    if '.' in list(str(location)):
        #print('insert'+str(A+'|'+B)+':'+str(int(float(location)+0.5))+'\n')
        data.insert(int(float(location)+0.5),A+'|'+B+':'+style)
    else:
        #print('int location: '+str(location))
        ori=float(re.split(r':',data[location])[-1])
        data[location]=A+'|'+B+':'+str(ori**float(style))

    
#with open('dataset\dataset.txt','a+') as file:file.write('Hello world')

#data=['白云|一片:0.006000000000000102', '白云|不知:0.0012222222222222424', '结成|冰入蒨:0.0012222222222222428']
#print(gps('结成|罗囊'))
buduifu=0
with open('message.txt','r+',encoding='utf-8') as file:
    content=file.readlines()
    for shi in content:
        print(content.index(shi)/len(content))
        try:
            shi=purify(shi)
        except:
            buduifu+=1
            print('有诗不对付'+str(buduifu))
            continue
        #print(shi)
        for liana in shi:
            lianapos=shi.index(liana)
            for jua in liana:
                juapos=liana.index(jua)
                for cia in jua:
                    ciapos=jua.index(cia)
                    for lianb in shi:
                        lianbpos=shi.index(lianb)
                        for jub in lianb:
                            jubpos=lianb.index(jub)
                            for cib in jub:
                                cibpos=jub.index(cib)
                                if ciapos==cibpos and lianapos==lianbpos and juapos==jubpos:
                                    #print('A:'+str(ciapos)+' B:'+str(cibpos))
                                    #print('CI')#a=b,same target
                                    writein(cia,cib,'ci')
                                elif juapos==jubpos and lianapos==lianbpos:
                                    #print('JU')
                                    #print('')
                                    writein(cia,cib,'ju')
                                elif lianapos==lianbpos:
                                    #print('LIAN')
                                    #print('')
                                    writein(cia,cib,'lian')
                                else:pass
                                    #print('SHI')
                                    #print('')#writein(cia,cib,'shi')          #shiapos=shibpos
                                #print(cia+': '+cib)

maxi=0.00
for i in data:
    try:
        cdd=float(re.split(r':',i)[-1])
        if float(cdd)>float(maxi):maxi=cdd
    except:
        print(str(i)+'1')
        del data[data.index(i)]
i=0
while i<=len(data)-1:
    try:
        a=re.split(r':',data[i])[:-1]
        b=re.split(r':',data[i])[-1]
        #print('a: '+str(a))
        data[i]=a[0]+':'+str(float(b)/maxi)
        i+=1
    except:
        print(str(len(data))+' '+str(i)+'2')
        del data[i]
i=0
while i<=len(data)-1:
    try:
        if float(re.split(r':',data[i])[-1])<0.7:
            del data[i]
        else:i+=1
    except:
        print(str(len(data))+' '+str(i)+'3')
        del data[i]
    
#for i in range(0,len(data)):print(str(i+1)+': '+str(data[i]))
with open('dataset\dataset.txt','w',encoding='utf-8') as file:
    for i in data:file.write(i+'\n')

