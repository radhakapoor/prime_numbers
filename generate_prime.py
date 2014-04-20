#generating prime numbers

n = 2.0
d = 2.0


pn = []#list of all the prime numbers 
factors = [] #factors of the number (prime or not)


def main():    
    prime(n,d)
    

def prime(n,d):
    while d > 1 and d < 100:              
        d = d - 1
                       
        if n % d == 0:            
            factors.append(d)
            print "Factors are: "
            print factors
            
            if len(factors) == 1 and 1.0 in factors:
                print str(n) + " is prime!"
                pn.append(n)                
                n = n + 1
                d = n               
                del factors[:]
                print 'Prime numbers are: '
                print pn
            else:
                n = n + 1
                d = n                
                del factors[:]
                print 'Prime numbers are: '
                print pn
                



if __name__ == '__main__':
    main()               
        
         