x=input("1:")
y=input("2:")
f=0
x1=len(x)
y1=len(y)
z1=x1+y1
if(z1<=20):
    for i in range(x1):
        if(x[i]!='z'):
            f=1
    for i in range(y1):
        if(y[i]!='o'):
            f=1
    if(f==0):
        if(2*x1==y1):
            print(x+y)
        else:
            print("Invalid!")
    else:
        print("No")


'''
z=input("Enter:")
z1=len(z)
flag=0
x=[]
y=[]
if(z1<=20):
    for i in range(z1):
        if(z[i]=='z'):
            x.append(z[i])
        elif(z[i]=='o'):
            y.append(z[i])
            for j in range(i,z1):
                if(z[j]=='z'):
                    flag=z
                else:
                    continue
        else:
            print("No")
    if(flag==0):
        x1=len(x)
        y1=len(y)
        if(2*x1==y1):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")

'''
