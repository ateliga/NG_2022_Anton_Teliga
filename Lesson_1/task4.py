print("Enter the coefficients for the equation:")
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

D = b**2 - 4*a*c

if D < 0:    
    print ("no roots")
elif D == 0:    
    x = (-b + D** .5) / (2*a)
    print ("D = ", D)
    print ("one root: ", x)
else:   
    x1 =  (-b + D** .5) / (2*a)
    x2 =  (-b - D** .5) / (2*a)
    print ("D = ", D)
    print ("first root =  ", x1)
    print ("second root =  ", x2)