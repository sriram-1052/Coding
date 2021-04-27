a=input("Enter the character:\n");
b[100]=0
n=len(a)
if(1<=n<=1000):
  for i in n:
    if((a[i]!=a[i+1])or(a[i]!=a[i-1])):
      b[i]=a[i]
    else:
      i+=1
  i+=1
print(b)
