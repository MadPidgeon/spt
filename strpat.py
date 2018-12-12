s = raw_input().upper()
l = [ ord(c)-ord('A') for c in s ]
lsum0 = sum(l)
lsum1 = lsum0+len(l)
base26 = reduce( (lambda x,y : 26*x+y ), l, 0 )
