import copy
from breakdown import *

def der(orisent,tar):#原装list,str
    sent=copy.deepcopy(orisent)
    pos=sent[0].index(tar)
    bktar=breakdown(tar)
    sent[0].insert(pos,'D'+bktar.lower()+'0')
    sent[1][pos]=sent[1][pos]*1.07
    sent[1].insert(pos,1.0)
    return(sent)

def aer(orisent,tar):#原装list,str
    #print('aer ori sent'+str(orisent))
    sent=copy.deepcopy(orisent)
    pos=sent[0].index(tar)
    bktar=breakdown(tar)
    if tar[0]=='P' or tar[0]=='D':sent[0].insert(pos,'A'+bktar[0].lower()+bktar[3].lower()+'0')
    else:sent[0].insert(pos,'A'+bktar.lower()+'0')#A修饰P的情况为双重修饰
    sent[1][pos]=sent[1][pos]*1.07
    sent[1].insert(pos,1.0)
    return(sent)
#print(aer([['Z1','B1','Dz12'],[0.5,0.5,0.3]],'B1'))
def per(orisent,tar):#原装list,str
    sent=copy.deepcopy(orisent)
    pos=sent[0].index(tar)
    bktar=breakdown(tar)
    sent[0].insert(pos,'P'+bktar.lower()+'0')
    sent[1][pos]=sent[1][pos]*1.07
    sent[1].insert(pos,1.0)
    return(sent)

def augment(orisent,tar):#原装list,str
    sent=copy.deepcopy(orisent)
    pos=sent[0].index(tar)
    orivaltar=sent[1][pos]
    newlen=len(tar+breakdown(tar))
    if newlen==2:
        newvaltar=1.5
        orivaltar=1
    elif newlen==3:
        newvaltar=1.8
        orivaltar=1.5
    elif newlen==4:
        newvaltar=2
        orivaltar=1.8
    elif newlen==5:
        newvaltar=2.1
        orivaltar=2
    else:
        newvaltar=2.1
        orivaltar=2.1
    hit=0.64603445
    orivaltar=orivaltar*hit
    newvaltar=newvaltar*hit
    #newvaltar=(orivaltar/len(tar))*len(tar+breakdown(tar))
    if tar[0] in ['A','D','P']:
        ter=tar[1:3].upper()
        for i in sent[0]:
            if breakdown(i)==ter:
                sent[1][sent[0].index(i)]=(sent[1][sent[0].index(i)]/orivaltar)*newvaltar
                break
    sent[0][pos]=tar+breakdown(tar)
    sent[1][pos]=newvaltar
    return(sent)

#print(augment([['Z1','B1','Dz12'],[0.5,0.5,0.3]],'Z1'))

def ignore(orisent,tar):#原装list,str
    #print('人家本来是这样的： '+str(orisent))
    sent=copy.deepcopy(orisent)
    pos=sent[0].index(tar)
    orivaltar=sent[1][pos]
    newvaltar=(orivaltar/len(tar))*len(tar[:-len(breakdown(tar))])
    if tar[0] in ['A','D','P']:
        ter=tar[1:3].upper()
        for i in sent[0]:
            if breakdown(i)==ter:
                sent[1][sent[0].index(i)]=(sent[1][sent[0].index(i)]/orivaltar)*newvaltar
                break
    sent[0][pos]=tar[:-len(breakdown(tar))]
    sent[1][pos]=newvaltar
    #print('ignore又干了好事：  '+str(sent))
    return(sent)

#print(ignore([['Z1','B1','Dz12'],[0.5,0.5,0.3]],'B1'))

def dz(orisent,tar):#原装list,str
    if len(tar)==4:pass
    else:return(orisent)#保护机制
    sent=copy.deepcopy(orisent)
    sant=[]
    ter=tar[1:3].upper()
    pos=sent[0].index(tar)
    val=sent[1][pos]*1.03
    del sent[0][pos]
    del sent[1][pos]
    #print(str(sent[0])+ ':'+str(ter))

    for i in sent[0]:
        if len(breakdown(i))==2:sant.append(i[:2].upper())
        else:sant.append((i[0]+i[3]).upper())
    #print(str(sant)+' '+str(ter)+' '+str(tar))
    pis=sant.index(ter)
    sent[1][pis]=sent[1][pis]*1.03
    sent[0].insert(pis,tar)
    sent[1].insert(pis,val)
    return(sent)

#print(dz([['Z1','B1','Dz12'],[0.5,0.5,0.3]],'Dz12'))


#[['Z1','Dz12','B1'],[0.5,0.5,0.3]],'Dz12'















