deg=input("Enter degree Fahrenheit as f and Celsius as c:")
try:
    if(deg!='c'and deg!='f'):
        print("Enter the valid degree as only c or f!")
    elif(deg=='f'):
        temp=int(input("Enter the degree:"))
        cel=(temp-32)/1.8
        print("Celsius = ",cel)
    else:
        temp=int(input("Enter the degree:"))
        fah=(temp*1.8)+32
        print("Fahrenheit = ",fah)
except ValueError:
    print("Invalid temperature! Enter only integer as temperature..")
