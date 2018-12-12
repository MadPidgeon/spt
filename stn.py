import sys
off = 1
if len(sys.argv) > 1 and sys.argv[1] == '0':
	off = 0
s = raw_input().upper()
while s != '':
	print " ".join([ str( ord(c)-ord('A')+off ) if c.isalpha() else '' for c in s ])
	s = raw_input().upper()