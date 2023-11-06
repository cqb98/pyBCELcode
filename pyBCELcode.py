#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string
import gzip


# In[2]:


ms="ABCDEFGHIJKLMNOPQRSTUVWXYZghijklmnopqrstuvwxyz$_"


# In[3]:


isLowerHex=lambda ch:True if (( '0'<=ch) and (ch<='9') ) or ( ('a'<=ch)and(ch<='f')) else False


# In[4]:


def encode(b:bytes,compress=False):
    
    if(compress):
        b=bytes(gzip.compress(b))
        #print(b)
    s="$$BCEL$$"
    for ch in b:
        if((ch >= ord('a')) and (ch <= ord('z'))):
            s+=chr(ch)
        elif((ch >= ord('A')) and (ch <= ord('Z')) ):
            s+=chr(ch)
        elif ((ch >= ord('0')) and (ch <= ord('9'))):
            s+=chr(ch)
        elif (ch == ord('_') ):
            s+=chr(ch)
        elif( ( 0<=ch) and (ch<48)):
            s+="$"+ms[ch]
        else:
            s+="$%02x"%(ch)
    
    return s

#print(encode(b"123",True))


# In[5]:


def decode(s:str,decompress=False):
    
    bs=[]
    length=len(s)
    indexstr="$$BCEL$$"
    p=s.index(indexstr)+len(indexstr)
    #print(s[p:])
    
    while(p<length):
        #print(s[p])
        if(s[p]!='$'):
            ch=ord(s[p])
            p+=1
        else:
            
            p+=1
            if isLowerHex(s[p]):
                p+=1
                ch=int(s[p-1]+s[p],16)
                p+=1
            else:
                #print(s[p])
                ch=ms.index(s[p])
                p+=1
        bs.append(ch)
    b=bytes(bs)
    if len(b)>2:
        if b[:2]==b"\x1f\x8b" :#maybe compress!
            if(decompress):
                #print(b)
                b=gzip.decompress(b)
            else:
                print("maybe compress,but you did not pass compress")
    return b
                


# In[6]:


a="$$BCEL$$$l$8b$I$A$A$A$A$A$A$AuQ$cbn$daP$Q$3d$X$M6$8e$J$8f$U$f2h$9e$7d$C$L$yu$L$ea$a6J7u$93$wD$e9$fa$fa$e6$8a$5e062$97$88$3f$ea$9a$N$ad$ba$e8$H$f4$a3$aa$ccu$9eRZK$9e$f1$9c$99s$e6$8c$fc$e7$ef$af$df$A$de$e1$8d$L$H$9b$$$b6$b0$ed$60$c7$e4$e76v$5d$U$b0gc$df$c6$BC$b1$afb$a5$df3$e4$5b$ed$L$G$ebCr$v$Z$w$81$8a$e5$c9$7c$S$ca$f4$9c$87$R$n$f5$m$R$3c$ba$e0$a92$f5$zh$e9oj$c6$b0$j$88d$e2_$f2t$y$d30Y$f8$a1$90$91$7f$7c$a5$a2$k$83$d3$X$d1$ed$GF$8cF0$e2W$dc$8fx$3c$f4$8f$XBN$b5Jb$g$x$P4$X$e3$cf$7c$9a$v$93I$Gw$90$ccS$n$3f$w$b3$a9d$e4$ba$86$eb$a1$E$d7$c6$a1$87$p$bc$m$7dr$r$bar$n$3d$bc$c4$x$86$8d$7f$e8$7bx$N$97a$f3$3f$$$Z$aa$P$a4$d3p$q$85f$a8$3d$40g$f3X$ab$J$99p$87R$df$X$8dV$3bx2C$97X$e4E0$bcm$3d$ea$Ot$aa$e2a$ef1$e1K$9a$I9$9b$R$a12$a5$a6$ce$ee$3fO$b9$90t$97M$bf$cd$3c90s$z$c55$aa$7c$ca$8cr$a1$f3$Dl$99$b5$3d$8a$c5$M$cc$a3L$d1$bb$Z$c0$3a$w$94$jT$ef$c9$3c$T$D$ea$3f$91$ab$e7W$b0$be$7e$87$f3$a9$b3Bq$99$e1$r$e2$WH$c5$u6$e9$cb$e8$962$d4$se$H5R$ba$dbP$86Eu$9d$aa$Nzm$e4$C$h$cf$yj42S$cdk$dfl$i$C$80$C$A$A"
a="$$BCEL$$$l$8b$I$A$a9$3fHe$C$ff342$G$A$d2cH$88$D$A$A$A"


# In[7]:


b=decode(a,True)
print(b)


# In[8]:


#f=open("1.class","wb")
#f.write(b)
#f.close()


# 
# define:
# 
# ```
# encode(b:bytes,compress=False  ):
# decode(s:str  ,decompress=False):
# ```
# 
# usage:
# ```
# import pyBCELcode
# pyBCELcode.encode(b"123",True)
# pyBCELcode.encode("$$BCEL$$....",True)
# 
# ```
# 
# 
# JAVA中把类生成BCEL:
# ```
#  com.sun.org.apache.bcel.internal.classfile.JavaClass cls = com.sun.org.apache.bcel.internal.Repository.lookupClass(A01_agent.class);//将class对象表示java字节码的对象javaclass
#             System.out.println("length"+cls.getBytes().length);
#             String code = com.sun.org.apache.bcel.internal.classfile.Utility.encode(cls.getBytes(), true);//将java字节码对象javaclass转化为JavaClass格式的字节码
#             System.out.println("length"+code.length());
#             System.out.println("$$BCEL$$" + code);//这是前缀要求
# ```

# In[ ]:




