x=input("enter the no")
v=len(x)
n=int(x)
m=n
s=0
while(n>0):
    l=n%10
    s=s+(l**v)
    n=n//10
print(s)
if s==m:
    
        print("armstring number")
else:
        print("not an armstring number")
        
