a=int(input('x: '))
b=int(input('y: '))
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                print(i,'is composite')
                break
    else:
        print(i,'is prime')
c=a
d=b
s1=0
s2=0
for i in range(c,d+1):
   for j in range(2,i):
       if i%j==0:
           s1+=1
           break
    else:
        s2+=1
print(s2,'prime and ',s1,'composite numbers')
       
           
       
    
