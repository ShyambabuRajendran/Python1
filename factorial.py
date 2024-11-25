#5!=5x4x3x2x1
n=int(input('Enter the value:'))
a=1
if (n==0 or n==1):
    a=1
else:
    for i in range (2,n+1):
        a=a*i
print("The factorial is",a)


    #i=1,fact=1*1
    #i=2,fact=1*2
    #i=3,fact=2*3
    #i=4,fact=6*4
    #i=5,fact=24*5
    