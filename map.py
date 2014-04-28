import numpy
import time
import field

class BaseMap(object):
	def __init__(self, map=None, shape=None, retain=False):
		#Pass BaseMap instance (or subclass) as map to create map of same size eg. BaseMap(map=TestMap)
		#set retain to True to copy information eg. BaseMap(map=TestMap, retain=True)
		#Pass a tuple of (width, height) as shape to create a blank map of give size eg. BaseMap(shape=(10,10))
		if not map == None:
			if retain == True:
				self.map = numpy.copy(map.map)
			else:
				self.map = numpy.zeros(shape=map.shape)
				
		elif not shape == None:
			self.map = numpy.zeros(shape=shape)
		
		else:
			raise Exception
			
		self.shape = self.map.shape
		self.changed = False	
		
	def get(self, position):
		return self.map[position]
		
	def set(self, position, value):
		self.map[position] = value
		self.changed = True
		return self
		
class StaticMap(BaseMap):
	def addObstacle(self, Positions):
		#Positions - list of tuples of positions to mark eg. [(2,5), (2,6), (2,7)]
		#TODO: change to take a list of objects and store Type instead of 1
		for coord in Positions:
			if not self.map[coord] == 1:
				self.set(coord, 1)
		return self
		
class StaticCostField(BaseMap):
	def __init__(self, staticmap):
		BaseMap.__init__(self, shape=staticmap.shape)
		self.buildMap(staticmap.map)
		
	def buildMap(self, staticmap):
		field.buildStaticCostField(staticmap, self.map)
		
	
class DynamicCostField(BaseMap):
	pass
		
		
class MapHandler(object):
	def __init__(self):
		self.cache = {}
		
		
	def getFlowField(self, MovementType, Target):
		key = '|'.join(map(str, (MovementType, Target)))
		field = self.cache.get(key, None)
		if field == None:
			#Generate Fields
			pass
		return field
		