a=5
print(type(a))
b=1.2
print(type(b))
print(5+4)
print(4/3)  #neni celociselne, ale desetinne
print(4//3) #celociselne
s1="hello"
s2=' universe'
print(s1+s2)
print(s1[1:3])

l=[1,2,3]
t=(1,2,3)
print(l)
print(t)
l[0]=4  #tu to jde
#t[0]=4  #toto je jako konst, nepujde
l.append(5)

d={'a':1, 'b':2}
print(d)
d['c']=3
print(d)

def fun(a,b):
    return a+b
print(fun(2,3))
print(fun("a", "b"))


tmp=[1,2,3,4]
for i in tmp:
    print('hodnota:',i,'cosi',tmp[i])
