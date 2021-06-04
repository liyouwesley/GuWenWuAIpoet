
try:
    with open('learnovo_master_I\dataset.txt','r',encoding='utf-8') as file:data=file.readlines()
except FileNotFoundError:
    with open('dataset.txt','r',encoding='utf-8') as file:data=file.readlines()
for i in range(0,len(data)):data[i]=data[i][:-1]

def trace(location,tree):#location as int
    track=tree
    forelocation=str(location)[0:-1]
    lastlocation=str(location)[len(str(location))-1]
    
    for i in forelocation:
        i=int(i)
        track=track[i*2-1]
    
    subject=str(track[int(lastlocation)*2-2])#subject is what location is talking about
    #except:subject='白云'
        #print(track,end='  ;  ')
        #print(str(int(lastlocation)*2-2))
    prospect=(track[int(lastlocation)*2-1])#prospect is where subject may lead to according to the current tree
    #except:prospect='白云'
    return([subject,prospect])#a list containing two str

def read(subject):#subject as str
    H=int((len(data))/2)
    footprint=[-1,len(data)+1]
    while 1==1:
        if data[H][:len(subject)]==subject:break#subject found
        footprint.append(H)
        footprint.sort()
        compare=[data[H],subject]
        compare.sort()
        if compare.index(subject)==0:H=int((H+footprint[footprint.index(H)-1])/2)
        else:H=int((H+footprint[footprint.index(H)+1])/2)#应向后
    message=[data[H]]
    while 1==1:
        H=H+1
        if float(H)>float(len(data)-1):break
        if data[H][:len(subject)]==subject:#读取全部符合者
            message.append(data[H])
        else:break
    #print(message)
    return(message)
        
def expend(location,decay,footprint,tree,tict):#decay as float
    footprint.append(trace(location,tree)[0])
    for i in read(trace(location,tree)[0]):
        #print(tree)
        #print(re.split(r':|\|',i)[1],end='  ;  ')
        #print(footprint)
        if re.split(r':|\|',i)[1] in footprint:pass#print('pass')
        else:
            lock=re.split(r':|\|',i)[1]
            key=re.split(r':',i)[1]
            tict[lock]=float(key)*decay
            trace(location,tree)[1].append(lock)
            trace(location,tree)[1].append([])
            

import re
import os
import time
#启动子
def main():
    mini=int(input("Outcome number?"))
    while 1==1:
        start=str(input("Starting point?"))
        tree=[start,[]]
        tict={start:1}
        footprint=[start]
        location=1
        expend(location,tict[trace(location,tree)[0]],footprint,tree,tict)
        
        location=11
        safe=0
        while safe<10:
            safe+=1#安全措施，防止套娃
            if location==1:break#主循环跳出
            expend(location,tict[trace(location,tree)[0]],footprint,tree,tict)
            while trace(location,tree)[0] in footprint:
                #print(tree)
                prospect=trace(location,tree)[1]
                future=[]
                for i in prospect:
                    if prospect.index(i)%2==1 or i in footprint:pass
                    else:future.append(i)
                if len(future)==0:
                    if location==1:break#主循环跳出
                    location=int(str(location)[:-1])
                else:
                    for k in future:
                        if k==[]:del future[future.index(k)]
                    location=int(str(location)+str(int((prospect.index(future[0])+2)*0.5)))
        
        tict_key=[]
        tict_value=[]
        for i in tict:#preparation for orderly output
            tict_key.append(str(i))
            tict_value.append(int(tict[i]))
        for i in range(1,mini+1):
            try:out_value=max(tict_value)#防止结果不足outcome number
            except:break
            out_index=tict_value.index(out_value)
            out_key=tict_key[out_index]
            print(out_key+':'+str(out_value))
            del tict_value[out_index]
            del tict_key[out_index]
#main()
def DEMOimagineunit(outcomenum,startpoint):#外部端口单元
    mini=int(outcomenum)
    while 1==1:
        start=str(startpoint)
        tree=[start,[]]
        tict={start:1}
        footprint=[start]
        location=1
        expend(location,tict[trace(location,tree)[0]],footprint,tree,tict)

        location=11
        safe=0
        while safe<10:
            #print(safe)
            try:
                safe+=1#安全措施，防止套娃
                if location==1:break#主循环跳出
                if len(str(tree))>1000:break
                expend(location,tict[trace(location,tree)[0]],footprint,tree,tict)
                while trace(location,tree)[0] in footprint:
                    prospect=trace(location,tree)[1]
                    future=[]
                    for i in prospect:
                        if prospect.index(i)%2==1 or i in footprint:pass
                        else:future.append(i)
                    if len(future)==0:
                        if location==1:break#主循环跳出
                        location=int(str(location)[:-1])
                    else:
                        for k in future:
                            if k==[]:del future[future.index(k)]
                        location=int(str(location)+str(int((prospect.index(future[0])+2)*0.5)))
            except:break
        #print('prep')
        tict_key=[]
        tict_value=[]
        for i in tict:#preparation for orderly output
            tict_key.append(str(i))
            tict_value.append(int(tict[i]))
        ans=[]
        for i in range(1,mini+1):
            try:out_value=max(tict_value)#防止结果不足outcome number
            except:break
            out_index=tict_value.index(out_value)
            out_key=tict_key[out_index]
            ans.append(out_key)
            del tict_value[out_index]
            del tict_key[out_index]
        return(ans)

def DEMOimagine(outcomenum,startpoint):#外部端口
    try:ans=DEMOimagineunit(outcomenum,startpoint)
    except:ans=[startpoint]
    return(ans)
#print(DEMOimagine(8,'一日不见'))
