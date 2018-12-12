import sys, re
off = 1
if len(sys.argv) > 1 and sys.argv[1] == '0':
	off = 0
s = raw_input()
while s != '':
	print ''.join([ chr( int(n)+ord('A')-off ) for n in re.findall('\d+',s) ])
	s = raw_input()