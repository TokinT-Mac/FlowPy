import numpy

def buildStaticCostField(map, dest):
	for (x,y), value in numpy.ndenumerate(map):
		if value != 0:
			dest[(x,y)] = 255
	return dest
	
def genCostForObject(radius, fade, basecost):
	distance = 0
	cost=round(basecost*fade)
	while distance <=radius:
		for x in range(distance+1):
			yield (x, distance-x), int(cost)
			if distance-x != 0: yield (x, -(distance-x)), int(cost)
			if x != 0: yield (-x, distance-x), int(cost)
			if x != 0 and distance-x != 0: yield (-x, -(distance-x)), int(cost)
		distance += 1
		cost = round(cost*fade)