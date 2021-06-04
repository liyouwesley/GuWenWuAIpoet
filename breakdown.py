import re
import os


lst=['Z','D','W','B','L','A','C','V','P','E']
def breakdown(name):#str
    ans=name[0]
    for i in range(1,len(name)):
        g=name[i]
        if g in lst:break
        else:ans=ans+g
    return(ans)#str
#print(breakdown('Az11Az11Az11'))
