#check if a number is prime

import sys

n = float(sys.argv[1])
d = n


factors = []

 
while d > 1:
    d = d - 1       
    if n % d == 0:        
        factors.append(d)
        if len(factors) == 1 and 1.0 in factors:            
            print str(n) + ' is prime!'            
        else:
            print str(n) + ' is not prime'
    
 
    
