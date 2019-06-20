import math
pi, exp, erf = math.pi, math.exp, math.erf

# fibonacci series using golden ration
def fib(n):
    ratio = (1 + math.sqrt(5)) / 2
    return int( ((ratio ** n) / (math.sqrt(5))) + 0.5)

# if you need to print the fibonacci series use this code
def fibonacci(n):
    a, b = 0, 1
    values = []
    for _ in range(n+1):
        values.append(a)
        a, b = a + b, a     
    return b, values

def fact(n):
    j = 1
    for i in range(1,n+1):
        j *= i
    return j

def combn(n,k):
    num = 1
    for i in range(n-k+1,n+1):
        num *= i
    return (num // fact(k))

def perm(n,k):
    prod = 1 
    for i in range(n-k-1,n+1):
        prod *= i
    return prod

def b(n, k, p):
    return combn(n,k) * p**k * (1-p)**(n-k)

def geo(n,p):
    return ((1-p)**(n-1) * p)

def poi(mu,k):
    return ( (mu**k) * (exp(-mu))) / (fact(k) )

def norm(x,mu,std):
    var = float(std)**2
    p1 = 1 / (2*pi*var)**.5
    p2 = exp(- ((mu-x)**2) / (2*var) )
    return p1*p2

def phi(x,mu,sigma):
    return 0.5*(1+erf((x-mu)/(sigma * (2**0.5))))

def clt(x,n,mu,sigma):
    mu_ = n*mu
    sigma_ = (n**.5) * sigma
    return phi(x, mu_, sigma_)

#%%
n, k, p, mu = 10, 5, 1/5, 3

print('Fibonacci({}) = '.format(n),fib(n))
print('Fibonacci({}) = '.format(n),fibonacci(n)[1])
print('Factorial({}) = '.format(n), fact(n))
print('Combination({},{}) = '.format(n,k), combn(n,k))
print('Permutation({},{}) = '.format(n,k), perm(n,k))
print('Binomial({},{},{}) = '.format(n,k,p), round(b(n,k,p),4))
print('Geometrical({},{}) = '.format(n,p), round(geo(n,p),4))
print('Poisson_Distribution({},{}) = '.format(mu,k), round(poi(mu,k),4))
print('Standard Normal Distribution(80,70,10) = ',round((phi(x=80, mu=70, sigma=10)),4))
print('Central Limit Theorem(9800, 49, 205, 15) = ',round(clt(x=9800, n=49, mu=205, sigma=15),4))

