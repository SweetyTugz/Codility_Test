st='257'
x=int(st)
y=hex(x).split('x')[-1]
# print(y)
count=0
hexastring=['A','B','C','D','E','F','I','O','a','b','c','d','e','i','o']
m=(str(y).upper())

# print(m)
z=[i for i in m]
m=[]
for i in z:
    if i=='1':
       m.append("I")
    else:
        if i=='0':
            m.append("O")
        else:
            m.append(i)

for i in m:
    print(i)
    if i in hexastring:
        count=1

if count==1:
    print(m)
else:
    print("ERROR")
