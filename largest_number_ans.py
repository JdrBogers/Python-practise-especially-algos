#Uses python3

import sys

def superior(x, y):
	jan = str(x)
	modaal = str(y)
	temp=modaal
	modaal +=jan
	jan +=temp
	if int(jan)>int(modaal):
		return True
	return False

def largest_number(a):
	l = [0]*len(a)
	res = ""
	maxd = -1
	while 0 in l: 
		maxd = 0
		for i in range(len(a)):
			if superior(a[i],maxd) and l[i] ==0:
				maxd = a[i]
				index = i
		l[index]	=1	
		res +=str(maxd)
	return res	

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
