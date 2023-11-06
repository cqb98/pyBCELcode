# pyBCELcode
BCEL code/decode in pure python

for java secure research

fastjson srcure research



## define:

```
encode(b:bytes,compress=False  ):
decode(s:str  ,decompress=False):
```

## usage:
```
import pyBCELcode
pyBCELcode.encode(b"123",True)
pyBCELcode.encode("$$BCEL$$....",True)

```


## JAVA中把类生成BCEL:
```
 com.sun.org.apache.bcel.internal.classfile.JavaClass cls = com.sun.org.apache.bcel.internal.Repository.lookupClass(A01_agent.class);//将class对象表示java字节码的对象javaclass
            System.out.println("length"+cls.getBytes().length);
            String code = com.sun.org.apache.bcel.internal.classfile.Utility.encode(cls.getBytes(), true);//将java字节码对象javaclass转化为JavaClass格式的字节码
            System.out.println("length"+code.length());
            System.out.println("$$BCEL$$" + code);//这是前缀要求
```
