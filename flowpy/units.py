import Movement

class UnitManager(object):
	def __init__(self):
		#add new attributes to index here
		self.__index = ('type', 'task', 'position')
		self.units = {}
		for item in self.__index:
			self.units[item] = {}
		
	def addUnit(self, unit):
		for attribute in self.units:
			value = getattr(unit, attribute)
			if value in self.units[attribute]:
				self.units[attribute][value].append(unit)
			else:
				self.units[attribute][value] = [unit]
			
	def getUnits(self, **kwargs):
		#takes any key found in self.__index eg. getUnits(type='BaseUnit') - getUnits(type='Citizen', task='Idle')
		firstLoop = True
		results = []
		for attribute, value in kwargs.iteritems():
			if value in self.units[attribute]:
				if not firstLoop:
					matching = []
					for unit in self.units[attribute][value]:
						if unit in results:
							matching.append(unit)
					results = matching
				else:
					results = self.units[attribute][value]
			firstLoop = False

		#results = set(results)
		return results
			
class BaseUnit(object):
	def __init__(self, position = (0,0), task = None):
		self.position = position
		self.task = task
		self.type = self.__class__.__name__
		
		
class Citizen(BaseUnit, Movement.Legged):
	def __init__(self, position = (0,0), task = None):
		self.hp = 100
		BaseUnit.__init__(self, position, task)
		Movement.Legged.__init__(self)
		

def stress_test(units, variety):
	manager = UnitManager()
	for pos in range(variety/2):
		limit = int(units - round(units/variety))
		task = 1
		for x in range(units):
			if units - x == limit:
				task = task + 1
				limit = units - (round(units/variety)*task)
			y = BaseUnit(task=task, position=pos)
			manager.addUnit(y)
		
	raw_input()
	return manager
		
		