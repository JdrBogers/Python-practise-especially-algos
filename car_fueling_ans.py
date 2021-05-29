# python3
import sys


def compute_min_refills(distance, tank, stops):
	refil = 0
	location = 0
	nextlocation=0
	stops.append(distance)
	stops.insert(0,0)
	while stops[location]+tank<distance:
		location = nextlocation
		#print(stops[currentpos])
		while  nextlocation < len(stops) -1 and stops[nextlocation +1] <= stops[location] + tank :
			nextlocation = nextlocation + 1    
		if stops[location] + tank < distance:
			refil += 1
		if nextlocation == location:
			return -1
	return refil

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
