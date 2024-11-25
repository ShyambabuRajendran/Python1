a =  int (input ('Enter a 3 digit number : '))
print ( ' Given digit  is', a)
c = (a%1000)//100
print (' First digit (a) is ', c)
d = (a%100)//10
print (' Second digit (b) is ', d)
e = (a%10)
print (' Third digit (c) is', e)
f = c*c*c
g = d*d*d
h = e*e*e
i = f+g+h
print ('Total : a^3 + b^3 + c^3 is', i)
while  i == a:
    print ('Given Number is an Armstrong Number')
else:
    print ('Given number is NOT an Armstrong number')