# Uses python3
import sys

def optimal_summands(n):
    res = []
    cumsum=0
    x=0
    for i in range(n):
    	x +=1
    	if(cumsum>=n):
    		break
    	r = opsummands(n, x, cumsum)
    	res.append(r)
    	cumsum +=r	
    return res

def opsummands(n ,x ,cumsum):
	if (cumsum+x+x+1)>n:
		return n - cumsum
	return x

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
