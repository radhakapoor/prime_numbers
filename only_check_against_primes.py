#incremement n by 1; 
#only check it against previous primes. 

prime_numbers = [2,3]
not_factors = []



def prime():
    #print "prime numbers up top are: "
    #print prime_numbers
    n = prime_numbers[-1]
    n = n + 1
    #print "n up top is: "
    #print n
    while n > 1 and n < 1000000:
        for p in prime_numbers:
            if n % p != 0:
                #print "p in the list iternation is: "
                #print p
                #print "n in the list iternation is:"
                #print n
                not_factors.append(p)
                #print "not factors of n are: "
                #print not_factors
            #elif n % p == 0:
                #print "p in the list iternation is: "
                #print p 
                #print "n in the list iternation is: "
                #print n
            
        if len(not_factors) == len(prime_numbers):
            prime_numbers.append(n)
            #print "prime numbers are: "
            #print prime_numbers
            
        n = n + 1
        del not_factors[:]
        #print "n at the bottom is: "
        #print n
        #print "prime numbers are: "
        print prime_numbers
    #print prime_numbers
        
        
        

        
        
print prime()

        
#def check_factorization(x,pn):          
    #for p in pn:
        #while x > 1 and x % p == 0:
            #prime_factors.append(p)
            #x = x / p
            #print x
    #print prime_factors       
