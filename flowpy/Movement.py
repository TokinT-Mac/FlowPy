import inspect
import sys
	
class TypeHandler(object):
	def __init__(self):
		self.available = self.loadTypes()
		
		
	def loadTypes(self):
		available = {}
		index = 0
		for type in self.findTypes():
			available[type] = index
			index = index + 1
		return available
		
	def findTypes(self):
		return [
			cls	for name, cls in inspect.getmembers(sys.modules[__name__])
					if inspect.isclass(cls) and issubclass(cls, sys.modules[__name__].BaseType) and not cls is sys.modules[__name__].BaseType
		]
		
	def getIndex(self, type):
		return self.available[type]

class BaseType(object):	
	def __init__(self):
		self.BaseSpeed = 1
		#Values < 255
		self.Traction = 100
		self.movementType = self.__class__.__name__
		
	def getSpeed(self, Cost):
		if Cost < self.Traction:
			scalar = 1.0 - float(Cost)/float(self.Traction)
			return round(self.BaseSpeed*scalar, 2)
		else:
			return 0		
			
	def typeIndex(self):
		return getIndexOfType(type(self))
		
class Legged(BaseType):
	def __init__(self):
		BaseType.__init__(self)
		self.BaseSpeed = 5
		self.Traction = 100
	
class Wheeled(BaseType):
	def __init__(self):
		BaseType.__init__(self)
		self.BaseSpeed = 10
		self.Traction = 150
		
class Tracked(BaseType):
	def __init_(self):
		BaseType.__init__(self)
		self.BaseSpeed = 8
		self.Traction = 200
		
def getIndexOfType(type):
	return TypeHandler().getIndex(type)