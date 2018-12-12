from itertools import *
s = raw_input().upper()
l = [ ord(c)-ord('A') for c in s ]
lsum0 = sum(l)
lsum1 = lsum0+len(l)
base26 = reduce( (lambda x,y : 26*x+y ), l, 0 )
pro = reduce( (lambda x,y : x*(y+1)), l, 1 )
scrabble_nl = [1,3,5,2,1,4,3,4,1,4,3,3,3,1,1,3,10,2,2,2,4,4,5,8,8,4]
scrabble_int = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
snl = reduce( (lambda x,y : x+scrabble_nl[y] ), l, 0 )
sen = reduce( (lambda x,y : x+scrabble_int[y] ), l, 0 )
from math import sqrt
def pt(n):
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def primes(n=2, end=float('inf')):
    while n < end:
        if pt(n):
            yield n
        n += 1
pn = [ p for (p,i) in zip(primes(),range(26)) ]
prime_prod = reduce( (lambda x, y: x*pn[y]), l, 1 )
prime_sum = reduce( (lambda x, y: x+pn[y]), l, 0 )
def fibonacci():
	(a,b) = (0,1)
	while True:
		yield b
		(a,b) = (b,a+b)
fn = [ f for (f,i) in zip(fibonacci(),range(26)) ]
fibo_sum = reduce( (lambda x, y: x+fn[y]), l, 0 )



#hawk = reduce( (lambda x,(c,p): x*(p**c) ), zip(l,primes()), 1 )


print lsum0
print lsum1
print snl
print sen
print base26
print pro
print prime_prod
print prime_sum
print fibo_sum
#print hawk